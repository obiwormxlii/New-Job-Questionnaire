<script lang="ts">
	let projectItems: [] = $state([]);
	import Section from './Section.svelte';
	let bool = $state(false);
</script>

<h1>New Project</h1>

<form method="POST">
	<label for="CustomerName">Customer Name</label>
	<input type="text" name="CustomerName" />

	<label for="ProjectName">Project Name</label>
	<input type="text" name="ProjectName" />

	<label for="ProjectDescription">Project Description</label>
	<input type="text" name="ProjectDescription" />

	<button type="submit">Submit</button>
</form>
{#if bool}
	<Section />
{/if}
<button onclick={() => (bool = !bool)}>Toggle</button>

<style>
	.mainItem {
		padding: 16px;
		border: 1px solid gray;
		display: flex;
		flex-direction: column;
		gap: 4px;
	}
</style>
