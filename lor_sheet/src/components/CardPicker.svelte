<script>
    import {enabledCards} from '../store'
</script>

<div class="w-3/4 m-auto flex flex-col justify-center p-3 shadow my-6">
    <div class="mx-4 text-center">
        <p class="my-2">Click the filters above to select your opponent's region and to toggle showing only quick+burst spells.</p>
        <p class="my-2">Use the text field below to enable or disable cards from being shown.</p>
        <p class="my-2">Cards will only be enabled if their exact name is matched, so you can add a "#" to exclude them.</p>
    </div>
    <textarea bind:value={$enabledCards} class="mx-4 my-6" cols="50" rows="6"></textarea>
</div>
