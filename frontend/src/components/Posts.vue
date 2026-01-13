<template>
  <div class="container">
    <div v-if="isPostEditFormVisible" class="modal-backdrop d-flex justify-content-center align-items-center" @click="isPostEditFormVisible = false">
      <div id="postEditForm" class="modal-content form-group w-50 border border-2 rounded-2 bg-light" @click.stop>
        <h3 class="mb-3 mt-2 fw-bold">Edit Post</h3>
        <div class="form-field ms-2">
          <label for="postTitle" class="d-flex text-start">Title:</label>
        </div>
        <div class="form-field mx-2 mb-2">
          <input id="postTitle" class="w-100 ms-auto border-1 rounded-1" v-model="currentTitle"/>
        </div>
        <div class="form-field ms-2">
          <label for="postContent" class="d-flex text-start">Content:</label>
        </div>
        <div class="form-field mx-2 mb-2">
          <textarea id="postContent" class="w-100 ms-auto rounded-1" v-model="currentDescription"></textarea>
        </div>
        <div class="form-field d-flex justify-content-end mb-2 me-2">
          <button class="btn btn-light border border-3 fw-bold me-2" @click="isPostEditFormVisible = false">Cancel</button>
          <button class="btn btn-primary fw-bold" @click="updatePost">Update</button>
        </div>
      </div>
    </div>
    <h3 class="mb-3 fw-bold">News Feed</h3>
    <div class="PostsContainer">
      <div v-for="post in posts" :key="post.id" class="card mb-3">
        <div class="card-body d-flex justify-content-start flex-column">
          <div class="card-header d-flex justify-content-between align-items-center">
            <h5 class="card-title text-start text-primary p-2">{{ post.title }}</h5>
            <i class="text-muted ms-auto">@{{ post.owner.username }}</i>
            <!-- Three dot icon with build in library/module -->
            <i v-if="checkIfOwnPost(post)" class="bi bi-three-dots-vertical" @click="toggleOptionsDropdown(post.id)"></i>
            <ul v-if="checkIfOwnPost(post)" :id="`postActions${post.id}`" @blur="toggleOptionsDropdown(post.id)" class="d-none form-select form-select-sm w-auto ms-2" >
              <li class="dropdown-item" value="edit" @click="editPost(post)">Edit</li>
              <li class="dropdown-item" value="delete" @click="deletePost(post)">Delete</li>
            </ul>
          </div>
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
      posts: [],
      currentId: null,
      currentTitle: null,
      currentDescription: null,
      isPostEditFormVisible: false
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
        // console.log('Fetched posts:', this.posts);
      } catch (error) {
        console.error('Error fetching posts:', error);  
      }
    },
    checkIfOwnPost(post) {
      return post.owner.username === localStorage.getItem('username');
    },
    async deletePost(post) {
      try {
        const response = await axios.delete(`http://localhost:8000/api/posts/${post.id}/`);
        console.log('Post deleted:', response);
        // Refresh the posts list after deletion
        this.fetchPosts();
      } catch (error) {
        console.error('Error deleting post:', error);
      }
    },
    toggleOptionsDropdown(postId) {
      const dropdown = document.getElementById(`postActions${postId}`);
      console.log('Toggling dropdown for post ID:', postId, dropdown);
      dropdown.classList.toggle('d-none');
    },
    editPost(post) {
      this.currentId = post.id;
      this.isPostEditFormVisible = true;
      this.currentTitle = post.title;
      this.currentDescription = post.description;
      this.toggleOptionsDropdown(post.id);
    },
    async updatePost() {
      console.log('Updating post:', this.currentTitle, this.currentDescription);
      try {
        const response = await axios.put(`http://127.0.0.1:8000/api/posts/${this.currentId}/`, {
          title: this.currentTitle,
          description: this.currentDescription
        });
        if(response.status === 200) {
          console.log('Post updated:', response);
          // Hide the edit form
          this.isPostEditFormVisible = false;
          // Refresh the posts list after update
          this.fetchPosts();
        }
      } catch (error) {
        console.error('Error updating post:', error);
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /* .card-title {
    background-color: #d0d0d0;
    /* color: ; */
    /* border-radius: 4px;
  } */
  .modal-backdrop {
    opacity: 0.8;
    z-index: 1000;
  }
  .modal-content {
    /* background: white; */
    z-index: 1000;
  }
</style>
