<script>
    export let card;
</script>

<picture>
    <source srcset={`img/cards/${card.code}.webp`} type="image/webp">
    <img src={`img/cards/${card.code}.jpg`} />
</picture>