

# PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsWarningsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **String** | Digest of the image that caused the warning. |  [optional] |
|**repository** | **String** | Name of the repository of the image that caused the warning. |  [optional] |
|**tags** | **List&lt;String&gt;** | Current tags if warning is &#x60;current_tag&#x60;. |  [optional] |
|**warning** | [**WarningEnum**](#WarningEnum) | Warning type. |  [optional] |



## Enum: WarningEnum

| Name | Value |
|---- | -----|
| IS_ACTIVE | &quot;is_active&quot; |
| CURRENT_TAG | &quot;current_tag&quot; |



