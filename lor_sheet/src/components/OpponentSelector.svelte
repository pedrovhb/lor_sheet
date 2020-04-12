<script>
    import OpponentSelectorFaction from './OpponentSelectorRegion.svelte';
    import {regions, burstFastOnly} from '../store'
</script>

<div class="flex justify-center my-6">
    {#each Object.keys($regions) as region}
        <OpponentSelectorFaction regionName={region}/>
    {/each}
    <img src="img/regions/icon-burstfast.png"
         on:click={() => $burstFastOnly = !$burstFastOnly}
         class:opacity-25={!$burstFastOnly}>
</div>
