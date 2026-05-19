<template>
  <div class="canvas-container">
    <div class="draw">
      <p>Draw here:</p>
      <vue-drawing-canvas 
        ref="VueCanvasDrawing" 
        v-model:image="image" 
        :width="canvasSize" 
        :height="400"
        :stroke-type="strokeType" 
        :line-cap="lineCap" 
        :line-join="lineJoin" 
        :fill-shape="false" 
        :eraser="false"
        :lineWidth="5" 
        :color="color" 
        :background-color="backgroundColor" 
        :initial-image="initialImage" saveAs="png"
        :styles="{
          border: 'solid 1px #000',
        }" 
        :lock="false" 
      />
    </div>
    <div class="arrow">
      <img :src="require(`@/assets/img/arrow.png`)">
    </div>
    <div class="output">
      <p>Result:</p>
      <img :src="image" style="border: solid 1px #000000" />
    </div>
  </div>
  <SpaceButton :title="'Predict'" @spaceClick="submitImage()"></SpaceButton>
  <div v-if="prediction !== null">
    <p class="prediction-text">Model predicted the number was a: <b style='color:#DE58D1'>{{ prediction }}</b></p>
    <p class="prediction-text">Which in our superior number system is <b style='color:#DE58D1'>z0k{{ (prediction + 42) }}</b></p>
    <br/>
    <h2>You <b>human</b> think the prediction is wrong?</h2>
    <p>You are probably wrong, but please file a complaint</p>
    <textarea rows="10" cols="60" v-model="complaint" type=" " />
    <SpaceButton :title="'Complain!'" @spaceClick="submitComplaint()"></SpaceButton>
  </div>
</template>

<script>
import { post } from "../api";
import VueDrawingCanvas from "vue-drawing-canvas";
import SpaceButton from "./SpaceButton.vue";

export default {
  name: "Draw",
  components: {
    VueDrawingCanvas,
    SpaceButton,
  },
  data() {
    return {
      initialImage: [
        {
          type: "dash",
          from: {
            x: 262,
            y: 154,
          },
          coordinates: [],
          color: "#000000",
          width: 5,
          fill: false,
        },
      ],
      x: 0,
      y: 0,
      image: "",
      color: "#000000",
      strokeType: "dash",
      lineCap: "square",
      lineJoin: "miter",
      backgroundColor: "#FFFFFF",
      prediction: null,
      previousImage: null,
      complaint: "",
      canvasSize: window.innerWidth * 0.23,
    };
  },
  mounted() {
    if ("vue-drawing-canvas" in window.localStorage) {
      this.initialImage = JSON.parse(
        window.localStorage.getItem("vue-drawing-canvas")
      );
    }
  },
  methods: {
    submitImage() {
      post(
        "/api/predict",
        {
          image_data: this.image,
        },
      )
      .then((r) => r.json())
      .then((data) => {
        this.prediction = data.prediction
        this.previousImage = this.image;
        this.$refs.VueCanvasDrawing.reset();
      });
    },
    submitComplaint() {
      post(
        "/api/complaint",
        {
            description: this.complaint,
            image_data: this.previousImage,
            prediction: this.prediction,
        },
      ).then(() => this.complaint = "");
    }
  },
};
</script>

<style scoped>
.canvas-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(3, 1fr);
  grid-column-gap: 0px;
  grid-row-gap: 0px;
}

.draw {
  grid-area: 1 / 1 / 4 / 3;
}

.output {
  grid-area: 1 / 4 / 4 / 6;
}

.arrow {
  grid-area: 2 / 3 / 3 / 4;
  color: black;
}

.arrow img {
  width: 100px;
  height: 100px;
}

.prediction-text {
  font-size: 1.5em;
}
</style>