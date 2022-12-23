<template>
    <div class="mt-6">
        <h2 class="text-left font-bold text-lg mb-2">Interventions over the time</h2>
        <apexchart type="heatmap" height="350" :options="chartOptions" :series="series" width="100%" />
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
            series: [{
                name: 'Maintenance',
                data: this.generateData(20, {
                    min: 0,
                    max: 12
                })
            },
            {
                name: 'Troubleshooting',
                data: this.generateData(20, {
                    min: 0,
                    max: 15
                })
            }
            ],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'heatmap',
                },
                plotOptions: {
                    heatmap: {
                        shadeIntensity: 0.5,
                        radius: 0,
                        useFillColorAsStroke: true,
                        colorScale: {
                            ranges: [{
                                from: 8,
                                to: 20,
                                name: 'Very good',
                                color: '#00A100'
                            },
                            {
                                from: 6,
                                to: 8,
                                name: 'Good',
                                color: '#128FD9'
                            },
                            {
                                from: 3,
                                to: 5,
                                name: 'Bad',
                                color: '#FFB200'
                            },
                            {
                                from: 0,
                                to: 2,
                                name: 'Very bad',
                                color: '#FF0000'
                            }
                            ]
                        }
                    }
                },
                dataLabels: {
                    enabled: false,
                    fontSize: '16px',
                },
                stroke: {
                    width: 1
                },
            },
        }
    },
    methods: {
        generateData(count, yrange) {
            var i = 0;
            var series = [];

            const start = new Date(2019, 0, 1); // January 1, 2019
            const end = new Date(2020, 8, 1); // September 1, 2020

            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

            let date = start;
            while (i < count) {
                const month = months[date.getMonth()];
                const year = date.getFullYear();
                var x = `${month} ${year}`;
                date.setMonth(date.getMonth() + 1);

                var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

                series.push({
                    x: x,
                    y: y
                });
                i++;
            }
            return series;
        },
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