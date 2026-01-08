<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1 id="app-title" class="py-2 bg-primary text-light">HeadBook</h1>
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
    const token = localStorage.getItem('authToken');
    if (token) {
      this.isLoggedIn = true;
      axios.defaults.headers.common['Authorization'] = `Token ${token}`;
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
