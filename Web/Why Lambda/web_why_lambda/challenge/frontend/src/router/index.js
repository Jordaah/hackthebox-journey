import { createRouter, createWebHistory } from 'vue-router'
import Index from '../views/Index.vue'
import TryModel from '../views/TryModel.vue'
import Dashboard from '../views/Dashboard.vue'

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
    meta: { title: 'Lambda Space Corp. - Index' }
  },
  {
    path: '/try',
    name: 'Try model',
    component: TryModel,
    meta: { title: 'Lambda Space Corp. - Try out our model' }
  },
  {
    path: '/dashboard',
    name: 'Alien dashboard',
    component: Dashboard,
    meta: { title: 'Lambda Space Corp. - Alien dashboard' }
  },
]
const router = createRouter({
  history: createWebHistory("/"),
  routes
})
router.beforeEach((to, from, next) => {
  const title = to.meta.title
  if (title) {
    document.title = title
  }
  next()
})
export default router