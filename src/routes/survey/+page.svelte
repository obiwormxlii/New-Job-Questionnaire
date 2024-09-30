<script lang="ts">
	import Input from '$lib/components/ui/input/input.svelte';
	import Label from '$lib/components/ui/label/label.svelte';

	import Bimini from '../../lib/components/custom/Bimini.svelte';
	import AddNewProjectItem from '$lib/components/custom/AddNewProjectItem.svelte';
	import type { BiminiOptions } from '$lib/types';

	let projectItems: { biminis: BiminiOptions[] } = $state({ biminis: [] });

	function addBimini() {
		let newBimini: BiminiOptions = {
			pocket: {
				shape: 'straight',
				cutouts: false
			},
			main: {
				window: false,
				stayCutout: false
			},
			notes: ''
		};
		projectItems.biminis = [...projectItems.biminis, newBimini];
	}

	const addItem = (item: string) => {
		switch (item) {
			case 'bimini':
				addBimini();
				break;
			case 'windowPanel':
				break;

			default:
				break;
		}
	};

	function handleAddItem(event: any) {
		addItem(event.detail.item);
	}

	$inspect(projectItems);
</script>

<h1>New Project</h1>

<div class="grid grid-cols-1 gap-8">
	<div>
		<Label for="CustomerName">Customer Name</Label>
		<Input type="text" name="CustomerName" />
	</div>
	<div>
		<Label for="ProjectName">Project Name</Label>
		<Input type="text" name="ProjectName" />
	</div>
	<div>
		<Label for="ProjectDescription">Project Description</Label>
		<Input type="text" name="ProjectDescription" />
	</div>
	{#each projectItems.biminis as bimini, i}
		<Bimini bind:biminiOptions={projectItems.biminis[i]} />
	{/each}

	<AddNewProjectItem on:addItem={handleAddItem} />

	<button onclick={() => addItem('bimini')}>Add Bimini</button>
	<button onclick={() => (projectItems.biminis = [])}>Clear All</button>
</div>
