<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>HeadBook</h1>
    <NewsFeed v-if="isLoggedIn" msg="What's on your head?"/>
    <LogIn v-else @login-success="isLoggedIn = true"/>
  </div>
</template>

<script>
import NewsFeed from './components/NewsFeed.vue'
import LogIn from './components/LogIn.vue'

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
}
</style>
