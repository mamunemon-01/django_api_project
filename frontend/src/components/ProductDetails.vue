<template>
  <div class="container">
    <h1 v-if="id" class="mb-4 fw-bold">Edit Product</h1>
    <h1 v-else class="mb-4 fw-bold">Add Product</h1>
    <div class="ProductDetails">
      <label for="productName" class="d-flex text-start">Name:</label>
      <input id="productName" v-model="productName"/>
      <label for="productPrice" class="d-flex text-start mt-3">Price:</label>
      <input id="productPrice" type="number" step="0.01" v-model="productPrice"/>
      <label for="productQuantity" class="d-flex text-start mt-3">Quantity:</label>
      <input id="productQuantity" type="number" v-model="productQuantity"/>
    </div>
    <div class="d-flex justify-content-end align-items-center mt-4">
      <button class="btn btn-secondary fw-bold me-2" @click="$router.push({ name: 'Products' })">Cancel</button>
      <button v-if="id" class="btn btn-primary fw-bold" @click="updateProduct(id)">Update Product</button>
      <button v-else class="btn btn-primary fw-bold" @click="createProduct">Add Product</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProductDetails',
  props: {
    id: Number
  },
  data() {
    return {
      productName: null,
      productPrice: null,
      productQuantity: null,
    }
  },
  mounted() {
    console.log("Product ID: ", this.id);
    if(this.id){
      this.fetchProductDetails(this.id);
    }
  },
  methods: {
    async createProduct() {
      try {
        const newProduct = {
          name: this.productName,
          price: this.productPrice,
          quantity: this.productQuantity
        };
        const response = await axios.post('http://localhost:8000/api/products/', newProduct);
        if(response.status === 201){
          console.log(`Product created successfully: ${newProduct}`)
          // Navigate to the product list page
          this.$router.push({ name: 'Products' });
        }
      } catch(error) {
        console.error("Error creating product: ", error);
      }
    },
    async fetchProductDetails(productId) {
      try {
        const response = await axios.get(`http://localhost:8000/api/products/${productId}/`);
        const product = response.data;
        console.log("Fethched product details: ", product);
        this.productName = product.name;
        this.productPrice = product.price;
        this.productQuantity = product.quantity;
      } catch(error) {
        console.error("Error fetching product details: ", error);
      }
    },
    async updateProduct(productId) {
      try {
        const updatedProduct = {
          name: this.productName,
          price: this.productPrice,
          quantity: this.productQuantity
        };
        const response = await axios.put(`http://localhost:8000/api/products/${productId}/`, updatedProduct);
        if(response.status === 200) {
          console.log(`Product updated successfully: ${updatedProduct}`);
        }
      } catch(error) {
        console.error("Error updating product: ", error);
      }
      // Navigate to the product list page
      this.$router.push({ name: 'Products' });
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