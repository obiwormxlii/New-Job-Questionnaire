<script lang="ts">
	let {} = $props();
</script>

<div class="mainItem">
	<h2>Bimini</h2>
	<h5>Fore</h5>
	<div style="padding: 16px; border: 1px solid gray;">
		<h4>Fore Pocket</h4>
		<div>
			<input type="radio" name="forePocket" id="fitted" checked />
			<label for="fitted">fitted</label>
			<input type="radio" name="forePocket" id="straight" />
			<label for="fitted">Straight</label>
		</div>
		<input type="checkbox" name="forePocketCutouts" />
		<label for="fitted">Cutouts</label>
	</div>

	<div style="padding: 16px; border: 1px solid gray;">
		<h3>Main</h3>
		<input type="checkbox" name="mainWindow" />
		<label for="mainWindow">Window</label>
		<input type="checkbox" name="mainStayCutout" />
		<label for="mainStayCutout">Stay Cutout</label>
	</div>

	<div style="padding: 16px; border: 1px solid gray;">
		<h4>Aft Pocket</h4>
		<div>
			<input type="radio" name="aftPocket" id="fitted" checked />
			<label for="fitted">fitted</label>
			<input type="radio" name="aftPocket" id="straight" />
			<label for="fitted">Straight</label>
		</div>
		<input type="checkbox" name="aftPocketCutouts" />
		<label for="fitted">Cutouts</label>
	</div>
	<h5>Aft</h5>
</div>
