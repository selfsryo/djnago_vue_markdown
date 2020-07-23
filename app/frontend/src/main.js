import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.prototype.$http = (url, init) => fetch(url, init)
Vue.prototype.$getPosts = 'http://127.0.0.1:8000/api/posts/'


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
