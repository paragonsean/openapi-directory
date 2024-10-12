

# PostNamespacesDeleteImagesRequestIgnoreWarningsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **String** | Digest of the image to ignore the warning for. |  |
|**repository** | **String** | Name of the repository of the image to ignore the warning for. |  |
|**tags** | **List&lt;String&gt;** | Current tags to ignore. |  [optional] |
|**warning** | [**WarningEnum**](#WarningEnum) | Warning to ignore. |  |



## Enum: WarningEnum

| Name | Value |
|---- | -----|
| IS_ACTIVE | &quot;is_active&quot; |
| CURRENT_TAG | &quot;current_tag&quot; |



