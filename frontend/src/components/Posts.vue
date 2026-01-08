<template>
  <div class="container">
    <h3 class="mb-3">News Feed</h3>
    <div class="PostsContainer">
      <div v-for="post in posts" :key="post.id" class="card mb-3">
        <div class="card-body d-flex justify-content-start flex-column">
          <h5 class="card-title text-start p-2">{{ post.title }}</h5>
          <p class="card-text text-start p-3">{{ post.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ThePosts',
  props: {
    msg: String
  },
  data() {
    return {
      posts: []
    }
  },
  mounted() {
    this.fetchPosts();
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await axios.get('http://localhost:8000/api/posts/');
        this.posts = response.data;
      } catch (error) {
        console.error('Error fetching posts:', error);  
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .card-title {
    background-color: #d0d0d0;
    /* color: ; */
    border-radius: 4px;
  }
</style>
