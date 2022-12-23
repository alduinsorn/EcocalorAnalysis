<template>
    <div class="flex flex-col justify-center mt-4">
        <img src="/analysis.svg" class="logo" alt="Vite logo" />
        <h1 class="text-3xl font-semibold mb-1">EcocalorAnalysis</h1>
        <div class="flex flex-wrap gap-1 mb-8 mx-auto">
            Made with
            <span>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="w-6 h-6 fill-red-600">
                    <path
                        d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" />
                </svg>
            </span>
            by Thibaut Michaud & Romain Peretti
        </div>
        <div class="flex flex-col max-w-3xl mx-auto mt-8">
            <h2 class="font-bold text-start">Objectives / Intents</h2>
            <p class="text-start">
                Exploit the information collected by the CRM / ERP application over the last 3 years and provide an
                easily
                understandable and usable visual representation to provide relevant statistics on the installation park
                and
                the interventions carried out as well as a visualization to understand where the turnover comes from.
            </p>
            <h2 class="font-bold text-start mt-4">Data sources</h2>
            <p class="text-start">
                Database (SQL) extracted from the database system of the CRM / ERP application of the Ecocalor heating
                company
                (HFSQL)
            </p>
            <h2 class="font-bold text-start mt-4">Project description</h2>
            <p class="text-start">
                The project will be presented in the form of an interactive WEB application that will make available an
                interface allowing to visualize as much information as possible in order to learn more about the
                extension
                possibilities of the company. Several views will be proposed including a geographical view allowing to
                learn
                more about the geographical location of the company.
            </p>
        </div>
        <button class="btn btn-primary gap-2 w-fit mx-auto mt-16" @click="toggleView"
            :class="{'btn-disabled': this.$store.state.loading > 0}">
            <div v-if="this.$store.state.loading > 0" class="flex flex-row items-center gap-2">
                Loading data ...
                <svg class="animate-spin h-8 w-8 text-white mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none"
                    viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor"
                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
                    </path>
                </svg>
            </div>
            <div v-else class="flex flex-row items-center gap-2">
            Go to visualisations
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                stroke="currentColor" class="w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
            </svg>
        </div>
        </button>
    </div>
</template>

<script>
export default {
    name: "Home",
    methods: {
        toggleView() {
            this.$emit('toggleView')
        }
    }
}
</script>

<style scoped>
.logo {
    height: 8em;
    padding: 0;
    will-change: filter;
}

.logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
}
</style>