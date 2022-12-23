<template>
    <div class="flex flex-row gap-8 max-h-[95%]">
        <div class="overflow-y-auto pr-6 w-full">
            <div class="collapse collapse-plus border border-base-300 bg-base-100 rounded-box">
                <input type="checkbox" />
                <div class="collapse-title text-lg font-semibold text-left">
                    Filters <span v-if="appliedFilters.length > 0">({{ appliedFilters.length }})</span>
                </div>
                <div class="collapse-content mx-auto">
                    <div class="z-10">
                        <h2 class="text-left font-bold mb-2">By employee</h2>
                        <Multiselect v-model="filters.employeesValue" :options="employees" :multiple="true" class="multiselect-blue" />
                        </div>
                        <h2 class="text-left font-bold mt-4 mb-1">Select Date</h2>
                        <div class="flex flex-wrap gap-2 items-center mx-12">
                            <HistogramSlider :width="600" :bar-height="200" :data="data_slider" :prettify="prettify" :drag-interval="true"
                                :resettable="true" :force-edges="false" :colors="['#37CDBE', '#3ABFF8']" :min="new Date(2019, 1, 1).valueOf()"
                                :max="new Date().valueOf()" v-if="data_slider" @finish="interventionsDateChanged" ref="hist" />
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
                        <div class="flex flex-row gap-8 mt-8 w-10/12">
                            <div class="flex flex-col gap-4 w-1/3">
                                <div class="bg-primary text-white rounded-box flex items-center p-4 shadow-xl w-full">
                                    <div class="flex-1 px-2">
                                        <svg class="animate-spin h-8 w-8 text-white mx-auto mb-2" xmlns="http://www.w3.org/2000/svg" fill="none"
                                            viewBox="0 0 24 24" v-if="!rapports">
                                            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                            <path class="opacity-75" fill="currentColor"
                                                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                                            </path>
                                        </svg>
                                        <h2 class="text-3xl font-extrabold" v-else>{{ rapports.length }}</h2>
                                        <p class="text-sm text-opacity-80">Interventions operated</p>
                                        </div>
                                        </div>
                                        <InterventionAverageDuration :interventions="interventions" :rapports="rapports" />
                                        <InterventionAverageByWorkingDay :interventions="interventions" />
                                        </div>
                            <div class="w-2/5">
                                <InterventionTypeDistribution :rapports="rapports" />
                </div>
                <div class="w-1/3">
                    <InterventionRepartition :employees="employees"/>
                </div>
            </div>
            <InterventionsOverTime />
        </div>
    </div>
</template>

<script>
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';

import Multiselect from '@vueform/multiselect';
import '@vueform/multiselect/themes/default.css';

import InterventionTypeDistribution from '../components/charts/interventions/interventionTypeDistribution.vue';
import InterventionRepartition from '../components/charts/interventions/interventionRepartition.vue';
import InterventionsOverTime from '../components/charts/interventions/interventionsOverTime.vue';

import InterventionAverageDuration from '../components/charts/interventions/interventionAverageDuration.vue';
import InterventionAverageByWorkingDay from '../components/charts/interventions/interventionAverageByWorkingDay.vue';

export default {
    components: {
        Datepicker,
        Multiselect,
        InterventionTypeDistribution,
        InterventionRepartition,
        InterventionsOverTime,
        InterventionAverageDuration,
        InterventionAverageByWorkingDay
    },
    watch: {
        filters: {
            handler: function () {
                this.applyFilters()
            },
            deep: true
        },
    },
    mounted() {
        console.log("mounted")

        setTimeout(() => {
            this.rapports = Object.assign([], this.$store.state.rapports)
            this.interventions = Object.assign([], this.$store.state.interventions)
            console.log(this.interventions)
            console.log(this.rapports)

            this.$nextTick(() => {
                this.data_slider = this.interventions.map(intervention => {
                    let interventionDate = intervention.Date.toString()
                    return new Date(interventionDate.substring(0, 4), interventionDate.substring(4, 6) - 1, interventionDate.substring(6, 8))
                })
            })
        }, 1000)
    },
    data() {
        return {
            data_slider: null,
            prettify: function (ts) {
                return new Date(ts).toLocaleDateString("en", {
                    year: "numeric",
                    month: "short",
                    day: "numeric"
                });
            },
            rapports: null,
            interventions: [],
            averageDuration: "",
            employees: [
                {
                    label: "All employees",
                    value: 99
                },
                {
                    label: "Employee N°1",
                    value: 3
                },
                {
                    label: "Employee N°2",
                    value: 5
                },
                {
                    label: "Employee N°3",
                    value: 8
                },
                {
                    label: "Employee N°4",
                    value: 9
                },
                {
                    label: "Employee N°5",
                    value: 10
                },
            ],
            filters_origin: {
                startDate: new Date("2019-01-01"),
                endDate: new Date(),
                employeesValue: 99,
            },
            filters: {
                startDate: new Date("2019-01-01"),
                endDate: new Date(),
                employeesValue: 99,
            },
            appliedFilters: [],
        }
    },
    methods: {
        resetFilters() {
            this.filters = Object.assign({}, this.filters_origin)
            this.filters.startDate = new Date(this.filters_origin.startDate)
            this.filters.endDate = new Date(this.filters_origin.endDate)
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
                let startDateString = new Date(this.filters.startDate).toLocaleDateString("en", {
                    year: "numeric",
                    month: "short",
                    day: "numeric"
                });
                let endDateString = new Date(this.filters.endDate).toLocaleDateString("en", {
                    year: "numeric",
                    month: "short",
                    day: "numeric"
                });
                this.appliedFilters.push({
                    type: 'date',
                    value: `Intervention date: ${startDateString} - ${endDateString}`
                })
            } else {
                this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'date')
            }

            // Employee
            console.log('this.filters.employeesValue', this.filters.employeesValue)
            if (this.filters.employeesValue !== this.filters_origin.employeesValue) {
                if (this.appliedFilters.find(f => f.type === 'employee')) {
                    this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'employee')
                }
                this.appliedFilters.push({
                    type: 'employee',
                    value: `Employee: ${this.employees.find(e => e.value === this.filters.employeesValue).label}`
                })
            } else {
                this.appliedFilters = this.appliedFilters.filter(f => f.type !== 'employee')
            }

            this.interventions = Object.assign([], this.$store.state.interventions) 

            console.log("Interventions before filter", this.interventions.length)
            //Browse all installations and remove appareils that don't match filters and if no appareils left remove installation
            // this.installations = this.installations.map(installation => {
            //     if (installation.appareils && this.appliedFilters.length > 0) {
            //         installation.appareils = installation.appareils.filter(appareil => {
            //             // Check if appareil is in date range
            //             if (this.appliedFilters.find(f => f.type === 'date')) {
            //                 if (!appareil.DateMES) {
            //                     return false
            //                 }

            //                 let dateMES = this.convertDateString(appareil.DateMES)
            //                 if (dateMES.getTime() < this.filters.startDate.getTime() || dateMES.getTime() > this.filters.endDate.getTime()) {
            //                     return false
            //                 }
            //             }

            //             // Check if appareil is in power range
            //             if (this.appliedFilters.find(f => f.type === 'power')) {
            //                 if (appareil.KW < this.filters.power[0] || appareil.KW > this.filters.power[1]) {
            //                     return false
            //                 }
            //             }

            //             // Check if appareil is in fuel type range
            //             if (this.appliedFilters.find(f => f.type === 'fuelType')) {
            //                 if (appareil.Combustible === 'Mazout' || appareil.Combustible === 'MAZOUT' || appareil.Combustible === 'HEL') {
            //                     if (!this.filters.fuelType.gasoil) {
            //                         return false
            //                     }
            //                 } else if (appareil.Combustible === 'Gaz' || appareil.Combustible === 'Propane' || appareil.Combustible === 'Gaz ' || appareil.Combustible === 'Gaz atmo') {
            //                     if (!this.filters.fuelType.gas) {
            //                         return false
            //                     }
            //                 } else {
            //                     if (!this.filters.fuelType.other) {
            //                         return false
            //                     }
            //                 }
            //             }

            //             // Check if appareil has contract
            //             if (this.appliedFilters.find(f => f.type === 'contract')) {
            //                 // Check if appareil has contract by searching in contracts
            //                 if (!this.contracts.find(contract => contract.IDAppareil === appareil.IDAppareil)) {
            //                     return false
            //                 }
            //             }

            //             return true
            //         })
            //     }
            //     return installation
            // }).filter(installation => installation.appareils?.length > 0)

            console.log("Interventions after filter", this.interventions.length)
        },
        removeFilter(filter) {
            this.appliedFilters = this.appliedFilters.filter(f => f !== filter)
            switch (filter.type) {
                case 'date':
                    this.filters.startDate = this.filters_origin.startDate
                    this.filters.endDate = this.filters_origin.endDate
                    this.$refs.hist.update({ from: this.filters.startDate, to: this.filters.endDate })
                    break;
                case 'employee':
                    this.filters.employeesValue = this.filters_origin.employeesValue
                    break;
            }
        },
        interventionsDateChanged(val) {
            console.log(val)
            this.filters.startDate = new Date(val.from)
            this.filters.endDate = new Date(val.to)
        },
        // Generate array of random integers between two numbers
        randomIntFromInterval(min, max, count) {
            let arr = [];
            for (let i = 0; i < count; i++) {
                arr.push(Math.floor(Math.random() * (max - min + 1) + min));
            }
            return arr;
        },
    }
}
</script>
  
<style>
.multiselect-blue {
    --ms-font-size: 1rem;
    --ms-line-height: 1.375;
    --ms-bg: #FFFFFF;
    --ms-bg-disabled: #F3F4F6;
    --ms-border-color: #D1D5DB;
    --ms-border-width: 1px;
    --ms-border-color-active: #D1D5DB;
    --ms-border-width-active: 1px;
    --ms-radius: 4px;
    --ms-py: 0.5rem;
    --ms-px: 0.875rem;
    --ms-ring-width: 3px;
    --ms-ring-color: #3ABFF830;
    --ms-placeholder-color: #9CA3AF;
    --ms-max-height: 10rem;

    --ms-spinner-color: #3ABFF8;
    --ms-caret-color: #999999;
    --ms-clear-color: #999999;
    --ms-clear-color-hover: #000000;

    --ms-tag-font-size: 0.875rem;
    --ms-tag-line-height: 1.25rem;
    --ms-tag-font-weight: 600;
    --ms-tag-bg: #3ABFF8;
    --ms-tag-bg-disabled: #9CA3AF;
    --ms-tag-color: #FFFFFF;
    --ms-tag-color-disabled: #FFFFFF;
    --ms-tag-radius: 4px;
    --ms-tag-py: 0.125rem;
    --ms-tag-px: 0.5rem;
    --ms-tag-my: 0.25rem;
    --ms-tag-mx: 0.25rem;

    --ms-tag-remove-radius: 4px;
    --ms-tag-remove-py: 0.25rem;
    --ms-tag-remove-px: 0.25rem;
    --ms-tag-remove-my: 0rem;
    --ms-tag-remove-mx: 0.125rem;

    --ms-dropdown-bg: #FFFFFF;
    --ms-dropdown-border-color: #D1D5DB;
    --ms-dropdown-border-width: 1px;
    --ms-dropdown-radius: 4px;

    --ms-group-label-py: 0.3rem;
    --ms-group-label-px: 0.75rem;
    --ms-group-label-line-height: 1.375;
    --ms-group-label-bg: #E5E7EB;
    --ms-group-label-color: #374151;
    --ms-group-label-bg-pointed: #74d5ff;
    --ms-group-label-color-pointed: #374151;
    --ms-group-label-bg-disabled: #F3F4F6;
    --ms-group-label-color-disabled: #D1D5DB;
    --ms-group-label-bg-selected: #09aff7;
    --ms-group-label-color-selected: #FFFFFF;
    --ms-group-label-bg-selected-pointed: #09aff7;
    --ms-group-label-color-selected-pointed: #FFFFFF;
    --ms-group-label-bg-selected-disabled: #82d9ff;
    --ms-group-label-color-selected-disabled: #b4e8ff;

    --ms-option-font-size: 1rem;
    --ms-option-line-height: 1.375;
    --ms-option-bg-pointed: #94dfff;
    --ms-option-color-pointed: #1F2937;
    --ms-option-bg-selected: #3ABFF8;
    --ms-option-color-selected: #FFFFFF;
    --ms-option-bg-disabled: #FFFFFF;
    --ms-option-color-disabled: #D1D5DB;
    --ms-option-bg-selected-pointed: #82d9ff;
    --ms-option-color-selected-pointed: #FFFFFF;
    --ms-option-bg-selected-disabled: #FFFFFF;
    --ms-option-color-selected-disabled: #b4e8ff;
    --ms-option-py: 0.5rem;
    --ms-option-px: 0.75rem;

    --ms-empty-color: #4B5563;
    }
</style>