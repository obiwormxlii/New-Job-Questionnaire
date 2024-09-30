<script lang="ts">
	import pkg from 'file-saver';
	const { saveAs } = pkg;
	import Input from '$lib/components/ui/input/input.svelte';
	import Label from '$lib/components/ui/label/label.svelte';
	import Button from '$lib/components/ui/button/button.svelte';

	import Bimini from '../../lib/components/custom/Bimini.svelte';
	import WindowPanel from '../../lib/components/custom/WindowPanel.svelte';
	import AddNewProjectItem from '$lib/components/custom/AddNewProjectItem.svelte';
	import type { BiminiOptions, WindowOptions } from '$lib/types';

	let projectItems: {
		CustomerName: string;
		ProjectName: string;
		biminis: BiminiOptions[];
		windowPanels: WindowOptions[];
	} = $state({
		CustomerName: '',
		ProjectName: '',
		biminis: [],
		windowPanels: []
	});

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

	function addWindowPanel() {
		let newWindowPanel: WindowOptions = {
			windowStyle: '',
			glassType: '',
			attachmentType: {
				top: '',
				bottom: '',
				leftSide: '',
				rightSide: ''
			},
			sideStyle: {
				left: '',
				right: ''
			},
			features: {
				smiles: false,
				vents: false,
				burnStrips: false,
				cutouts: false,
				cinchStraps: false
			},
			notes: ''
		};
		projectItems.windowPanels = [...projectItems.windowPanels, newWindowPanel];
	}

	const addItem = (item: string) => {
		switch (item) {
			case 'bimini':
				addBimini();
				break;
			case 'windowPanel':
				addWindowPanel();
				break;

			default:
				break;
		}
	};

	function handleAddItem(event: any) {
		addItem(event.detail.item);
	}

	function submit() {
		let fileName = `${projectItems.CustomerName}_${projectItems.ProjectName}`;
		let json = JSON.stringify(projectItems);
		let blob = new Blob([json], { type: 'application/json' });
		saveAs(blob, fileName + '.json');
	}

	$inspect(projectItems);
</script>

<h1 class="text-4xl font-black">New Project</h1>

<div class="grid grid-cols-1 gap-8">
	<div>
		<Label for="CustomerName">Customer Name</Label>
		<Input type="text" name="CustomerName" bind:value={projectItems.CustomerName} />
	</div>
	<div>
		<Label for="ProjectName">Project Name</Label>
		<Input type="text" name="ProjectName" bind:value={projectItems.ProjectName} />
	</div>
	<div>
		<Label for="ProjectDescription">Project Description</Label>
		<Input type="text" name="ProjectDescription" />
	</div>
	{#each projectItems.biminis as bimini, i}
		<div>
			<Bimini bind:biminiOptions={projectItems.biminis[i]} />
			<Button
				class="w-80 font-bold"
				variant="destructive"
				onclick={() =>
					(projectItems.biminis = projectItems.biminis.filter((_, index) => index !== i))}
				>Clear</Button
			>
		</div>
	{/each}

	{#each projectItems.windowPanels as windowPanel, i}
		<WindowPanel index={i} bind:windowOptions={projectItems.windowPanels[i]} />
		<Button
			class="w-80 font-bold"
			variant="destructive"
			onclick={() =>
				(projectItems.windowPanels = projectItems.windowPanels.filter((_, index) => index !== i))}
			>remove</Button
		>
	{/each}

	<div class="w-96">
		<AddNewProjectItem on:addItem={handleAddItem} />

		<Button
			class="font-bold"
			variant="destructive"
			onclick={() => {
				projectItems = { biminis: [], windowPanels: [] };
			}}>Clear All</Button
		>
	</div>

	<Button class="w-80 text-2xl font-bold" variant="default" onclick={() => submit()}>SUBMIT</Button>
</div>
