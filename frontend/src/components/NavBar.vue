<template>
    <nav class="d-flex flex-column shadow position-sticky top-0 bg-info text-light min-vh-100 w-auto">
        <div class="container-fluid mt-3">
            <!-- <router-link to="/posts" class="navbar-brand"><h1 class="fw-bold">HeadBook</h1></router-link> -->
            <!-- <div class="navbar-nav"> -->
                <router-link to="/posts" class="nav-link text-light fw-bold">Posts</router-link>
                <router-link to="/products" class="nav-link text-light fw-bold">Products</router-link>
                <!-- <h3 id="user-name" class="mx-4 text-light fw-bold border rounded-pill p-1">@{{ username }}</h3>
                <div class="ms-auto pe-2 py-1">
                    <button class="btn btn-light fw-bold" @click="$emit('logout')">Log Out</button>
                </div> -->
            <!-- </div> -->
        </div>
    </nav>
</template>

<script>
export default {
    name: 'NavBar',
    props: {
        username: String
    },
}
</script>

<style scoped>
    nav {
        width: 150px;
    }
</style>