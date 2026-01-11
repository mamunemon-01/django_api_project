<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <div class="d-flex bg-primary justify-content-center align-items-center">
      <h1 id="app-title" class="ps-2 py-1 text-light">HeadBook</h1>
      <div v-if="isLoggedIn" class="ms-auto pe-2 py-1">
        <button class="btn btn-light fw-bold" @click="handleLogout">Log Out</button>
      </div>
    </div>
    <div id="app-content">
      <NewsFeed v-if="isLoggedIn" titlePlaceholder="What's on your head?" descriptionPlaceholder="Share your thoughts..."/>
      <LogIn v-else @login-success="isLoggedIn = true"/>
    </div>
  </div>
</template>

<script>
import NewsFeed from './components/NewsFeed.vue'
import LogIn from './components/LogIn.vue'
import axios from 'axios';

export default {
  name: 'App',
  components: {
    NewsFeed,
    LogIn
  },
  data() {
    return {
      isLoggedIn: false
    }
  },
  mounted() {
    // Check if the user is already logged in (e.g., by checking a token in localStorage)
    // For simplicity, we'll assume the user is not logged in initially
    this.isLoggedIn = false;
    this.handleLogin();
  },
  methods: {
    async handleLogin() {
      const token = localStorage.getItem('authToken');
      if (token) {
        // Check if token exists and set isLoggedIn accordingly
        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
        try {
          const response = await axios.get('http://127.0.0.1:8000/dj-rest-auth/user/');
          console.log('Retrieved user through token from localStorage:', response);
          if (response.status === 200) {
            this.isLoggedIn = true;
          }
        } catch (error) {
          if (error.status === 401) {
            localStorage.removeItem('authToken');
            delete axios.defaults.headers.common['Authorization'];
          }
          console.error("Failed to retrieve user:", error);
        }
      }
    },
    handleLogout() {
      // Clear the authentication token from localStorage
      localStorage.removeItem('authToken');
      // Remove the Authorization header from axios
      delete axios.defaults.headers.common['Authorization'];
      // Update the isLoggedIn state
      this.isLoggedIn = false;
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  /* Light background for the entire app */
  background-color: #f5f7fa;
  margin-top: 0px;
}
#app-title {
  font-weight: bold;
}
#app-content {
  margin-top: 60px;
}
</style>
