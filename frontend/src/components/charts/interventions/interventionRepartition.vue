<template>
    <div>
        <h2 class="text-left font-bold text-lg mb-4">Intervention done by</h2>
        <apexchart type="donut" height="280" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>
  
<script>
export default {
    mounted() {
        // this.$nextTick(() => {
        //     this.series = this.getSeries()
        // })
    },
    watch: {
        appareils: {
            handler: function (newVal, oldVal) {
                // this.series = this.getSeries()
            },
            deep: true
        }
    },
    components: {
    },
    // props: {
    //     appareils: {
    //         type: Array,
    //         required: true
    //     },
    // },
    data() {
        return {
            appareils: [],
            series: [44, 55],
            chartOptions: {
                chart: {
                    type: 'donut',
                },
                colors: ['#3ABFF8', '#37CDBE', '#570DF8'],
                legend: {
                    fontSize: '16px',
                    formatter: function (seriesName, opts) {
                        return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
                    },
                    labels: {
                        useSeriesColors: true,
                    },
                },
                labels: ["John Doe", "Jane Doe"],
                responsive: [{
                    breakpoint: 480,
                    options: {
                        chart: {
                            width: 200
                        },
                        legend: {
                            position: 'bottom'
                        }
                    }
                }]
            },
        }
    },
    methods: {
        getSeries() {
        }
    }
}
</script>
  
<style scoped>

</style>