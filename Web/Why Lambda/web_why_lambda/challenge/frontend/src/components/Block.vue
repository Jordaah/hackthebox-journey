<template>
    <div class="container">
        <h1 v-if="title" class="title"> {{ title }} </h1>
        <h2 v-if="description" class="desc">{{ description }}</h2>
        <br/>
        <slot name="content">
        </slot>
    </div>
</template>

<script>
export default {
    name: "Block",
    props: {
        title: String,
        description: String,
    }
}
</script>

<style>
.container {
    width: 70%;
    background-color: rgba(125, 213, 244, 0.8);
    margin-left: 15%;
    margin-top: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
    border-width: 50px;
    border-style: solid;
    border-radius: 10px;
    border-image: url("~@/assets/img/pixel.png") 50% repeat;
}
.title {
    color: #DE58D1;
    font-weight: bolder;
    font-size: 3em;
    text-shadow: 3px 3px 1px #8C089C;
}
.desc {
    line-height: 30px;
}
</style>