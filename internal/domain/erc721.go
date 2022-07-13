package domain

type ERC721Trait struct {
	TraitType string `json:"trait_type"`
	Value     string `json:"value"`
}

type ERC721Metadata struct {
	Image      string         `json:"image"`
	Attributes []*ERC721Trait `json:"attributes"`
}
