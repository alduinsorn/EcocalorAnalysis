<template>
    <div class="bg-info text-white rounded-box flex items-center p-4 shadow-xl w-full">
        <div class="flex-1 px-2">

            <p class="text-sm text-opacity-80">An average of </p>
            <svg class="animate-spin h-8 w-8 text-white mx-auto mt-2" xmlns="http://www.w3.org/2000/svg" fill="none"
                viewBox="0 0 24 24" v-if="!averageInterventionPerDay">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor"
                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                </path>
            </svg>
            <h2 class="text-3xl font-extrabold" v-else>{{ averageInterventionPerDay }}</h2>
            <p class="text-sm text-opacity-80">Interventions per working day</p>
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
    },
    watch: {
        interventions() {
            this.averageInterventionPerDay = this.getAverageInterventionPerWorkingDay()
        }
    },
    data() {
        return {
            averageInterventionPerDay: ""
        }
    },
    methods: {
        getAverageInterventionPerWorkingDay() {
            // Compute the number of days between the first and the last intervention
            // Find the first intervention by searching the intervention with the lowest date

            let firstIntervention = this.interventions[0]
            let lastIntervention = this.interventions[0]
            this.interventions.forEach(intervention => {
                if (intervention.Date < firstIntervention.Date) {
                    firstIntervention = intervention
                }

                if (intervention.Date > lastIntervention.Date) {
                    lastIntervention = intervention
                }
            })

            firstIntervention.Date = firstIntervention.Date.toString()
            lastIntervention.Date = lastIntervention.Date.toString()

            // Transform the date (20190101) to a Date object
            let firstDate = new Date(firstIntervention.Date.substring(0, 4), firstIntervention.Date.substring(4, 6) - 1, firstIntervention.Date.substring(6, 8))
            let lastDate = new Date(lastIntervention.Date.substring(0, 4), lastIntervention.Date.substring(4, 6) - 1, lastIntervention.Date.substring(6, 8))

            // Compute the number of days between the first and the last intervention
            let diffTime = Math.abs(lastDate.getTime() - firstDate.getTime())
            let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))

            // Remove all Saturday and Sunday from the number of days
            let numberOfWeekendDays = 0
            for (let i = 0; i < diffDays; i++) {
                let date = new Date(firstDate.getTime() + i * 24 * 60 * 60 * 1000)
                if (date.getDay() == 0 || date.getDay() == 6) {
                    numberOfWeekendDays++
                }
            }
            diffDays -= numberOfWeekendDays

            return (this.interventions.length / diffDays).toFixed(2).toString()
        },
    }
}
</script>
  
<style scoped>

</style>