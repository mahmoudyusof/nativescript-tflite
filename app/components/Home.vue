<template>
  <Page>
    <ActionBar backgroundColor="#3700b3">
      <Label text="Object Detection"></Label>
    </ActionBar>
    <DockLayout width="100%" height="100%" stretchLastChild="false">
      <ScrollView dock="top" style.zIndex="1" height="500" scrollableHeight="10">
        <StackLayout class="home-panel">
          <!--Add your page content here-->
          <Image src="~/assets/crime.png" margin="10" stretch="none" />
          <Image :src="src" margin="10" stretch="none" />
          <Image :src="converted" margin="10" stretch="none" />
        </StackLayout>
      </ScrollView>

      <FlexboxLayout
        class="bottom-nav"
        dock="bottom"
        justifyContent="space-between"
        width="100%"
        height="50"
        backgroundColor="#3700b3"
      >
        <Button text="Upload" class="noshad" @tap="upload" />
        <Button text="Take Pic" class="noshad" @tap="takePic" />
        <Button text="Button" class="noshad" @tap="onButtonTap" />
      </FlexboxLayout>
    </DockLayout>
  </Page>
</template>

<script>
import * as camera from "nativescript-camera";
import axios from "axios";
export default {
  data() {
    return { count: 1, src: "", converted: "" };
  },
  methods: {
    onButtonTap() {
      this.count++;
    },
    upload() {
      axios
        .get("http://192.168.1.8:5000/")
        .then(res => {
          console.log(res.data);
        })
        .catch(e => {
          console.log(e);
        });
    },
    takePic() {
      camera.requestCameraPermissions().then(() => {
        camera
          .takePicture()
          .then(asset => {
            this.src = asset;
          })
          .catch(e => {
            console.log(e);
          });
      });
    }
  }
};
</script>

<style scoped lang="scss">
@import "~@nativescript/theme/scss/variables/blue";

// Custom styles
.bottom-nav {
  border-top-color: black;
  border-top-width: 1px;
  @include colorize($color: accent);
  z-index: 100;
}
.noshad {
  z-index: 0;
}
</style>
