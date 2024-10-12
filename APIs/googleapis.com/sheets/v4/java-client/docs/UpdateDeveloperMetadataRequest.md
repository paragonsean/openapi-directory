

# UpdateDeveloperMetadataRequest

A request to update properties of developer metadata. Updates the properties of the developer metadata selected by the filters to the values provided in the DeveloperMetadata resource. Callers must specify the properties they wish to update in the fields parameter, as well as specify at least one DataFilter matching the metadata they wish to update.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFilters** | [**List&lt;DataFilter&gt;**](DataFilter.md) | The filters matching the developer metadata entries to update. |  [optional] |
|**developerMetadata** | [**DeveloperMetadata**](DeveloperMetadata.md) |  |  [optional] |
|**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;developerMetadata&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. |  [optional] |



