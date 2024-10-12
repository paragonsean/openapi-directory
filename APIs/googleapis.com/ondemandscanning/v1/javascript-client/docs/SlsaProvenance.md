# OnDemandScanningApi.SlsaProvenance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**builder** | [**SlsaBuilder**](SlsaBuilder.md) |  | [optional] 
**materials** | [**[Material]**](Material.md) | The collection of artifacts that influenced the build including sources, dependencies, build tools, base images, and so on. This is considered to be incomplete unless metadata.completeness.materials is true. Unset or null is equivalent to empty. | [optional] 
**metadata** | [**SlsaMetadata**](SlsaMetadata.md) |  | [optional] 
**recipe** | [**SlsaRecipe**](SlsaRecipe.md) |  | [optional] 


