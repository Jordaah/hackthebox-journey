<template>
<div class="button-container" @click="$emit('spaceClick')">
    <h1>{{ title }}</h1>
</div>
</template>

<script>
export default {
    name: "SpaceButton",
    props: {
        title: String,
    }
}
</script>

<style>
.button-container {
    margin-left: auto;
    margin-right: auto;
    width: fit-content;
    border-radius: 10px;
    background-color: #0E0788;
}

.button-container h1 {
    color: white;
    padding: 10px;
}

.button-container:hover {
    box-shadow: 5px 5px 5px #EF9DE9;
    cursor: pointer;
}
</style>
