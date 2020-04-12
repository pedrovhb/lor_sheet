<script>
    import {regions} from '../store'

    export let regionName;
    let region = $regions[regionName];

</script>

<img src={`img/regions/${region.iconPath}`}
     on:click={() => $regions[regionName].enabled = !$regions[regionName].enabled}
     class:opacity-25={!$regions[regionName].enabled}>

