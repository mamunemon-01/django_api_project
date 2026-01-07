<template>
  <div class="container">
    <div class="CreateForm">
      <h3 class="mb-3">Create a Post</h3>
      <div class="card form-group d-flex flex-column mb-4">
        <div class="form-field mb-2 d-flex align-items-center m-2">
          <label for="postTitle" class="me-1">Title:</label>
          <input id="postTitle" class="w-100 ms-auto" v-model="title"/>
        </div>
        <div class="form-field d-flex align-items-center m-2">
          <label for="postContent" class="me-1">Content:</label>
          <textarea id="postContent" class="w-100 ms-auto" :placeholder="msg" v-model="description"></textarea>
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
    msg: String
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
