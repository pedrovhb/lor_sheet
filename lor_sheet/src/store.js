import {writable} from 'svelte/store'
import {cards as baseCards, regions as baseRegions} from "./card_data/processed_data.json"
import naughtyCards from "./card_data/naughty_cards.json"

function getRegionsMap() {
    Object.values(baseRegions).forEach(region => region.enabled = false);
    return baseRegions;
}

function getManaSortedCards() {
    return baseCards.sort((a, b) => a.cost > b.cost ? 1 : -1);
}

function getEnabledCardsInitialInput() {
    let nameSortedCards = baseCards.sort((a, b) => a.name > b.name ? 1 : -1);
    let enabledCards = "";
    nameSortedCards.forEach((card) => {
        naughtyCards.includes(card.name)
            ? enabledCards = enabledCards.concat(card.name + "\n")
            : enabledCards = enabledCards.concat("#" + card.name + "\n")
    });
    return enabledCards;
}

export const regions = writable(getRegionsMap());

export const enabledCards = writable(getEnabledCardsInitialInput());

export const cards = writable(getManaSortedCards());

export const burstFastOnly = writable(false);