<template>
  <Page>
    <ActionBar>
      <Label text="Home"></Label>
    </ActionBar>

    <GridLayout>
      <Button @click="inc">{{ counter }}</Button>
      <Label class="info">
        <FormattedString>
          <Span class="fas" text.decode="&#xf135; " />
          <Span :text="counter" />
        </FormattedString>
      </Label>
    </GridLayout>
  </Page>
</template>

<script>
export default {
  data() {
    return { counter: 0 };
  },
  computed: {
    message() {
      return "Blank {N}-Vue app";
    }
  },
  methods: {
    inc() {
      this.counter = this.counter + 1;
    }
  }
};
</script>

<style scoped lang="scss">
@import "~@nativescript/theme/scss/variables/blue";

// Custom styles
.fas {
  @include colorize($color: accent);
}

.info {
  font-size: 20;
  horizontal-align: center;
  vertical-align: center;
}
</style>
