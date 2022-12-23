<template>
    <div>
        <h2 class="text-left font-bold text-lg">Fuel type</h2>
        <apexchart type="donut" height="350" :options="chartOptions" :series="series"></apexchart>
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
    },
    data() {
        return {
            series: [76, 67, 61, 1200],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'radialBar',
                },
                plotOptions: {
                    radialBar: {
                        offsetY: 0,
                        startAngle: 0,
                        endAngle: 270,
                        hollow: {
                            margin: 0,
                            size: '50%',
                            background: 'transparent',
                            image: undefined,
                        },
                        dataLabels: {
                            name: {
                                show: false,
                            },
                            value: {
                                show: false,
                            }
                        }
                    }
                },
                colors: ['#3ABFF8', '#37CDBE', '#570DF8'],
                labels: ['Oil', 'Gas', 'Other'],
                legend: {
                    show: true,
                    floating: false,
                    fontSize: '16px',
                    position: 'left',
                    labels: {
                        useSeriesColors: true,
                    },
                    markers: {
                        size: 0
                    },
                    formatter: function (seriesName, opts) {
                        return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
                    },
                    itemMargin: {
                        vertical: 3
                    }
                },
                responsive: [{
                    breakpoint: 480,
                    options: {
                        legend: {
                            show: false
                        }
                    }
                }]
            },
        }
    },
    methods: {
        getSeries() {
            return [
                this.appareils.filter(appareil => ["Mazout", "MAZOUT", "HEL"].includes(appareil.Combustible)).length,
                this.appareils.filter(appareil => ["Gaz", "Propane", "Gaz ", "Gaz atmo"].includes(appareil.Combustible)).length,
                this.appareils.filter(appareil => !["Mazout", "MAZOUT", "HEL", "Gaz", "Propane", "Gaz ", "Gaz atmo"].includes(appareil.Combustible)).length,
            ]
        }
    }
}
</script>
  
<style scoped>

</style>