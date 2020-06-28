<template>
  <Page>
    <ActionBar backgroundColor="#3700b3">
      <Label text="Object Detection"></Label>
    </ActionBar>
    <AbsoluteLayout>
      <DockLayout
        width="100%"
        height="100%"
        stretchLastChild="false"
        top="0"
        bottom="0"
        left="0"
        right="0"
      >
        <ScrollView dock="top" style.zIndex="1" height="500" scrollableHeight="10">
          <StackLayout class="home-panel">
            <!--Add your page content here-->
            <Image src="~/assets/crime.png" margin="10" stretch="none" />
            <Image :src="src" margin="10" stretch="none" />
            <Image :src="converted" ref="converted" margin="10" stretch="none" />
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
      <GridLayout height="100%" width="100%" backgroundColor="#fff" v-if="loading">
        <ActivityIndicator top left="50" :busy="true" height="100" width="100"></ActivityIndicator>
      </GridLayout>
    </AbsoluteLayout>
  </Page>
</template>

<script>
import * as camera from "nativescript-camera";
import axios from "axios";
import * as ImageSourceModule from "tns-core-modules/image-source";
export default {
  data() {
    return {
      count: 1,
      src: "",
      converted: "~/assets/crime.png",
      loading: false
    };
  },
  methods: {
    onButtonTap() {
      this.count++;
    },
    upload() {
      this.loading = true;
      ImageSourceModule.ImageSource.fromAsset(this.src)
        .then(src => src.toBase64String("jpg"))
        .then(base64 => {
          return axios.post(
            "http://192.168.1.8:5000/",
            { img: base64 },
            {
              headers: { "Content-Type": "application/json" }
            }
          );
        })
        .then(res => {
          console.log(res.data.slice(0, 20));
          let img = ImageSourceModule.ImageSource.fromBase64Sync(res.data);
          this.converted = img;
          console.log(img);
          console.log(img);
        })
        .catch(e => console.log(e))
        .finally(() => {
          this.loading = false;
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
