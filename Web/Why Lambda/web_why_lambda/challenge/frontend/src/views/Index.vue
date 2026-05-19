<template>
<Block :title="title" :description="description">
    <template v-slot:content>
        <SpaceButton :title="'Check out our latest model'" @spaceClick="$router.push('/try');"></SpaceButton>
        <template v-for="banner in banners" :key="banner.title">
            <ImageBanner :image="banner.image" :textContent="banner.textContent" :title="banner.title"></ImageBanner>
        </template>
    </template>
</Block>
</template>

<script>
import {get} from "../api";
import Block from '../components/Block.vue';
import ImageBanner from '../components/ImageBanner.vue';
import SpaceButton from '../components/SpaceButton.vue';

export default {
    name: "Index",
    components: {
        Block,
        ImageBanner,
        SpaceButton,
    },
    data() {
        return {
            title: "Lambda Space Corp",
            description: "We make the life of creatures around the universe better. Why? Because we can.",
            banners: [],
            dataAmount: 0,
            metrics: {
                loss: 0,
                acc: 0,
            },
        }
    },
    methods: {
        async getDataAmount() {
            return await get("/api/data")
                .then((r) => r.json())
                .then((j) => {
                    this.dataAmount = j.count;
                });
        },
        async getMetrics() {
            return await get("/api/metrics")
                .then((r) => r.json())
                .then((j) => {
                    this.metrics.loss = j.loss;
                    this.metrics.acc = j.acc * 100;
                });
        },
        loadBanners() {
            this.getDataAmount()
                .then(() => this.getMetrics())
                .then(() => {
                    this.banners = [
                        {
                            image: require(`@/assets/img/alien.png`),
                            textContent: "is a technique that trains a reward model directly from <b style='color:#DE58D1'>alien</b> \
                                            feedback and uses the model as a reward function to optimize an agent's \
                                            policy using reinforcement learning (RL) through an optimization algorithm.",
                            title: "Reinforcement Learning from Alien Feedback",
                        },
                        {
                            image: require(`@/assets/img/star.png`),
                            textContent: `With out outstanding dataset of <b style='color:#DE58D1'>${this.dataAmount}</b> handwritten digits pictures
                                            we acheive a <b style='color:#DE58D1'>${this.metrics.acc}%</b> accuracy with a loss of <b style='color:#DE58D1'>${this.metrics.loss}</b>.
                                            We at Lambda Space Corp. help our fellow aliens by translating silly human 'digits' in our superior, far better number system.` ,
                            title: "Our community matters to us",
                        },
                        {
                            image: require(`@/assets/img/payment.png`),
                            textContent: `Supporting the mega server up on our spaceship is really expensive, please consider sending us some 
                                            galactic gold doubloons at our crypto wallet here: 123space123 (yes everybody in space has crypto)`,
                            title: "Help us help you"
                        }
                    ];
                });
            
        }
    },
    created() {
        this.loadBanners();
    }
}
</script>
