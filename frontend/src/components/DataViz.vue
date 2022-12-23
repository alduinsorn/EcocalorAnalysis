<template>
    <div class="flex h-full flex-col">
        <div class="navbar bg-base-100">
            <div class="flex-1">
                <a class="btn btn-ghost normal-case text-xl">
                    <img src="/analysis.svg" class="h-8 mr-2" alt="Vite logo" />
                    EcocalorAnalysis
                </a>
            </div>
            <div class="flex-none">
                <div class="flex-none">
                    <ul class="menu menu-horizontal p-0">
                        <li @click="changeView('fleet')" :class="{ 'font-bold': isCurrentView('fleet') }">
                            <a>Heating systems fleet analysis</a>
                        </li>
                        <li @click="changeView('interventions')"
                            :class="{ 'font-bold': isCurrentView('interventions') }">
                            <a>Intervention history analysis</a>
                        </li>
                    </ul>
                </div>
                <button class="btn btn-square btn-ghost">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        class="inline-block w-5 h-5 stroke-current">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z">
                        </path>
                    </svg>
                </button>
            </div>
        </div>
        <Interventions v-if="isCurrentView('interventions')" />
        <Fleet v-if="isCurrentView('fleet')" />
        <Turnover v-if="isCurrentView('turnover')" />
    </div>
</template>

<script>
import Interventions from './Interventions.vue'
import Fleet from './Fleet.vue'
import Turnover from './Turnover.vue'

export default {
    components: {
        Interventions,
        Fleet,
        Turnover
    },
    data() {
        return {
            view: "fleet"
        }
    },
    methods: {
        isCurrentView(view) {
            return this.view == view
        },
        changeView(view) {
            console.log("changeView", view)
            this.view = view
        },
    }
}
</script>

<style scoped>

</style>