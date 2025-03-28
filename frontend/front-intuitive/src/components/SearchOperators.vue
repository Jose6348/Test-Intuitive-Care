<template>
  <div class="search-operators">
    <div class="search-container">
      <div class="search-input-wrapper">
        <i class="fas fa-search search-icon"></i>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Digite o nome da operadora, CNPJ, registro ANS ou localização..."
          class="search-input"
          :disabled="loading"
          ref="searchInput"
          @keyup.enter="searchOperators"
        />
        <button
          @click="searchOperators"
          class="search-button"
          :disabled="loading"
          :class="{ 'loading': loading }"
        >
          <i class="fas fa-spinner fa-spin" v-if="loading"></i>
          <span v-else>Buscar</span>
        </button>
      </div>
    </div>

    <div v-if="error" class="error-message">
      <i class="fas fa-exclamation-circle"></i>
      {{ error }}
    </div>

    <div v-if="results.length > 0" class="results-container">
      <div class="results-header">
        <h3>Resultados encontrados</h3>
        <span class="results-count">{{ results.length }} operadora(s)</span>
      </div>

      <div class="results-grid">
        <div v-for="operator in results" :key="operator.registro_ans" class="operator-card">
          <div class="operator-header">
            <h4>{{ operator.nome_fantasia }}</h4>
            <span class="operator-id">Registro ANS: {{ operator.Registro_ANS}}</span>
          </div>
          
          <div class="operator-details">
            <div class="detail-item">
              <i class="fas fa-building"></i>
              <span>{{ operator.Razao_Social }}</span>
            </div>
            <div class="detail-item">
              <i class="fas fa-id-card"></i>
              <span>{{ operator.CNPJ }}</span>
            </div>
            <div class="detail-item">
              <i class="fas fa-hospital"></i>
              <span>{{ operator.Modalidade }}</span>
            </div>
            <div class="detail-item">
              <i class="fas fa-map-marker-alt"></i>
              <span>{{ operator.Cidade }} - {{ operator.UF}}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else-if="!loading && searchQuery && results.length === 0" class="no-results">
      <i class="fas fa-search"></i>
      <p>Nenhuma operadora encontrada para "{{ searchQuery }}"</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'SearchOperators',
  setup() {
    const searchQuery = ref('')
    const results = ref([])
    const loading = ref(false)
    const error = ref(null)
    const searchInput = ref(null)

    const searchOperators = async () => {
      if (!searchQuery.value.trim()) {
        results.value = []
        return
      }

      loading.value = true
      error.value = null

      try {
        const response = await axios.get(`http://127.0.0.1:8001/api/search?query=${encodeURIComponent(searchQuery.value)}`)
        results.value = response.data
      } catch (err) {
        error.value = 'Erro ao buscar operadoras. Por favor, tente novamente.'
        console.error('Erro na busca:', err)
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      if (searchInput.value) {
        searchInput.value.focus()
      }
    })

    return {
      searchQuery,
      results,
      loading,
      error,
      searchOperators,
      searchInput
    }
  }
}
</script>

<style scoped>
.search-operators {
  width: 100vw;
  max-width: 1200px;
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin: 0 auto;
  min-height: calc(60vh - 4rem);
  display: flex;
  flex-direction: column;
}

.search-container {
  width: 100%;
  margin-bottom: 2rem;
}

.search-input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1rem;
  background: white;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  padding: 0.75rem;
  transition: all 0.3s ease;
  width: 100%;
}

.search-input-wrapper:focus-within {
  border-color: #1e3c72;
  box-shadow: 0 0 0 3px rgba(30, 60, 114, 0.1);
}

.search-icon {
  color: #64748b;
  font-size: 1.2rem;
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 1rem;
  padding: 0;
  background: transparent;
  min-width: 0;
  width: 100%;
}

.search-input::placeholder {
  color: #94a3b8;
}

.search-button {
  background: #1e3c72;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-shrink: 0;
  min-width: 100px;
  justify-content: center;
  white-space: nowrap;
}

.search-button:hover:not(:disabled) {
  background: #2a5298;
}

.search-button:disabled {
  background: #94a3b8;
  cursor: not-allowed;
}

.error-message {
  background: #fee2e2;
  color: #dc2626;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
}

.results-container {
  margin-top: 2rem;
  width: 100%;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e2e8f0;
  width: 100%;
}

.results-header h3 {
  color: #1e3c72;
  font-size: 1.5rem;
  margin: 0;
  font-weight: 600;
}

.results-count {
  color: #64748b;
  font-size: 0.9rem;
  background: #f1f5f9;
  padding: 0.5rem 1rem;
  border-radius: 999px;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  width: 100%;
  flex: 1;
  overflow-y: auto;
  padding-right: 0.5rem;
  max-height: calc(100vh - 300px);
}

.results-grid::-webkit-scrollbar {
  width: 8px;
}

.results-grid::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 4px;
}

.results-grid::-webkit-scrollbar-thumb {
  background: #94a3b8;
  border-radius: 4px;
}

.results-grid::-webkit-scrollbar-thumb:hover {
  background: #64748b;
}

.operator-card {
  background: #f8fafc;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #e2e8f0;
  width: 100%;
  height: fit-content;
}

.operator-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-color: #1e3c72;
}

.operator-header {
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e2e8f0;
  width: 100%;
}

.operator-header h4 {
  color: #1e3c72;
  margin: 0 0 0.5rem 0;
  font-size: 1.2rem;
  font-weight: 600;
}

.operator-id {
  color: #64748b;
  font-size: 0.9rem;
  background: #f1f5f9;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  display: inline-block;
}

.operator-details {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  width: 100%;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #475569;
  padding: 0.5rem;
  border-radius: 6px;
  transition: background-color 0.2s ease;
  width: 100%;
}

.detail-item:hover {
  background-color: #f1f5f9;
}

.detail-item i {
  color: #1e3c72;
  width: 1.2rem;
  flex-shrink: 0;
}

.detail-item span {
  flex: 1;
  word-break: break-word;
}

.no-results {
  text-align: center;
  padding: 3rem;
  color: #64748b;
  background: #f8fafc;
  border-radius: 12px;
  border: 1px dashed #e2e8f0;
  width: 100%;
  margin-top: 2rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.no-results i {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #94a3b8;
}

@media (max-width: 768px) {
  .search-operators {
    padding: 1rem;
    min-height: calc(70vh - 2rem);
    width: 100vw;
    border-radius: 0;
  }

  .search-input-wrapper {
    padding: 0.5rem;
  }

  .search-button {
    padding: 0.5rem 1rem;
  }

  .results-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
    max-height: calc(100vh - 200px);
  }

  .operator-card {
    padding: 1rem;
  }

  .detail-item {
    padding: 0.25rem;
  }
}
</style> 