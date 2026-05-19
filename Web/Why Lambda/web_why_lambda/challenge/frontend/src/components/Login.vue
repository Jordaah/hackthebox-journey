<template>
    <div class="login">
        <div>
          <div>
            <label for="username">Username:</label>
            <input type="text" name="username" v-model="username" />
          </div>
          <br/>
          <div>
            <label for="password">Password:</label>
            <input type="password" name="password" v-model="password" />
          </div>
          <SpaceButton :title="'Login'" @spaceClick="performLogin()"></SpaceButton>
        </div>
        <p v-if="showError" id="error">Username or Password is incorrect</p>
    </div>
</template>

<script>
import { post } from "../api";
import SpaceButton from "./SpaceButton.vue";

export default {
    name: "Login",
    components: {
        SpaceButton,
    },
    data() {
      return {
        username: "",
        password: "",
        showError: false
      };
    },
    methods: {
        performLogin(){
            post(
                "/api/login",
                {
                    username: this.username,
                    password: this.password,
                },
            ).then((response) => {
                if (response.status != 200){
                    this.showError = true
                    throw new Error();
                }
                this.showError = false;
                this.$emit("success");
            });
        }
    }
}
</script>

<style>
.login label {
    font-size: 2em;
    margin-right: 20px;
}
.login input {
    height: 2em;
}
</style>