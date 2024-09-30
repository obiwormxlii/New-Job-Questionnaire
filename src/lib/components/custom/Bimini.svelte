<script lang="ts">
	import RadioGroupItem from '$lib/components/ui/radio-group/radio-group-item.svelte';
	import RadioGroup from '$lib/components/ui/radio-group/radio-group.svelte';
	import Checkbox from '$lib/components/ui/checkbox/checkbox.svelte';
	import Label from '$lib/components/ui/label/label.svelte';
	import * as Card from '$lib/components/ui/card/index';
	import Textarea from '$lib/components/ui/textarea/textarea.svelte';

	import type { BiminiOptions } from '$lib/types';

	let { biminiOptions = $bindable() }: { biminiOptions: BiminiOptions } = $props();
</script>

<Card.Root>
	<Card.Header class="text-2xl">Bimini</Card.Header>
	<Card.Content class="space-y-4">
		<div class="flex gap-4 border p-4">
			<h4>Pockets</h4>
			<RadioGroup bind:value={biminiOptions.pocket.shape}>
				<div class="flex items-center space-x-2">
					<RadioGroupItem value="fitted" id="fitted" />
					<Label for="fitted">fitted</Label>
				</div>
				<div class="flex items-center space-x-2">
					<RadioGroupItem value="straight" id="straight" />
					<Label for="straight">Straight</Label>
				</div>
			</RadioGroup>
			<div class="flex items-center space-x-2">
				<Checkbox name="pocketCutouts" bind:checked={biminiOptions.pocket.cutouts} />
				<Label for="pocketCutouts">Cutouts</Label>
			</div>
		</div>

		<div class="flex gap-4 border p-4">
			<h3>Main</h3>
			<div class="flex items-center space-x-2">
				<Checkbox name="sailWindow" bind:checked={biminiOptions.main.window} />
				<Label for="pocketCutouts">Sail Window</Label>
			</div>
			<div class="flex items-center space-x-2">
				<Checkbox name="cutouts" bind:checked={biminiOptions.main.stayCutout} />
				<Label for="pocketCutouts">Stay Cutouts</Label>
			</div>
		</div>

		<Textarea bind:value={biminiOptions.notes} placeholder="Notes" />
	</Card.Content>
</Card.Root>
