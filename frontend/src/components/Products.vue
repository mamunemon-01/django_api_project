<template>
  <!-- Product list container -->
  <div class="container d-flex flex-column">
    <!-- Product list Header -->
    <h1 class="mb-4 fw-bold">Product List</h1>
    <!-- Product table container -->
    <div class="ProductList d-flex justify-content-center align-items-center mb-2">
      <table class="table table-bordered rounded-2">
        <thead>
          <!-- Table header -->
          <tr class="border border-bottom">
            <td>Sl No.</td>
            <td>Name</td>
            <td>Price</td>
            <td>Quantity</td>
            <td>Actions</td>
          </tr>
        </thead>
        <tbody>
          <!-- table body -->
          <tr v-for="(product, index) in this.products" :key="product.id">
            <td>{{ offset + index + 1 }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.quantity }}</td>
            <td>
              <div class="d-flex justify-content-center align-items-center m-1">
                <button class="btn btn-secondary p-1 me-2" @click="editProduct(product.id)">Edit</button>
                <button class="btn btn-danger p-1" @click="deleteProduct(product.id)">Delete</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="d-flex justify-content-between align-items-center mb-1">
      <button class="btn btn-primary fw-bold" @click="fetchPreviousProducts"><i class="bi bi-arrow-left"></i></button>
      <select class="form-select mx-2 w-auto" v-model="limit">
        <option>5</option>
        <option>10</option>
        <option>20</option>
        <option>50</option>
        <option>100</option>
      </select>
      <button class="btn btn-primary fw-bold" @click="fetchNextProducts"><i class="bi bi-arrow-right"></i></button>
    </div>
    <div class="d-flex justify-content-end align-items-center mt-1 mb-5">
      <button class="btn btn-primary fw-bold" @click="$router.push({ name: 'ProductDetails', params: {id: null} })">Add Product</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TheProducts',
  props: {
    msg: String
  },
  data() {
    return {
      products: [],
      previousPagination: null,
      nextPagination: null,
      limit: 10,
      offset: 0,
      count: 0
    }
  },
  mounted() {
    this.fetchProducts();
  },
  watch: {
    limit() {
      this.fetchProducts();
    }
  },
  methods: {
    async fetchProducts(url = `http://localhost:8000/api/products/?limit=${this.limit}&offset=${this.offset}`) {
      try {
        const response = await axios.get(url);
        this.products = response.data.results;
        this.previousPagination = response.data.previous;
        this.nextPagination = response.data.next;
        this.count = response.data.count;
      } catch(error) {
        console.error("Error fetching products: ", error);
      }
    },
    fetchPreviousProducts() {
      if(this.previousPagination){
        this.fetchProducts(this.previousPagination);
        this.offset = parseInt(new URL(this.previousPagination).searchParams.get('offset')) || 0;
      }
    },
    fetchNextProducts() {
      if(this.nextPagination){
        this.fetchProducts(this.nextPagination);
        this.offset = parseInt(new URL(this.nextPagination).searchParams.get('offset')) || 0;
      }
    },
    async editProduct(productId) {
      // Implement product editing logic here
      console.log("Edit product with ID:", productId);
      // Navigate to the retrieve product page
      this.$router.push({ name: 'ProductDetails', params: { id: productId } });
    },
    async deleteProduct(productId) {
      try{
        const response = await axios.delete(`http://localhost:8000/api/products/${productId}/`);
        console.log("Delete response: ", response);
        if(response.status === 204) {
          this.fetchProducts();
          console.log("Product deleted successfully.");
        }
      } catch(error) {
        console.error("Error deleting product: ", error);
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>