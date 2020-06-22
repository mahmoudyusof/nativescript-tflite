<template>
  <Page>
    <ActionBar backgroundColor="#3700b3">
      <Label text="Object Detection"></Label>
    </ActionBar>
    <DockLayout width="100%" height="100%" stretchLastChild="false">
      <ScrollView dock="top" style.zIndex="1" height="500" scrollableHeight="10">
        <StackLayout class="home-panel">
          <!--Add your page content here-->
          <Image v-for="i in count" :key="i" src="~/assets/crime.png" margin="10" stretch="none" />
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
        <Button text="Button" class="noshad" @tap="onButtonTap" />
        <Button text="Button" class="noshad" @tap="onButtonTap" />
        <Button text="Button" class="noshad" @tap="onButtonTap" />
      </FlexboxLayout>
    </DockLayout>
  </Page>
</template>

<script>
import * as camera from "nativescript-camera";
export default {
  data() {
    return { count: 1 };
  },
  methods: {
    onButtonTap() {
      this.count++;
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
