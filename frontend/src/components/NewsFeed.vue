<template>
  <div class="container">
    <div class="CreateForm">
      <h3 class="mb-3">Create a Post</h3>
      <div class="card form-group d-flex flex-column mb-4">
        <div class="form-field ms-2">
          <label for="postTitle" class="d-flex text-start">Title:</label>
        </div>
        <div class="form-field mx-2 mb-2">
          <input id="postTitle" class="w-100 ms-auto border-1 rounded-1" :placeholder="titlePlaceholder" v-model="title"/>
        </div>
        <div class="form-field ms-2">
          <label for="postContent" class="d-flex text-start">Content:</label>
        </div>
        <div class="form-field mx-2 mb-2">
          <textarea id="postContent" class="w-100 ms-auto rounded-1" :placeholder="descriptionPlaceholder" v-model="description"></textarea>
        </div>
        <div class="form-field d-flex justify-content-end mb-2 me-2">
          <button class="btn btn-primary" @click="createPost">Post</button>
        </div>
      </div>
    </div>
    <Posts />
  </div>
</template>

<script>
import axios from 'axios'
import Posts from './Posts.vue'

export default {
  name: 'NewsFeed',
  props: {
    titlePlaceholder: String,
    descriptionPlaceholder: String
  },
  components: {
    Posts
  },
  data() {
    return {
      title: null,
      description: null,
      owner: 1
    }
  },
  methods: {
    async createPost() {
      try {
        const response = await axios.post('http://localhost:8000/api/posts/', {
          title: this.title,
          description: this.description,
          owner: this.owner
        });
        console.log(response);
        // Reload if response is successful
        if (response.status === 201) {
          window.location.reload();
        }
      } catch(error) {
        console.error("Error creating post: ", error);
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
