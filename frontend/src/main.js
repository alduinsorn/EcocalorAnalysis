import { createApp } from 'vue'
import store from "./store";
import './style.css'
import App from './App.vue'

import VueGoogleMaps from 'vue-google-maps-community-fork'
import VueApexCharts from "vue3-apexcharts";

import SimpleWebWorker from 'simple-web-worker'

import HistogramSlider from "vue3-histogram-slider";
import "vue3-histogram-slider/dist/histogram-slider.css";

const app = createApp(App)
app.config.globalProperties.$worker = SimpleWebWorker;
app.component(HistogramSlider.name, HistogramSlider);

app.use(store)
    .use(VueGoogleMaps, {
        load: {
            key: 'AIzaSyBJ6NvvVgmiWK9MMijJ7HlQaT3EKpw20dM'
        }
    })
    .use(VueApexCharts)
    .mount('#app')
