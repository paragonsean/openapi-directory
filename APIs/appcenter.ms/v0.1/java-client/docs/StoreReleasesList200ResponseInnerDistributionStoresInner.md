

# StoreReleasesList200ResponseInnerDistributionStoresInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID identifying a unique distribution store. |  [optional] |
|**isLatest** | **Boolean** | Is the containing release the latest one in this distribution store. |  [optional] |
|**name** | **String** | A name identifying a unique distribution store. |  [optional] |
|**publishingStatus** | **String** | A status identifying the status of release in the distribution store. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | A type identifying the type of distribution store. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GOOGLEPLAY | &quot;googleplay&quot; |
| INTUNE | &quot;intune&quot; |
| APPLE | &quot;apple&quot; |



