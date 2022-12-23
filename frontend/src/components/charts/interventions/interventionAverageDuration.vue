<template>
    <div class="bg-accent text-white rounded-box flex items-center p-4 shadow-xl w-full">
        <div class="flex-1 px-2">
            <p class="text-sm text-opacity-80">Average intervention duration</p>
            <svg class="animate-spin h-8 w-8 text-white mx-auto mt-2" xmlns="http://www.w3.org/2000/svg" fill="none"
                viewBox="0 0 24 24" v-if="!averageDuration">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                </path>
            </svg>
            <h2 class="text-3xl font-extrabold">{{ averageDuration }}</h2>
        </div>
    </div>
</template>
  
<script>

export default {
    props: {
        interventions: {
            type: Array,
            required: true
        },
        rapports: {
            type: Array,
            required: true
        }
    },
    watch: {
        interventions() {
            this.averageDuration = this.getAverageInterventionDuration()
        },
        rapports() {
            this.averageDuration = this.getAverageInterventionDuration()
        }
    },
    data() {
        return {
            averageDuration: ""
        }
    },
    methods: {
        getAverageInterventionDuration() {
            if (!this.interventions || !this.rapports) {
                return ""
            }

            // this.$worker.run((interventionsJSON, rapportsJSON) => {
            //     console.log("interventionsJSON", interventionsJSON)
            //     let interventions = JSON.parse(interventionsJSON)
            //     let rapports = JSON.parse(rapportsJSON)

            //     let mergedInterventions = []
            //     interventions.forEach(intervention => {
            //         let rapport = rapports.find(rapport => rapport.IDRapTravail === intervention.IDRapport)
            //         if (!rapport) {
            //             return
            //         }
            //         let mergedIntervention = mergedInterventions.find(mergedIntervention => mergedIntervention.IDRapport === rapport.IDRapTravail)
            //         if (mergedIntervention) {
            //             mergedIntervention.Duration += intervention.Duration
            //         } else {
            //             mergedInterventions.push({
            //                 IDRapport: rapport.IDRapTravail,
            //                 Duration: intervention.Duration
            //             })
            //         }
            //     })
            //     console.log("mergedInterventions", mergedInterventions)

            //     let totalDuration = 0
            //     let totalCount = 0
            //     mergedInterventions.forEach(mergedIntervention => {
            //         // Check is duration is not nan
            //         if (mergedIntervention.Duration) {
            //             totalDuration += mergedIntervention.Duration
            //             totalCount++
            //         }
            //     })
            //     console.log("totalDuration", totalDuration)
            //     console.log("totalCount", totalCount)

            //     let averageDuration = totalDuration / totalCount

            //     // Format duration to HHhMM
            //     let hours = Math.floor(averageDuration / 60)
            //     let minutes = averageDuration % 60

            //     // Add leading 0 if minutes < 10
            //     if (minutes < 10) {
            //         minutes = "0" + minutes
            //     }
            //     // Round minutes
            //     minutes = Math.round(minutes)

            //     return `${hours}h${minutes}min`
            // }, JSON.stringify(this.interventions), JSON.stringify(this.rapports)
            // ).then((result) => {
            //     this.averageDuration = result
            // }).catch((err) => {
            //     console.log(err.message);
            // })
        },
    }
}
</script>
  
<style scoped>

</style>