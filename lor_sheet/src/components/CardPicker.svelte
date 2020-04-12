<script>
    import {enabledCards} from '../store'
</script>

<div class="w-3/4 m-auto flex justify-center h-64 p-3 shadow my-6">
    <textarea bind:value={$enabledCards} class="w-1/3 mx-4 "></textarea>
    <div class="w-2/3 mx-4 text-center flex flex-col justify-around rounded ">
        <p>Click the filters above to select your opponent's region and to toggle showing only quick+burst spells.</p>
        <p>Use the text field on the left to enable or disable cards from being shown.</p>
        <p>Cards will only be enabled if their exact name is matched, so you can add a "#" to exclude them.</p>
    </div>
</div>
