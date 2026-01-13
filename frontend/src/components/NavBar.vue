<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
            <router-link to="/posts" class="navbar-brand"><h1 class="fw-bold">HeadBook</h1></router-link>
            <div class="navbar-nav">
                <router-link to="/posts" class="nav-link text-light fw-bold">Posts</router-link>
                <router-link to="/products" class="nav-link text-light fw-bold ms-3">Products</router-link>
                <h3 id="user-name" class="mx-4 text-light fw-bold border rounded-5 p-1">@{{ username }}</h3>
                <div class="ms-auto pe-2 py-1">
                    <button class="btn btn-light fw-bold" @click="$emit('logout')">Log Out</button>
                </div>
            </div>
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