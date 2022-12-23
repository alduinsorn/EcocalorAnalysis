<template>
    <!-- Installation infos modal -->
    <input type="checkbox" id="my-modal-4" class="modal-toggle" />
    <label for="my-modal-4" class="modal cursor-pointer">
        <label class="modal-box relative text-left" for="">
            <h3 class="text-xl font-bold mb-2">{{ selectedInstallation.address }}</h3>
            <h4 class="text-lg font-semibold">Devices</h4>
            <div class="divider my-0"></div>
            <div v-for="appareil in selectedInstallation.appareils" :key="appareil.id" class="flex flex-col">
                <div class="flex flex-row flex-nowrap items-center gap-2">
                    <div class="tooltip tooltip-right" data-tip="Active contract on this device">
                        <svg v-if="appareil.activeContrat" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M10.125 2.25h-4.5c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125v-9M10.125 2.25h.375a9 9 0 019 9v.375M10.125 2.25A3.375 3.375 0 0113.5 5.625v1.5c0 .621.504 1.125 1.125 1.125h1.5a3.375 3.375 0 013.375 3.375M9 15l2.25 2.25L15 12" />
                        </svg>
                    </div>
                    <p>{{ appareil.typeAppareil }}
                        à {{ appareil.combustible }}
                        <span class="font-semibold">{{ appareil.marque }} {{ appareil.modele }}</span> <span v-if="appareil.kw != 0">
                            de {{ appareil.kw }}kW</span>
                        
                        <span v-if="isDateMSEValid(appareil.dateMES)"><br>Put in service on {{ appareil.dateMES
                            }}</span>
                        <br>
                        </p>
                        </div>
                        <div class="divider my-0"></div>
                        </div>
                        </label>
                        </label>
                        <div class="flex flex-row gap-8 max-h-[95%]">
                            <!-- Map -->
                            <div class="w-4/6 max-h-full">
                                <GMapMap :center="{ lat: 46.2814, lng: 6.1432 }" :zoom="11" :options="options" class="h-full"
                                    style="border-radius: 1rem;" ref="map">
                                    <GMapCluster :minimumClusterSize="10" :renderer="renderCluster">
                                        <GMapMarker v-for="marker in markers" :key="marker.id" :position="marker.position" :clickable="true"
                                            @click="displayInstallInfos(marker.id)" />
                                    </GMapCluster>
                                    </GMapMap>
                                    </div>
                                    <div class="w-2/6 overflow-y-auto pr-6">
                                        <div class="collapse collapse-plus border border-base-300 bg-base-100 rounded-box">
                                            <input type="checkbox" />
                                            <div class="collapse-title text-lg font-semibold text-left">
                                                Filters <span v-if="appliedFilters.length > 0">({{ appliedFilters.length }})</span>
                                            </div>
                                            <div class="collapse-content mx-auto">
                                                <h2 class="text-left font-bold mb-1">Installation year</h2>
                                                <div class="w-full items-center">
                                                    <HistogramSlider :width="400" :bar-height="100" :data="data_slider_year" :prettify="prettify_year"
                                                        :drag-interval="true" :resettable="true" :force-edges="false" :colors="['#37CDBE', '#3ABFF8']"
                                                        :min="getMinInstallationsDate()" :max="2022" v-if="data_slider_year" @finish="installationsYearChanged" ref="histYear"/>
                                                </div>
                                                <h2 class="text-left font-bold mt-4">Fuel type</h2>
                                                <div class="flex flex-wrap gap-4 items-center">
                                                    <label class="label cursor-pointer gap-2 px-0">
                                                        <span class="label-text">Gasoil</span>
                                                        <input type="checkbox" v-model="filters.fuelType.gasoil" class="checkbox checkbox-sm" />
                                                    </label>
                                                    <label class="label cursor-pointer gap-2 px-0">
                                                        <span class="label-text">Gas</span>
                                                        <input type="checkbox" v-model="filters.fuelType.gas" class="checkbox checkbox-sm" />
                                                    </label>
                                                    <label class="label cursor-pointer gap-2 px-0">
                                                        <span class="label-text">Other</span>
                                                        <input type="checkbox" v-model="filters.fuelType.other" class="checkbox checkbox-sm" />
                                                    </label>
                                                    </div>
                                                    <h2 class="text-left font-bold mt-4 mb-2">Power</h2>
                                                    <div class="mx-6">
                                                        <HistogramSlider :width="400" :bar-height="100" :data="data_slider_power" :prettify="prettify_power"
                                                            :drag-interval="true" :resettable="true" :force-edges="false" :colors="['#37CDBE', '#3ABFF8']" :min="getMinPower()"
                                                            :max="1000" v-if="data_slider_power" @finish="installationsPowerChanged" ref="histPower"/>
                                                        </div>
                                                        <h2 class="text-left font-bold mt-4">Contract</h2>
                                                        <div class="flex flex-wrap gap-4 items-center">
                                                            <label class="label cursor-pointer gap-2 px-0">
                                                                <span class="label-text">Only device with active contract</span>
                                                                <input type="checkbox" v-model="filters.onlyWithContract" class="checkbox checkbox-sm" />
                                                            </label>
                                                        </div>
                                                        </div>
                                                        </div>
                                                        <!-- Filter badges -->
                                                        <div class="flex mt-2 gap-2">
                                                            <div class="badge gap-2 font-semibold badge-lg text-xs" v-for="filter in appliedFilters">
                                                                {{ filter.value }}
                                                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                                                    class="inline-block w-4 h-4 stroke-current hover:scale-125" @click="removeFilter(filter)">
                                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12">
                                                                    </path>
                                                                </svg>
                                                            </div>
                                                        </div>
                                                        <!-- Charts -->
                                                        <div v-if="appareils.length > 0">
                                                            <div class="flex mt-4 gap-4">
                                                                <div class="bg-accent text-white rounded-box flex items-center p-4 shadow-xl w-full">
                                                                    <div class="flex-1 px-2">
                                                                        <p class="text-3xl font-extrabold">{{ appareils.length }}</p>
                                                                        <h2 class="text-sm text-opacity-80">Heating systems operated</h2>
                                                                    </div>
                                                                </div>
                                                                <div class="bg-primary text-white rounded-box flex items-center p-4 shadow-xl w-full">
                                                                    <div class="flex-1 px-2">
                                                                        <h2 class="text-3xl font-extrabold">{{ getNumberOfActiveContracts() }}</h2>
                                                                        <p class="text-sm text-opacity-80">under maintenance contract</p>
                                                                    </div>
                                                                </div>
                                                                <div class="bg-info text-white rounded-box flex items-center p-4 shadow-xl w-full">
                                                                    <div class="flex-1 px-2">
                                                                        <p class="text-3xl font-extrabold">{{ installations.length }}</p>
                                                                        <h2 class="text-sm text-opacity-80">Installation sites</h2>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class="mt-6">
                                                                <BrandDistributionChart :appareils="appareils" />
                                                            </div>
                                                            <div class="mt-6">
                                                                <PowerDistributionChart :appareils="appareils" :minPower="filters.power[0]" :maxPower="filters_origin.power[1]" />
                                                                </div>
                                                                <div class="mt-6">
                                                                    <FuelDistributionChart :appareils="appareils" :minPower="filters.power[0]" :maxPower="filters_origin.power[1]" />
                                                                </div>
                                                                </div>
                                                                <div v-else class="h-[40rem] mt-8">
                                                                    <h2 class="text-center text-2xl font-bold">No data available</h2>
                                                                    <!-- Reset filters button -->
                                                                    <div class="flex justify-center mt-4">
                                                                        <button class="btn btn-primary" @click="resetFilters()">Reset filters</button>
                                                                    </div>
                                                                </div>
                                                                </div>
    </div>
</template>
  
<script>
import mapStyle from '../assets/map-style.json'

import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

import Slider from '@vueform/slider'
import '@vueform/slider/themes/default.css';

import PowerDistributionChart from '../components/charts/fleet/powerDistribution.vue'
import FuelDistributionChart from '../components/charts/fleet/fuelDistribution.vue'
import BrandDistributionChart from './charts/fleet/brandDistribution.vue';

import * as d3 from 'd3';

export default {
    components: {
        Datepicker,
        Slider,
        PowerDistributionChart,
        FuelDistributionChart,
        BrandDistributionChart
    },
    mounted() {
        this.installations = Object.assign([], this.$store.getters.getAllInstallations)
        this.contracts = Object.assign([], this.$store.getters.getAllContracts)
        this.statistics = this.getInstallationsStatistics()
        this.initFilters()

        this.$nextTick(() => {
            this.data_slider_year = this.appareils.map(appareil => {
                if (appareil.DateMES) {
                    let dateMES = appareil.DateMES.toString()
                    return dateMES.substring(0, 4)
                }
            })

            this.data_slider_power = this.appareils.map(appareil => {
                if (appareil.KW) {
                    if (appareil.KW >= 1000) {
                        return 1000
                    }
                    return appareil.KW
                }
            })
        })
    },
    watch: {
        filters: {
            handler: function () {
                this.applyFilters()
            },
            deep: true
        },
        installations: {
            handler: function () {
                this.$nextTick(() => {
                    console.log('Installations changed', this.installations.length)
                    this.markers = this.getInstallationsPosition()
                    this.getAppareilsFromInstallations()
                    console.log("Appareils after updating installations: " + this.appareils.length)
                })
            },
            deep: true
        },
    },
    data() {
        return {
            installations: [],
            selectedInstallation: {},
            appareils: [],
            markers: [],
            contracts: [],
            statistics: {},
            options: {
                streetViewControl: false,
                styles: mapStyle
            },
            filters_origin: {
                startDate: new Date(),
                endDate: new Date(),
                fuelType: {
                    gasoil: true,
                    gas: true,
                    other: true
                },
                power: [20, 40],
                onlyWithContract: false
            },
            filters: {
                startDate: new Date(),
                endDate: new Date(),
                fuelType: {
                    gasoil: true,
                    gas: true,
                    other: true
                },
                power: [20, 40],
                onlyWithContract: false
            },
            appliedFilters: [],
            data_slider_year: null,
            data_slider_power: null,
            prettify_year: function (ts) {
                // Round to nearest year
                return Math.round(ts).toString()
            },
            prettify_power: function (value) {
                if (value >= 1000) {
                    return `> 1 MW`
                }
                return `${parseInt(value)} kW`
            },
            renderCluster: {
                render: ({ count, position }, stats) => {
                    // use d3-interpolateRgb to interpolate between red and blue
                    const color = d3.interpolateRgb("blue", "red")(count / stats.clusters.markers.max);
                    // create svg url with fill color
                    const svg = window.btoa(`
                <svg fill="${color}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240">
                    <circle cx="120" cy="120" opacity=".8" r="70" />    
                </svg>`);

                    let minSize = 45
                    let maxSize = 85

                    let minCount = stats.clusters.markers.min
                    let maxCount = stats.clusters.markers.max

                    let size = (count - minCount) / (maxCount - minCount) * (maxSize - minSize) + minSize

                    // create marker using svg icon
                    return new google.maps.Marker({
                        position,
                        icon: {
                            url: `data:image/svg+xml;base64,${svg}`,
                            scaledSize: new google.maps.Size(size, size),
                        },
                        label: {
                            text: String(count),
                            color: "rgba(255,255,255,0.9)",
                            fontSize: "12px",
                        },
                        // adjust zIndex to be above other markers
                        zIndex: Number(google.maps.Marker.MAX_ZINDEX) + count,
                    });
                }
            }
        }
    },
    methods: {
        initFilters() {
            this.filters_origin.startDate = new Date(this.statistics.minDate)
            this.filters_origin.power = [this.statistics.minPower, this.statistics.maxPower]
            this.filters = JSON.parse(JSON.stringify(this.filters_origin))
            this.filters.startDate = new Date(this.filters_origin.startDate)
            this.filters.endDate = new Date(this.filters_origin.endDate)
        },
        resetFilters() {
            this.filters = JSON.parse(JSON.stringify(this.filters_origin))
            this.filters.startDate = new Date(this.filters_origin.startDate)
            this.filters.endDate = new Date(this.filters_origin.endDate)
            this.$refs.histPower.update({ from: this.filters.power[0], to: this.filters.power[1] })
            this.$refs.histYear.update({ from: this.filters.startDate.getFullYear(), to: this.filters.endDate.getFullYear() })
        },
        applyFilters() {
            // Check if filters have changed
            console.log('applyFilters', this.appliedFilters.length)

            // Date
            if (this.filters.startDate.getTime() !== this.filters_origin.startDate.getTime()
                || this.filters.endDate.getTime() !== this.filters_origin.endDate.getTime()) {
                if (this.appliedFilters.find(f => f.type === 'date')) {
                    this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'date')
                }
                this.appliedFilters.push({
                    type: 'date',
                    value: `Installation year: ${new Date(this.filters.startDate).getFullYear()} - ${new Date(this.filters.endDate).getFullYear()}`
                })
            } else {
                this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'date')
            }

            // Fuel type
            if (this.filters.fuelType.gasoil !== this.filters_origin.fuelType.gasoil
                || this.filters.fuelType.gas !== this.filters_origin.fuelType.gas
                || this.filters.fuelType.other !== this.filters_origin.fuelType.other) {
                if (this.appliedFilters.find(f => f.type === 'fuelType')) {
                    this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'fuelType')
                }
                this.appliedFilters.push({
                    type: 'fuelType',
                    value: `Fuel type: ${this.filters.fuelType.gasoil ? 'Gasoil' : ''} ${this.filters.fuelType.gas ? 'Gas' : ''} ${this.filters.fuelType.other ? 'Other' : ''}`
                })
            } else {
                this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'fuelType')
            }

            // Power
            if (this.filters.power[0] !== this.filters_origin.power[0]
                || this.filters.power[1] !== this.filters_origin.power[1]) {
                if (this.appliedFilters.find(f => f.type === 'power')) {
                    this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'power')
                }
                if (this.filters.power[1] === 1000) {
                    this.appliedFilters.push({
                        type: 'power',
                        value: `Power: >${this.filters.power[0]} kW`
                    })
                } else {
                    this.appliedFilters.push({
                        type: 'power',
                        value: `Power: ${this.filters.power[0]} - ${this.filters.power[1]} kW`
                    })
                }
            } else {
                this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'power')
            }

            // Only with contract
            if (this.filters.onlyWithContract !== this.filters_origin.onlyWithContract) {
                if (this.appliedFilters.find(f => f.type === 'onlyWithContract')) {
                    this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'onlyWithContract')
                }
                this.appliedFilters.push({
                    type: 'contract',
                    value: `Only with contract`
                })
            } else {
                this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'onlyWithContract')
            }

            this.installations = JSON.parse(JSON.stringify(this.$store.getters.getAllInstallations))

            console.log("Installations before filter", this.installations.length)
            console.log("Applied filters", this.appliedFilters)
            //Browse all installations and remove appareils that don't match filters and if no appareils left remove installation
            this.installations = this.installations.map(installation => {
                if (installation.appareils && this.appliedFilters.length > 0) {
                    installation.appareils = installation.appareils.filter(appareil => {
                        // Check if appareil is in date range
                        if (this.appliedFilters.find(f => f.type === 'date')) {
                            if (!appareil.DateMES) {
                                return false
                            }

                            let dateMES = this.convertDateString(appareil.DateMES)
                            if (dateMES.getTime() < this.filters.startDate.getTime() || dateMES.getTime() > this.filters.endDate.getTime()) {
                                return false
                            }
                        }

                        // Check if appareil is in power range
                        if (this.appliedFilters.find(f => f.type === 'power')) {
                            if (appareil.KW < this.filters.power[0] || appareil.KW > this.filters.power[1]) {
                                return false
                            }
                        }

                        // Check if appareil is in fuel type range
                        if (this.appliedFilters.find(f => f.type === 'fuelType')) {
                            if (appareil.Combustible === 'Mazout' || appareil.Combustible === 'MAZOUT' || appareil.Combustible === 'HEL') {
                                if (!this.filters.fuelType.gasoil) {
                                    return false
                                }
                            } else if (appareil.Combustible === 'Gaz' || appareil.Combustible === 'Propane' || appareil.Combustible === 'Gaz ' || appareil.Combustible === 'Gaz atmo') {
                                if (!this.filters.fuelType.gas) {
                                    return false
                                }
                            } else {
                                if (!this.filters.fuelType.other) {
                                    return false
                                }
                            }
                        }

                        // Check if appareil has contract
                        if (this.appliedFilters.find(f => f.type === 'contract')) {
                            // Check if appareil has contract by searching in contracts
                            if (!this.contracts.find(contract => contract.IDAppareil === appareil.IDAppareil)) {
                                return false
                            }
                        }

                        return true
                    })
                }
                return installation
            }).filter(installation => installation.appareils?.length > 0)

            console.log("Installations after filter", this.installations.length)
        },
        removeFilter(filter) {
            this.appliedFilters = this.appliedFilters.filter(f => f !== filter)
            switch (filter.type) {
                case 'date':
                    this.filters.startDate = this.filters_origin.startDate
                    this.filters.endDate = this.filters_origin.endDate
                    this.$refs.histYear.update({ from: this.filters.startDate.getFullYear(), to: this.filters.endDate.getFullYear() })
                    break;
                case 'fuelType':
                    this.filters.fuelType = JSON.parse(JSON.stringify(this.filters_origin.fuelType))
                    break;
                case 'power':
                    this.filters.power = JSON.parse(JSON.stringify(this.filters_origin.power))
                    this.$refs.histPower.update({ from: this.filters.power[0], to: this.filters.power[1] })
                    break;
                case 'contract':
                    this.filters.onlyWithContract = this.filters_origin.onlyWithContract
                    break;
                default:
                    break;
            }
        },
        installationsYearChanged(val) {
            this.filters.startDate = new Date(val.from, 0, 1)
            this.filters.endDate = new Date(val.to, 11, 31)
        },
        installationsPowerChanged(val) {
            console.log(val)
            this.filters.power = [Math.round(val.from), Math.round(val.to)]
        },
        getInstallationsPosition() {
            if (!this.installations) {
                return []
            }
            return this.installations
                .filter(installation => installation.appareils?.length > 0)
                .map(installation => {
                    return {
                        id: installation.IDAdrInstal,
                        position: {
                            lat: installation.GPS.lat,
                            lng: installation.GPS.lng,
                        }
                    }
                })
        },
        getInstallationsStatistics() {
            let minDate = new Date()
            let minPower = 1000
            let maxPower = 0
            this.installations.forEach(installation => {
                installation.appareils?.forEach(appareil => {
                    // Find min date
                    if (appareil.DateMES) {
                        const year = appareil.DateMES.substring(0, 4);
                        const month = appareil.DateMES.substring(4, 6);
                        const day = appareil.DateMES.substring(6, 8);
                        const dateAppareil = new Date(year, month - 1, day);
                        if (dateAppareil < minDate) {
                            minDate = dateAppareil
                        }
                    }

                    // Find min and max power
                    if (appareil.KW) {
                        if (appareil.KW < minPower) {
                            minPower = appareil.KW
                        }
                        if (appareil.KW > maxPower && appareil.KW < 10000) {
                            maxPower = appareil.KW
                        }
                    }

                })
            })

            return {
                minDate,
                minPower,
                maxPower
            }
        },
        getMinInstallationsDate() {
            return this.statistics.minDate ? this.statistics.minDate.getFullYear() : 1900
        },
        getMinPower() {
            return this.statistics.minPower ? this.statistics.minPower : 0
        },
        getAppareilsFromInstallations() {
            this.appareils = this.installations.map(installation => installation.appareils).flat()
        },
        displayInstallInfos(installationID) {
            const installation = this.installations.find(installation => installation.IDAdrInstal === installationID)

            let address = installation.CodeAdr + ' ' + installation.NumRue1 + (installation.NumRue2 ? '-' + installation.NumRue2 : '') + (installation.ExtNoRue.trim() ? installation.ExtNoRue : '') + ', ' + installation.CodeCommune
            let appareils = installation.appareils?.map(appareil => {
                return {
                    marque: appareil.Marque,
                    modele: appareil.Modele,
                    dateMES: this.convertDateString(appareil.DateMES).getFullYear(),
                    kw: appareil.KW,
                    combustible: appareil.Combustible.toLowerCase(),
                    dateIntervention: this.convertDateString(appareil.DateInterrvention),
                    typeAppareil: this.getTypesAppareils()[appareil.TypeAppareil],
                    activeContrat: this.contracts.find(contract => contract.IDAppareil === appareil.IDAppareil)?.Actif,
                }
            })
            this.selectedInstallation = {
                address,
                appareils
            }

            // Center and zoom on installation
            this.$refs.map.$mapObject.setCenter(installation.GPS)
            this.$refs.map.$mapObject.setZoom(17)

            document.getElementById('my-modal-4').checked = true;
        },
        getTypesAppareils() {
            return {
                1: 'Chaudière',
                2: 'Brûleur',
                3: 'Pompe à chaleur',
            }
        },
        getNumberOfActiveContracts() {
            return this.contracts
                .filter(contract => {
                    // Check if contract.IDAppareil is in appareils
                    return this.appareils.find(appareil => appareil.IDAppareil === contract.IDAppareil)
                }).length
        },
        convertDateString(dateString) {
            dateString = dateString.toString()
            const year = dateString.substring(0, 4);
            const month = dateString.substring(4, 6);
            const day = dateString.substring(6, 8);
            return new Date(year, month - 1, day);
        },
        isDateMSEValid(DateMES) {
            if (DateMES) {
                if (DateMES > 1899) {
                    return true
                }
            }
            return false
        }
    },
}
</script>
  
<style scoped>

</style>