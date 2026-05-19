<template>
<Block :title="title" :description="description">
    <template v-slot:content>
        <Draw />
    </template>
</Block>
</template>

<script>
import Draw from '../components/Draw.vue';
import Block from '../components/Block.vue';

export default {
    name: "TryModel",
    components: {
        Draw,
        Block
    },
    data() {
        return {
            title: "Try out our revolutionary model",
            description: "We heard humans use something called 'digits' from 0-9 because they have only a few fingers, draw one and the model shall predict!",
        }
    }
}
</script>
