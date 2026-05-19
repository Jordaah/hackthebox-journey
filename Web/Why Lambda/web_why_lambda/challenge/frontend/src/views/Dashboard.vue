<template>
<Block :title="title" :description="description">
    <template v-slot:content>
        <Login @success="showDashboard()" v-if="!loggedIn"/>
        <div v-else>
            <div class="upload">
                <h1 class="upload-title">Upload and test a new version of the model</h1>
                <input type="file" ref="file"/>
                <SpaceButton :title="'Submit'" @spaceClick="submitModel()"></SpaceButton>
                <p v-if="uploadText">{{ uploadText }}</p>
            </div>
            <br/>
            <div v-if="complaints.length < 1">
                <h2>No complaints!</h2>
            </div>
            <template v-else v-for="(c, key) in complaints" :key="key">
                <ImageBanner :title="c.description" :image="c.image_data" :textContent="getPredictionText(c)"></ImageBanner>
            </template>
        </div>
    </template>
</Block>
</template>

<script>
import Login from '../components/Login.vue';
import Block from '../components/Block.vue';
import ImageBanner from '../components/ImageBanner.vue';
import {get, postForm} from "../api";
import SpaceButton from "../components/SpaceButton.vue";

export default {
    name: "TryModel",
    components: {
        Login,
        Block,
        ImageBanner,
        SpaceButton,
    },
    data() {
        return {
            title: "Alien Dashboard",
            description: "Where are admins go to cry after reading your complaints",
            complaints: [],
            modelFile: null,
            uploadText: null,
            loggedIn: false,
        }
    },
    methods: {
        showDashboard() {
            get("/api/internal/complaints")
            .then((response) => { 
                if (response.status != 200) {
                    this.showError = true
                    throw new Error();
                }
                return response.json()
            })
            .then((content) => {
                this.loggedIn = true;
                this.complaints = content;
            })
        },
        getPredictionText(complaint) {
            return `<p>Our amazing model said the image represented the digit: <b>${complaint.prediction}</b></p>`;
        },
        submitModel() {
            const formData = new FormData();
            formData.append('file', this.$refs.file.files[0]);
            postForm(
                "/api/internal/model",
                formData,
            )
            .then((response) => response.json())
            .then((content) => {
                this.uploadText = content.message;
            });
        }
    },
    created() {
        this.showDashboard();
    }
}
</script>

<style>
.upload {
    background-color: rgba(255, 255, 255, 0.8);
    height: 250px;
}
.upload-title {
    padding-top: 50px;
}
</style>
    