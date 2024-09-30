<script lang="ts">
	import * as Select from '$lib/components/ui/select';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import Label from '../ui/label/label.svelte';
	import Button from '../ui/button/button.svelte';

	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let selectedItem: string = $state('');

	const addItemCallback = (item: string) => {
		dispatch('addItem', { item });
	};
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger asChild let:builder>
		<Button builders={[builder]} class="font-bold">Add New Project Item</Button>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content>
		<DropdownMenu.Item on:click={() => addItemCallback('bimini')}>Bimini</DropdownMenu.Item>
		<DropdownMenu.Item on:click={() => addItemCallback('windowPanel')}
			>Window Panel</DropdownMenu.Item
		>
	</DropdownMenu.Content>
</DropdownMenu.Root>
