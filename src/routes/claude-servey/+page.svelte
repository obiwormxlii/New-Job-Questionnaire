<script lang="ts">

  // Stores
  let selectedProducts: string[] = $state([]);
  let productDetails = $state({});

  // Helper functions
  function addProduct(type: string) {
    selectedProducts = [...selectedProducts, type];
    productDetails ={
      ...productDetails,
      [type]: type === 'enclosure' ? { windowPanels: [] } : {}
    };
  }

  function removeProduct(index: number) {
    selectedProducts =
      const updatedProducts = selectedProducts.filter((_, i) => i !== index);
      productDetails.update(details => {
        const { [selectedProducts[index]]: removed, ...rest } = details;
        return rest;
      });
      return updatedProducts;
  }

  function updateProductDetails(productType, field, value) {
    productDetails.update(details => ({
      ...details,
      [productType]: {
        ...details[productType],
        [field]: value
      }
    }));
  }

  function addWindowPanel(productType) {
    productDetails.update(details => ({
      ...details,
      [productType]: {
        ...details[productType],
        windowPanels: [
          ...details[productType].windowPanels,
          {
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
              cutOuts: false,
              cinchStraps: false
            }
          }
        ]
      }
    }));
  }

  function updateWindowPanel(productType, panelIndex, field, value) {
    productDetails.update(details => {
      const updatedPanels = [...details[productType].windowPanels];
      if (field.includes('.')) {
        const [mainField, subField] = field.split('.');
        updatedPanels[panelIndex] = {
          ...updatedPanels[panelIndex],
          [mainField]: {
            ...updatedPanels[panelIndex][mainField],
            [subField]: value
          }
        };
      } else {
        updatedPanels[panelIndex] = {
          ...updatedPanels[panelIndex],
          [field]: value
        };
      }
      return {
        ...details,
        [productType]: {
          ...details[productType],
          windowPanels: updatedPanels
        }
      };
    });
  }

  function handleSave() {
    const jsonString = JSON.stringify(productDetails, null, 2);
    const blob = new Blob([jsonString], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = 'canvas_project.json';
    link.click();

    URL.revokeObjectURL(url);
  }
</script>

<main>
	<h1>Canvas Product Specification</h1>

	<select onchange={(e) => addProduct(e.target.value)}>
		<option value="">Add a Product</option>
		<option value="bimini">Bimini</option>
		<option value="enclosure">Enclosure</option>
		<option value="sunFly">Sun Fly</option>
		<option value="dodger">Dodger</option>
	</select>

	{#each selectedProducts as productType, index}
		<div class="product-form">
			<h2>{productType.charAt(0).toUpperCase() + productType.slice(1)}</h2>

			{#if productType === 'bimini'}
				<select bind:value={productDetails[productType].pocketType}>
					<option value="">Select Pocket Type</option>
					<option value="square">Square Pockets</option>
					<option value="sculptured">Sculptured Pockets</option>
				</select>

				<label>
					<input type="checkbox" bind:checked={productDetails[productType].hasCutouts} />
					Has cutouts in pockets
				</label>

				<label>
					<input type="checkbox" bind:checked={productDetails[productType].hasStayCutouts} />
					Has stay cutouts
				</label>

				<label>
					<input type="checkbox" bind:checked={productDetails[productType].hasSailWindows} />
					Has sail windows
				</label>
			{/if}

			{#if productType === 'enclosure'}
				<h3>Window Panels</h3>
				{#each productDetails[productType].windowPanels as panel, panelIndex}
					<div class="window-panel">
						<h4>Panel {panelIndex + 1}</h4>

						<select bind:value={panel.windowStyle}>
							<option value="">Select Window Style</option>
							<option value="standard">Standard</option>
							<option value="long-canvas-bottom">Long Canvas Bottom</option>
							<option value="long-clear-bottom">Long Clear Bottom</option>
							<option value="straight-venturi">Straight Venturi</option>
							<option value="curved-venturi">Curved Venturi</option>
						</select>

						<select bind:value={panel.glassType}>
							<option value="">Select Glass Type</option>
							<option value="glass">Glass</option>
							<option value="strataglass">Strataglass</option>
							<option value="polycarbonate">Polycarbonate</option>
						</select>

						<select bind:value={panel.attachmentType.top}>
							<option value="">Select Top Attachment</option>
							<option value="zipper">Zipper</option>
							<option value="keder">Keder</option>
							<option value="zipper-keder">Zipper Keder</option>
							<option value="zipper-keder-velcro">Zipper Keder Velcro</option>
							<option value="snaps-standard">Snaps - Standard</option>
							<option value="snaps-lift-the-dot">Snaps - Lift the Dot</option>
							<option value="snaps-common-sense">Snaps - Common Sense</option>
							<option value="none">None</option>
						</select>

						<!-- Similar selects for bottom, leftSide, and rightSide attachments -->

						<select bind:value={panel.sideStyle.left}>
							<option value="">Select Left Side Style</option>
							<option value="butted">Butted Together</option>
							<option value="rain-flap">Rain Flap</option>
							<option value="tapered">Tapered</option>
							<option value="scalloped">Scalloped</option>
						</select>

						<!-- Similar select for right side style -->

						<h5>Additional Features:</h5>
						{#each Object.entries(panel.features) as [feature, value]}
							<label>
								<input type="checkbox" bind:checked={panel.features[feature]} />
								{feature.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase())}
							</label>
						{/each}
					</div>
				{/each}
				<button onclick={() => addWindowPanel(productType)}>Add Window Panel</button>
			{/if}

			{#if productType === 'sunFly'}
				<select bind:value={$productDetails[productType].poleCount}>
					<option value="">Select Number of Poles</option>
					{#each [1, 2, 3, 4, 5, 6] as num}
						<option value={num}>{num} Pole{num > 1 ? 's' : ''}</option>
					{/each}
				</select>

				<fieldset>
					<legend>Attachment Style</legend>
					<label>
						<input
							type="radio"
							bind:group={$productDetails[productType].attachmentStyle}
							value="keder"
						/>
						Keder
					</label>
					<label>
						<input
							type="radio"
							bind:group={$productDetails[productType].attachmentStyle}
							value="quickRelease"
						/>
						Quick Release Webbing Mounts
					</label>
					<label>
						<input
							type="radio"
							bind:group={$productDetails[productType].attachmentStyle}
							value="both"
						/>
						Both
					</label>
				</fieldset>
			{/if}

			{#if productType === 'dodger'}
				<select bind:value={$productDetails[productType].style}>
					<option value="">Select Dodger Style</option>
					<option value="california">California</option>
					<option value="traditional">Traditional</option>
				</select>

				<select bind:value={$productDetails[productType].glassType}>
					<option value="">Select Glass Type</option>
					<option value="strataglass">Strataglass</option>
					<option value="polycarbonate">Polycarbonate</option>
				</select>

				<label>
					<input type="checkbox" bind:checked={$productDetails[productType].cinchStraps} />
					Cinch Straps in Aft Corners
				</label>

				<select bind:value={$productDetails[productType].centerWindow}>
					<option value="">Select Center Window Style</option>
					<option value="rollUp">Roll Up</option>
					<option value="snapBack">Snap Back</option>
				</select>

				<label>
					<input type="checkbox" bind:checked={$productDetails[productType].chafePatch} />
					Chafe Patch on Front
				</label>

				<select bind:value={$productDetails[productType].travelerRope}>
					<option value="">Select Traveler Rope Option</option>
					<option value="none">None</option>
					<option value="glassSlit">Glass Slit</option>
					<option value="zipper">Zipper</option>
				</select>

				<label>
					<input type="checkbox" bind:checked={$productDetails[productType].cellPhonePocket} />
					Cell Phone Pocket
				</label>
			{/if}

			<button on:click={() => removeProduct(index)}>Remove {productType}</button>
		</div>
	{/each}

	{#if $selectedProducts.length > 0}
		<button on:click={handleSave}>Save Project Details</button>
	{/if}
</main>

<style>
	main {
		max-width: 800px;
		margin: 0 auto;
		padding: 20px;
	}

	.product-form {
		border: 1px solid #ccc;
		padding: 20px;
		margin-bottom: 20px;
		border-radius: 5px;
	}

	.window-panel {
		border: 1px solid #eee;
		padding: 10px;
		margin-bottom: 10px;
		border-radius: 3px;
	}

	select,
	input[type='checkbox'],
	input[type='radio'] {
		margin-bottom: 10px;
	}

	button {
		margin-top: 10px;
	}
</style>
