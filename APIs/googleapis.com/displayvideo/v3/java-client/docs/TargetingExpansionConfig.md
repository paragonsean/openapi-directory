

# TargetingExpansionConfig

Settings that control the [optimized targeting](//support.google.com/displayvideo/answer/12060859) settings of the line item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audienceExpansionLevel** | [**AudienceExpansionLevelEnum**](#AudienceExpansionLevelEnum) | Output only. Magnitude of expansion for eligible first-party user lists under this ad group. This field only applies to YouTube and Partners line item and ad group resources. |  [optional] [readonly] |
|**audienceExpansionSeedListExcluded** | **Boolean** | Output only. Whether to exclude seed list for audience expansion. This field only applies to YouTube and Partners line item and ad group resources. |  [optional] [readonly] |
|**enableOptimizedTargeting** | **Boolean** | Required. Whether to enable Optimized Targeting for the line item. |  [optional] |



## Enum: AudienceExpansionLevelEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| NO_REACH | &quot;NO_REACH&quot; |
| LEAST_REACH | &quot;LEAST_REACH&quot; |
| MID_REACH | &quot;MID_REACH&quot; |
| MOST_REACH | &quot;MOST_REACH&quot; |



