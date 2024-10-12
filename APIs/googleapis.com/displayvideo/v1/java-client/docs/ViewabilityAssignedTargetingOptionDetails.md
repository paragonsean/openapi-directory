

# ViewabilityAssignedTargetingOptionDetails

Assigned viewability targeting option details. This will be populated in the viewability_details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_VIEWABILITY`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_VIEWABILITY&#x60; (e.g., \&quot;509010\&quot; for targeting the &#x60;VIEWABILITY_10_PERCENT_OR_MORE&#x60; option). |  [optional] |
|**viewability** | [**ViewabilityEnum**](#ViewabilityEnum) | Required. The predicted viewability percentage. |  [optional] |



## Enum: ViewabilityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VIEWABILITY_UNSPECIFIED&quot; |
| _10_PERCENT_OR_MORE | &quot;VIEWABILITY_10_PERCENT_OR_MORE&quot; |
| _20_PERCENT_OR_MORE | &quot;VIEWABILITY_20_PERCENT_OR_MORE&quot; |
| _30_PERCENT_OR_MORE | &quot;VIEWABILITY_30_PERCENT_OR_MORE&quot; |
| _40_PERCENT_OR_MORE | &quot;VIEWABILITY_40_PERCENT_OR_MORE&quot; |
| _50_PERCENT_OR_MORE | &quot;VIEWABILITY_50_PERCENT_OR_MORE&quot; |
| _60_PERCENT_OR_MORE | &quot;VIEWABILITY_60_PERCENT_OR_MORE&quot; |
| _70_PERCENT_OR_MORE | &quot;VIEWABILITY_70_PERCENT_OR_MORE&quot; |
| _80_PERCENT_OR_MORE | &quot;VIEWABILITY_80_PERCENT_OR_MORE&quot; |
| _90_PERCENT_OR_MORE | &quot;VIEWABILITY_90_PERCENT_OR_MORE&quot; |



