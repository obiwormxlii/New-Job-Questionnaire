<script lang="ts">
	import Checkbox from '$lib/components/ui/checkbox/checkbox.svelte';
	import Label from '$lib/components/ui/label/label.svelte';
	import * as Select from '$lib/components/ui/select';
	import * as Card from '$lib/components/ui/card/index';
	import Textarea from '$lib/components/ui/textarea/textarea.svelte';
	import * as Collapsible from '$lib/components/ui/collapsible';

	import type { WindowOptions } from '$lib/types';
	import { on } from 'svelte/events';

	let { index, windowOptions = $bindable() }: { index: number; windowOptions: WindowOptions } =
		$props();

	const attachmentTypes = [
		{ value: 'zipper', label: 'Zipper' },
		{ value: 'keder', label: 'Keder' },
		{ value: 'zipperKeder', label: 'Zipper Keder' },
		{ value: 'zipperKederVelcro', label: 'Zipper Keder Velcro' },
		{ value: 'snaps', label: 'Snaps' },
		{ value: 'lift-the-dot', label: 'Lift the Dot' },
		{ value: 'common-sense', label: 'Common Sense' },
		{ value: 'none', label: 'None' }
	];

	const windowStyles = [
		{ value: 'standard', label: 'Standard' },
		{ value: 'long-canvas-bottom', label: 'Long Canvas Bottom' },
		{ value: 'long-clear-bottom', label: 'Long Clear Bottom' },
		{ value: 'straight-venturi', label: 'Straight Venturi' },
		{ value: 'curved-venturi', label: 'Curved Venturi' }
	];

	const sideStyles = [
		{ value: 'butted', label: 'Butted Together' },
		{ value: 'rain-flap', label: 'Rain Flap' },
		{ value: 'tapered', label: 'Tapered' },
		{ value: 'scalloped', label: 'Scalloped' }
	];

	const glassTypes = [
		{ value: 'strataglass', label: 'Strataglass' },
		{ value: 'polycarbonate', label: 'Polycarbonate' }
	];
</script>

<Card.Root>
	<Collapsible.Root>
		<Collapsible.Trigger>
			<Card.Header class="p-4 text-2xl">
				Window Panel {index + 1}
			</Card.Header>
		</Collapsible.Trigger>

		<Collapsible.Content class="space-y-4">
			<Card.Content class="space-y-4">
				<div>
					<Label>Window Style</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.windowStyle = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Window Style" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each windowStyles as windowStyle}
									<Select.Item value={windowStyle.value}>{windowStyle.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				</div>

				<div>
					<Label>Glass Type</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.glassType = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Glass Type" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each glassTypes as glassType}
									<Select.Item value={glassType.value}>{glassType.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				</div>

				<div>
					<Label>Top Attachment</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.attachmentType.top = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Top Attachment" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each attachmentTypes as attachmentType}
									<Select.Item value={attachmentType.value}>{attachmentType.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				</div>

				<div>
					<Label>Bottom Attachment</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.attachmentType.bottom = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Bottom Attachment" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each attachmentTypes as attachmentType}
									<Select.Item value={attachmentType.value}>{attachmentType.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				</div>

				<div>
					<Label>Left Style</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.sideStyle.left = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Left Style" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each sideStyles as sideStyle}
									<Select.Item value={sideStyle.value}>{sideStyle.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				</div>

				{#if windowOptions.sideStyle.left === 'butted' || windowOptions.sideStyle.left === 'rain-flap'}
					<Label>Left Attachment</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.attachmentType.leftSide = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Left Attachment" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each attachmentTypes as attachmentType}
									<Select.Item value={attachmentType.value}>{attachmentType.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				{/if}

				<div>
					<Label>Right Style</Label>
					<Select.Root
						onSelectedChange={(v) => {
							windowOptions.sideStyle.right = v.value;
						}}
					>
						<Select.Trigger>
							<Select.Value placeholder="Right Style" />
						</Select.Trigger>
						<Select.Content>
							<Select.Group>
								{#each sideStyles as sideStyle}
									<Select.Item value={sideStyle.value}>{sideStyle.label}</Select.Item>
								{/each}
							</Select.Group>
						</Select.Content>
					</Select.Root>
				</div>

				{#if windowOptions.sideStyle.right === 'butted' || windowOptions.sideStyle.right === 'rain-flap'}
					<div>
						<Label>Right Attachment</Label>
						<Select.Root
							onSelectedChange={(v) => {
								windowOptions.attachmentType.rightSide = v.value;
							}}
						>
							<Select.Trigger>
								<Select.Value placeholder="Right Attachment" />
							</Select.Trigger>
							<Select.Content>
								<Select.Group>
									{#each attachmentTypes as attachmentType}
										<Select.Item value={attachmentType.value}>{attachmentType.label}</Select.Item>
									{/each}
								</Select.Group>
							</Select.Content>
						</Select.Root>
					</div>
				{/if}

				<div class="flex justify-between">
					<div class="flex items-center space-x-2">
						<Checkbox
							id="smile"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.smiles = v;
								}
							}}
						/>
						<Label
							id="smile-label"
							for="smile"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Smiles
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="vents"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.vents = v;
								}
							}}
						/>
						<Label
							id="vents-label"
							for="vents"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Vents
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="burnStrips"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.burnStrips = v;
								}
							}}
						/>
						<Label
							id="burnStrips-label"
							for="burnStrips"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Burn Strips
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="cutouts"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.cutouts = v;
								}
							}}
						/>
						<Label
							id="cutouts-label"
							for="cutouts"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Cutouts
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="cinch"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.cinchStraps = v;
								}
							}}
						/>
						<Label
							id="cinch-label"
							for="cinch"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Cinch Straps
						</Label>
					</div>
					<div class="flex items-center space-x-2">
						<Checkbox
							id="vents"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.vents = v;
								}
							}}
						/>
						<Label
							id="vents-label"
							for="vents"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Vents
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="burnStrips"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.burnStrips = v;
								}
							}}
						/>
						<Label
							id="burnStrips-label"
							for="burnStrips"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Burn Strips
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="cutouts"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.cutouts = v;
								}
							}}
						/>
						<Label
							id="cutouts-label"
							for="cutouts"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Cutouts
						</Label>
					</div>

					<div class="flex items-center space-x-2">
						<Checkbox
							id="cinch"
							onCheckedChange={(v) => {
								if (v !== 'indeterminate') {
									windowOptions.features.cinchStraps = v;
								}
							}}
						/>
						<Label
							id="cinch-label"
							for="cinch"
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
						>
							Cinch Straps
						</Label>
					</div>
				</div>

				<Textarea bind:value={windowOptions.notes} placeholder="Notes" />
			</Card.Content>
		</Collapsible.Content>
	</Collapsible.Root>
</Card.Root>
