

# ReleasesGetLatestByDistributionGroup200ResponseDistributionStoresInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID identifying a unique distribution store. |  |
|**name** | **String** | A name identifying a unique distribution store. |  [optional] |
|**publishingStatus** | **String** | publishing status of the release in the store. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | type of the distribution store currently stores type can be intune, googleplay or windows. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTUNE | &quot;intune&quot; |
| GOOGLEPLAY | &quot;googleplay&quot; |
| APPLE | &quot;apple&quot; |
| NONE | &quot;none&quot; |



