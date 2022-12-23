import { createStore } from 'vuex'

// Backend API URL
const API_URL = 'http://localhost:5000'

function timeToMinutes(time) {
  // Add leading 0 if needed
  if (time.length === 3) {
    time = '0' + time
  }

  const hours = parseInt(time.slice(0, 2));
  const minutes = parseInt(time.slice(2));
  return hours * 60 + minutes;
}

export default createStore({
  state: {
    loading: 1,
    installations: [],
    appareils: [],
    contrats: [],
    rapports: [],
    interventions: [],
    prestations: [],
    fournitures: [],
  },
  mutations: {
    setLoading(state, count) {
      state.loading = count
    },
    fetchInstallations(state) {
      // Get all installations addresses
      fetch(`${API_URL}/installations`)
        .then(response => response.json())
        .then(data => {
          state.installations = data
          state.installations.map(installation => {
            const [lat, lng] = installation.GPS.split(';')
            installation.GPS = {
              lat: parseFloat(lat),
              lng: parseFloat(lng)
            }
          })

          // Get all appareils
          fetch(`${API_URL}/appareils`)
            .then(response => response.json())
            .then(data => {
              // For each appareil add it to the installation
              data.forEach(appareil => {
                const installation = state.installations.find(installation => installation.IDAdrInstal === appareil.IDAdrInstal)
                if (installation) {
                  if (!installation.appareils) {
                    installation.appareils = []
                  }

                  // Remove dateMES if before 1900
                  // Convert dateMES to int
                  let dateMES = parseInt(appareil.DateMES)
                  if (dateMES < 19000101) {
                    appareil.DateMES = null
                  }

                  // Add appareil to the installation
                  installation.appareils.push(appareil)
                }
              })
            })
          state.loading--
        })
    },
    fetchContracts(state) {
      // Get all contracts
      fetch(`${API_URL}/contrats`)
        .then(response => response.json())
        .then(data => {
          state.contrats = data
          state.loading--
        })
    },
    fetchRapports(state) {
      // Get all interventions
      fetch(`${API_URL}/rapports`)
        .then(response => response.json())
        .then(data => {
          state.rapports = data
          state.loading--
        })
    },
    fetchInterventions(state) {
      // Get all interventions
      fetch(`${API_URL}/interventions`)
        .then(response => response.json())
        .then(data => {
          state.interventions = data

          // For each intervention transform HeureArrivee and HeureDepart to duration
          state.interventions.forEach(intervention => {
            let heureArrivee = timeToMinutes(intervention.HeureArrivee.toString())
            let heureDepart = timeToMinutes(intervention.HeureDepart.toString())

            intervention.Duration = heureDepart - heureArrivee
          })

          state.loading--
        })
    },
    fetchPrestations(state) {
      // Get all prestations
      fetch(`${API_URL}/prestations`)
        .then(response => response.json())
        .then(data => {
          state.prestations = data
          state.loading--
        })
    },
    fetchFournitures(state) {
      // Get all fournitures
      fetch(`${API_URL}/fournitures`)
        .then(response => response.json())
        .then(data => {
          state.fournitures = data
          state.loading--
        })
    }
  },
  getters: {
    getAllInstallations: state => {
      return state.installations
    },
    getAllContracts: state => {
      return state.contrats.filter(contrat => contrat.Actif === 1)
    },
    getAllRapports: state => {
      return state.rapports
    },
    getAllInterventions: state => {
      return state.interventions
    },
    getAllPrestations: state => {
      return state.prestations
    },
    getAllFournitures: state => {
      return state.fournitures
    }
  },
  actions: {
  }
})
