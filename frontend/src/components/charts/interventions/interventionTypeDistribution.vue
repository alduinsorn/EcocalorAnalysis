<template>
    <div>
        <h2 class="text-left font-bold text-lg mb-4">Intervention type</h2>
        <apexchart type="donut" height="280" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>
  
<script>
export default {
    mounted() {
        this.$nextTick(() => {
            this.series = this.getSeries()
        })
    },
    watch: {
        rapports: {
            handler: function () {
                this.series = this.getSeries()
            },
            deep: true
        }
    },
    props: {
        rapports: {
            type: Array,
            required: true
        },
    },
    data() {
        return {
            series: [76, 67],
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
                labels: ['Maintenance', 'Troubleshooting'],
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
            if (this.rapports) {
                return [
                    this.rapports.filter(rapport => rapport.InterventionType === 'Maintenance').length,
                    this.rapports.filter(rapport => rapport.InterventionType === 'Troubleshooting').length
                ]
            } else {
                return [45, 12]
            }
        }
    }
}
</script>
  
<style scoped>

</style>