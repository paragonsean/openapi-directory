

# CreativeRestrictions

Represents creative restrictions associated to Programmatic Guaranteed/ Preferred Deal in Ad Manager. This doesn't apply to Private Auction and AdX Preferred Deals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeFormat** | [**CreativeFormatEnum**](#CreativeFormatEnum) | The format of the environment that the creatives will be displayed in. |  [optional] |
|**creativeSpecifications** | [**List&lt;CreativeSpecification&gt;**](CreativeSpecification.md) |  |  [optional] |
|**skippableAdType** | [**SkippableAdTypeEnum**](#SkippableAdTypeEnum) | Skippable video ads allow viewers to skip ads after 5 seconds. |  [optional] |



## Enum: CreativeFormatEnum

| Name | Value |
|---- | -----|
| CREATIVE_FORMAT_UNSPECIFIED | &quot;CREATIVE_FORMAT_UNSPECIFIED&quot; |
| DISPLAY | &quot;DISPLAY&quot; |
| VIDEO | &quot;VIDEO&quot; |



## Enum: SkippableAdTypeEnum

| Name | Value |
|---- | -----|
| SKIPPABLE_AD_TYPE_UNSPECIFIED | &quot;SKIPPABLE_AD_TYPE_UNSPECIFIED&quot; |
| SKIPPABLE | &quot;SKIPPABLE&quot; |
| INSTREAM_SELECT | &quot;INSTREAM_SELECT&quot; |
| NOT_SKIPPABLE | &quot;NOT_SKIPPABLE&quot; |



