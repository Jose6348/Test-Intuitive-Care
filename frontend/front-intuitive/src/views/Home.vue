<template>
  <div class="home">
    <div class="hero" :class="{ 'with-search': showSearch }">
      <div class="hero-content">
        <h1>Consulta de Operadoras de Saúde</h1>
        <p>Encontre informações detalhadas sobre operadoras de planos de saúde registradas na ANS</p>
        <button @click="showSearch = true" class="cta-button" v-if="!showSearch">
          <i class="fas fa-search"></i>
          Realizar consulta de operadoras
        </button>
      </div>
    </div>

    <div class="container" v-if="showSearch">
      <SearchOperators />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import SearchOperators from '@/components/SearchOperators.vue'

export default {
  name: 'Home',
  components: {
    SearchOperators
  },
  setup() {
    const showSearch = ref(false)
    return { showSearch }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.home {
  min-height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  background-color: #f8fafc;
  overflow-x: hidden;
  position: relative;
}

.hero {
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  color: white;
  width: 100vw;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  transition: min-height 0.3s ease;
  position: relative;
}

.hero.with-search {
  min-height: 40vh;
}

.hero-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  width: 100%;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.hero p {
  font-size: 1.2rem;
  opacity: 0.9;
  margin-bottom: 2rem;
  line-height: 1.5;
}

.cta-button {
  background: white;
  color: #1e3c72;
  border: none;
  padding: 1rem 2rem;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
  background: #f8fafc;
}

.cta-button i {
  font-size: 1.2rem;
}

.container {
  width: 100vw;
  max-width: 100vw;
  margin: 0;
  padding: 2rem;
  flex: 1;
  display: flex;
  justify-content: center;
}

@media (max-width: 768px) {
  .hero {
    min-height: 60vh;
  }

  .hero.with-search {
    min-height: 30vh;
  }

  .hero-content {
    padding: 1rem;
  }

  .hero h1 {
    font-size: 2rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .cta-button {
    padding: 0.8rem 1.6rem;
    font-size: 1rem;
  }

  .container {
    padding: 1rem;
  }
}
</style> 