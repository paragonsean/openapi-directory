# VertexAiSearchForRetailApi.GoogleCloudRetailV2alphaBatchRemoveCatalogAttributesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletedCatalogAttributes** | **[String]** | Catalog attributes that were deleted. Only pre-loaded catalog attributes that are neither in use by products nor predefined can be deleted. | [optional] 
**resetCatalogAttributes** | **[String]** | Catalog attributes that were reset. Catalog attributes that are either in use by products or are predefined attributes cannot be deleted; however, their configuration properties will reset to default values upon removal request. | [optional] 


