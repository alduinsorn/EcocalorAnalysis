<template>
  <Home v-if="isHome" @toggleView="toggleView" />
  <DataViz v-else @toggleView="toggleView" />
</template>

<script>
import { useStore } from "vuex";
import { onMounted } from "vue";

import Home from './components/Home.vue'
import DataViz from './components/DataViz.vue'

export default {
  setup() {
    const store = useStore();
    onMounted(() => {
      store.commit("setLoading", 6)
      store.commit("fetchInstallations")
      store.commit("fetchContracts")
      store.commit("fetchRapports")
      store.commit("fetchInterventions")
      store.commit("fetchPrestations")
      store.commit("fetchFournitures")
    });
  },
  components: {
    Home,
    DataViz
  },
  data() {
    return {
      isHome: true,
    }
  },
  methods: {
    toggleView() {
      this.isHome = !this.isHome
    }
  }
}
</script>

<style scoped>
.logo {
  height: 8em;
    padding: 0;
  will-change: filter;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>