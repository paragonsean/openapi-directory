

# ItemCountByStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | Number of items matching the status code. |  [optional] |
|**indexedItemsCount** | **String** | Number of items matching the status code for which billing is done. This excludes virtual container items from the total count. This count would not be applicable for items with ERROR or NEW_ITEM status code. |  [optional] |
|**statusCode** | [**StatusCodeEnum**](#StatusCodeEnum) | Status of the items. |  [optional] |



## Enum: StatusCodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| MODIFIED | &quot;MODIFIED&quot; |
| NEW_ITEM | &quot;NEW_ITEM&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |



