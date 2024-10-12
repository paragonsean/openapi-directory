

# TransformSummary

Description of the type, names/ids, and input/outputs for a transform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayData** | [**List&lt;DisplayData&gt;**](DisplayData.md) | Transform-specific display data. |  [optional] |
|**id** | **String** | SDK generated id of this transform instance. |  [optional] |
|**inputCollectionName** | **List&lt;String&gt;** | User names for all collection inputs to this transform. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Type of transform. |  [optional] |
|**name** | **String** | User provided name for this transform instance. |  [optional] |
|**outputCollectionName** | **List&lt;String&gt;** | User names for all collection outputs to this transform. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| UNKNOWN_KIND | &quot;UNKNOWN_KIND&quot; |
| PAR_DO_KIND | &quot;PAR_DO_KIND&quot; |
| GROUP_BY_KEY_KIND | &quot;GROUP_BY_KEY_KIND&quot; |
| FLATTEN_KIND | &quot;FLATTEN_KIND&quot; |
| READ_KIND | &quot;READ_KIND&quot; |
| WRITE_KIND | &quot;WRITE_KIND&quot; |
| CONSTANT_KIND | &quot;CONSTANT_KIND&quot; |
| SINGLETON_KIND | &quot;SINGLETON_KIND&quot; |
| SHUFFLE_KIND | &quot;SHUFFLE_KIND&quot; |



