<template>
  <div class="container">
    <div class="LoginForm">
      <h3 class="mb-3">Sign In</h3>
      <div class="card form-group d-flex flex-column mb-4">
        <div class="form-field mb-2 d-flex align-items-center m-2">
          <label for="userName" class="me-1">User Name:</label>
          <input id="userName" class="w-100 ms-auto" v-model="username"/>
        </div>
        <div class="form-field d-flex align-items-center m-2">
          <label for="password" class="me-1">Password:</label>
          <input id="password" class="w-100 ms-auto" type="password" v-model="password"/>
        </div>
        <div class="form-field d-flex justify-content-end mb-2 me-2">
          <button class="btn btn-primary" @click="logIn">Log In</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'NewsFeed',
  props: {
    msg: String
  },
  data() {
    return {
      username: null,
      password: null,
      owner: 1
    }
  },
  methods: {
    async logIn() {
      try {
        const response = await axios.post('http://localhost:8000/dj-rest-auth/login/', {
          username: this.username,
          password: this.password
        });
        console.log("Login response: ",response);
        if(response.status === 200){
          this.$emit("login-success");
        }
        // window.location.reload();
      } catch(error) {
        console.error("Error logging in: ", error);
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>