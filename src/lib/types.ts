export type BiminiOptions = {
	pocket: {
		shape: string;
		cutouts: boolean;
	};
	main: {
		window: boolean;
		stayCutout: boolean;
	};
	notes: string;
};

export type WindowOptions = {
	windowStyle: string;
	glassType: string;
	attachmentType: {
		top: string;
		bottom: string;
		leftSide: string;
		rightSide: string;
	};
	sideStyle: {
		left: string;
		right: string;
	};
	features: {
		smiles: boolean;
		vents: boolean;
		burnStrips: boolean;
		cutouts: boolean;
		cinchStraps: boolean;
	};
	notes: string;
};
