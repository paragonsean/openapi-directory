

# CreativeOptimizationConfiguration

Creative optimization settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of this creative optimization config. This field is auto-generated when the campaign is inserted or updated. It can be null for existing campaigns. |  [optional] |
|**name** | **String** | Name of this creative optimization config. This is a required field and must be less than 129 characters long. |  [optional] |
|**optimizationActivitys** | [**List&lt;OptimizationActivity&gt;**](OptimizationActivity.md) | List of optimization activities associated with this configuration. |  [optional] |
|**optimizationModel** | [**OptimizationModelEnum**](#OptimizationModelEnum) | Optimization model for this configuration. |  [optional] |



## Enum: OptimizationModelEnum

| Name | Value |
|---- | -----|
| CLICK | &quot;CLICK&quot; |
| POST_CLICK | &quot;POST_CLICK&quot; |
| POST_IMPRESSION | &quot;POST_IMPRESSION&quot; |
| POST_CLICK_AND_IMPRESSION | &quot;POST_CLICK_AND_IMPRESSION&quot; |
| VIDEO_COMPLETION | &quot;VIDEO_COMPLETION&quot; |



