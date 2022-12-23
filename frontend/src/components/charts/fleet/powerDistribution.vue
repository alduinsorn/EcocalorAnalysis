<template>
    <div>
        <h2 class="text-left font-bold text-lg">Power</h2>
        <apexchart type="bar" :options="chartOptions" :series="series" width="100%" height="400" />
    </div>
</template>
  
<script>
export default {
    mounted() {
        // next tick to make sure the chart is rendered
        this.$nextTick(() => {
            this.series = this.getSeries()
        })
    },
    watch: {
        appareils: {
            handler: function (newVal, oldVal) {
                this.series = this.getSeries()
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
        },
        minPower: {
            type: Number,
            required: true
        },
        maxPower: {
            type: Number,
            required: true
        },
    },
    data() {
        return {
            chartOptions: {
                chart: {
                    id: "power-distribution-chart",
                },
                xaxis: {
                    categories: ["5-20kW", "21-50kW", "51-100kW", "101-200kW", "201-300kW", "301-500kW", "501-1000kW", "+1000kW"],
                },
                colors: ['#3ABFF8', '#37CDBE', '#570DF8'],
            },

            series: [
                {
                    name: "Count",
                    data: [30, 40, 45, 50, 49, 60, 70, 91]
                }
            ]
        }
    },
    methods: {
        getSeries() {
            let data = []
            let categories = [20, 50, 100, 200, 300, 500, 1000]
            for (let i = 0; i < categories.length; i++) {
                if (i == 0) {
                    data.push(this.appareils.filter(appareil => appareil.KW <= categories[i]).length)
                } else {
                    data.push(this.appareils.filter(appareil => appareil.KW > categories[i - 1] && appareil.KW <= categories[i]).length)
                }
            }
            data.push(this.appareils.filter(appareil => appareil.KW > categories[categories.length - 1]).length)

            return [{
                name: "Count",
                data: data
            }]
        }
    }
}
</script>
  
<style scoped>

</style>