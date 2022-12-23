<template>
    <div>
        <h2 class="text-left font-bold text-lg">Brand</h2>
        <apexchart type="bar" height="500" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>
  
<script>
export default {
    mounted() {
        // next tick to make sure the chart is rendered
        this.$nextTick(() => {
            this.getSeries()
        })
    },
    watch: {
        appareils: {
            handler: function (newVal, oldVal) {
                this.getSeries()
            },
            deep: true
        }
    },
    components: {
    },
    props: {
        appareils: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            series: [{
                name: 'Count',
                data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380]
            }],
            chartOptions: {
                chart: {
                    type: 'bar',
                    height: 350
                },
                colors: ['#3ABFF8', '#37CDBE', '#570DF8'],
                plotOptions: {
                    bar: {
                        borderRadius: 4,
                        horizontal: true,
                    }
                },
                dataLabels: {
                    enabled: false
                },
                xaxis: {
                    categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan',
                        'United States', 'China', 'Germany'
                    ],
                }
            },
        }
    },
    methods: {
        getSeries() {
            let categories = {}
            this.appareils.forEach(appareil => {
                if (categories[appareil.Marque]) {
                    categories[appareil.Marque] += 1
                } else {
                    categories[appareil.Marque] = 1
                }
            })

            // Keep only the 10 most apparat categories and put the rest in "Other"
            if (Object.keys(categories).length > 10) {
                let other = 0
                let sortedCategories = Object.keys(categories).sort((a, b) => categories[b] - categories[a])
                for (let i = 10; i < sortedCategories.length; i++) {
                    other += categories[sortedCategories[i]]
                    delete categories[sortedCategories[i]]
                }
                categories["Other"] = other
            }


            // Sort categories by apparat count
            let sortedCategories = Object.keys(categories).sort((a, b) => categories[b] - categories[a])

            // Put "Other" at the end
            if (sortedCategories[sortedCategories.length - 1] != "Other") {
                let otherIndex = sortedCategories.indexOf("Other")
                sortedCategories.splice(otherIndex, 1)
                sortedCategories.push("Other")
            }

            // Create series
            let data = []
            let xaxis = []
            sortedCategories.forEach(category => {
                data.push(categories[category])
                xaxis.push(category)
            })

            this.series = [{
                data: data
            }]

            this.chartOptions = {
                ...this.chartOptions,
                xaxis: {
                    categories: xaxis
                }
            }
        }
    }
}
</script>
  
<style scoped>

</style>