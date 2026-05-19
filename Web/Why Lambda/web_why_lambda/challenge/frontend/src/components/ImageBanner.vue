<template>
    <div class="banner">
        <div class="image-container">
            <img :src="image" class="image">
        </div>
        <div class="text-container">
            <h2 class="banner-title">{{ title }}</h2>
            <span class="text" v-html="textContent"></span>
        </div>
    </div>
</template>

<script>
export default {
    name: "ImageBanner",
    props: {
        image: String,
        title: String,
        textContent: String,
    }
}
</script>

<style>
.banner {
    margin-top: 100px;
    width: 100%;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-template-rows: repeat(5, 1fr);
    grid-column-gap: 25px;
    grid-row-gap: 0px; 
}

.image-container {
    grid-area: 1 / 1 / 4 / 3;
}

.image {
    width: 300px;
    height: 300px;
}

.text-container {
    grid-area: 1 / 3 / 4 / 6;
    text-align: left;
    margin-right: 200px;
    font-size: 1.5em;
    line-height: 40px;
    padding: 10px;
}

.banner-title {
    font-size: 2em;
}
</style>