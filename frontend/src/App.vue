<template>
  <div id="app" class="d-flex flex-column min-vh-100">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <div id="app-header" class="d-flex bg-primary shadow position-sticky top-0 justify-content-center align-items-center">
      <h1 id="app-title" class="ps-2 py-1 text-light fw-bold">HeadBook</h1>
      <h3 v-if="isLoggedIn" id="user-name" class="ms-4 text-light fw-bold border rounded-5 p-1">@{{ username }}</h3>
      <div v-if="isLoggedIn" class="ms-auto pe-2 py-1">
        <button class="btn btn-light fw-bold" @click="handleLogout">Log Out</button>
      </div>
    </div>
    <div id="app-content" class="d-flex flex-grow-1 align-items-start">
      <NavBar v-if="isLoggedIn" class="flex-shrink-0" :username="username" @logout="handleLogout"/>
      <!-- <NewsFeed v-if="isLoggedIn" titlePlaceholder="What's on your head?" descriptionPlaceholder="Share your thoughts..."/> -->
      <router-view v-if="isLoggedIn" class="mt-5"/>
      <LogIn v-else class="mt-5 pt-5" @login-success="handleLoginSuccess"/>
    </div>
  </div>
</template>

<script>
// import NewsFeed from './components/NewsFeed.vue'
import LogIn from './components/LogIn.vue'
import axios from 'axios';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    // NewsFeed,
    LogIn,
    NavBar
  },
  data() {
    return {
      isLoggedIn: false,
      username: null
    }
  },
  mounted() {
    // Check if the user is already logged in (e.g., by checking a token in localStorage)
    // For simplicity, we'll assume the user is not logged in initially
    this.isLoggedIn = false;
    this.handlePreviousLogin();
  },
  methods: {
    async handlePreviousLogin() {
      const token = localStorage.getItem('authToken');
      if (token) {
        // Check if token exists and set isLoggedIn accordingly
        axios.defaults.headers.common['Authorization'] = `Token ${token}`;
        try {
          const response = await axios.get('http://127.0.0.1:8000/dj-rest-auth/user/');
          console.log('Retrieved user through token from localStorage:', response);
          if (response.status === 200) {
            this.isLoggedIn = true;
            this.username = response.data.username;
          }
        } catch (error) {
          if (error.status === 401) {
            localStorage.removeItem('authToken');
            localStorage.removeItem('username');
            delete axios.defaults.headers.common['Authorization'];
          }
          console.error("Failed to retrieve user:", error);
          this.username = null;
          this.isLoggedIn = false;
        }
      }
    },
    handleLoginSuccess(){
      this.isLoggedIn = true;
      this.username = localStorage.getItem('username');
    },
    async handleLogout() {
      try {
          const response = await axios.post('http://localhost:8000/dj-rest-auth/logout/');
          console.log("Logout response: ", response);
          if(response.status === 200){
          // Clear the authentication token from localStorage
          localStorage.removeItem('authToken');
          localStorage.removeItem('username');
          this.username = null;
          // Remove the Authorization header from axios
          delete axios.defaults.headers.common['Authorization'];
          // Update the isLoggedIn state
          this.isLoggedIn = false;
          }
      } catch(error) {
          console.error("Error logging out: ", error);
      }
    }
  }
}
</script>

<style>
html, body {
  height: 100%;
}
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
#app-header {
  z-index:1050;
}
</style>
