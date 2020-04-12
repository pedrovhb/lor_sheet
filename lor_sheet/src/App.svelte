<script>
    import OpponentSelector from './components/OpponentSelector.svelte';
    import CardsGrid from "./components/CardsGrid.svelte";
    import CardPicker from "./components/CardPicker.svelte";
    import Footer from "./components/Footer.svelte";

</script>

<main>
    <div class="opacity-25"></div>
    <OpponentSelector/>
	<CardsGrid/>
    <CardPicker />
    <Footer />
</main>
