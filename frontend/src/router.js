import Vue from 'vue'
import Router from 'vue-router'
import NewsFeed from './components/NewsFeed.vue'
import Products from './components/Products.vue'
import ProductDetails from './components/ProductDetails.vue'
import LogIn from './components/LogIn.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        { path: '/login', name: 'LogIn', component: LogIn },
        { path: '/posts', name: 'Posts', component: NewsFeed },
        { path: '/products', name: 'Products',component: Products },
        { path: '/products/:id', name: 'ProductDetails', component: ProductDetails },
        { path: '/', redirect: '/posts' }
    ]
})