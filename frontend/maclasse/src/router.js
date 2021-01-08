import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      alias: "/eleves",
      name: "eleves",
      component: () => import("./components/ElevesList")
    },
    {
      path: "/eleves/:id",
      name: "eleves-details",
      component: () => import("./components/Eleve")
    },
    {
      path: "/add",
      name: "add",
      component: () => import("./components/AddEleve")
    }
  ]
});