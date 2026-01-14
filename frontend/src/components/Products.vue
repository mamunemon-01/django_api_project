<template>
  <div class="container">
    <h1 class="mb-4 fw-bold">Product List</h1>
    <div class="ProductList mb-2">
      <table class="table table-bordered rounded-2">
        <thead>
          <tr class="border border-bottom">
            <td>Sl No.</td>
            <td>Name</td>
            <td>Price</td>
            <td>Quantity</td>
            <td>Actions</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(product, index) in this.products" :key="product.id">
            <td>{{ index + 1 }}</td>
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
    <div class="d-flex justify-content-end align-items-center">
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
      products: []
    }
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://localhost:8000/api/products/');
        this.products = response.data;
      } catch(error) {
        console.error("Error fetching products: ", error);
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
  .container {
    max-width: 420px;
  }
</style>