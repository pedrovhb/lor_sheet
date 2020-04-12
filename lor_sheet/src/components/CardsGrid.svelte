<script>
    import {regions, cards, burstFastOnly, enabledCards} from '../store'
    import Card from "./Card.svelte";

    let visibleCards = [];

    $: visibleCards = $cards.filter(
            card => {
                // Remove non-burst/fast cards if that's not toggled
                if ($burstFastOnly && !["Fast", "Burst"].includes(card.speed)) {
                    return false;
                }

                // Remove cards whose name isn't in the enabled cards list
                if (!$enabledCards.split("\n").includes(card.name)) {
                    return false;
                }

                // Return false if the card's region isn't enabled
                return $regions[card.regionRef].enabled
            }
    );
</script>

<div class="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6 w-5/6 m-auto">
    {#each visibleCards as card}
        <Card card={card} />
    {/each}
</div>