

# TargetingExpansionConfig

Settings that control the [optimized targeting](//support.google.com/displayvideo/answer/12060859) settings of the line item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**excludeFirstPartyAudience** | **Boolean** | Whether to exclude first-party audiences from use in targeting expansion. This field was deprecated with the launch of [optimized targeting](//support.google.com/displayvideo/answer/12060859). This field will be set to &#x60;false&#x60;. If this field is set to &#x60;true&#x60; when deprecated, all positive first-party audience targeting assigned to this line item will be replaced with negative targeting of the same first-party audiences to ensure the continued exclusion of those audiences. |  [optional] |
|**targetingExpansionLevel** | [**TargetingExpansionLevelEnum**](#TargetingExpansionLevelEnum) | Required. Whether optimized targeting is turned on. This field supports the following values: * &#x60;NO_EXPANSION&#x60;: optimized targeting is turned off * &#x60;LEAST_EXPANSION&#x60;: optimized targeting is turned on If this field is set to any other value, it will automatically be set to &#x60;LEAST_EXPANSION&#x60;. &#x60;NO_EXPANSION&#x60; will be the default value for the field and will be automatically assigned if you do not set the field. |  [optional] |



## Enum: TargetingExpansionLevelEnum

| Name | Value |
|---- | -----|
| TARGETING_EXPANSION_LEVEL_UNSPECIFIED | &quot;TARGETING_EXPANSION_LEVEL_UNSPECIFIED&quot; |
| NO_EXPANSION | &quot;NO_EXPANSION&quot; |
| LEAST_EXPANSION | &quot;LEAST_EXPANSION&quot; |
| SOME_EXPANSION | &quot;SOME_EXPANSION&quot; |
| BALANCED_EXPANSION | &quot;BALANCED_EXPANSION&quot; |
| MORE_EXPANSION | &quot;MORE_EXPANSION&quot; |
| MOST_EXPANSION | &quot;MOST_EXPANSION&quot; |



