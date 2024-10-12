

# YoutubeAndPartnersBiddingStrategy

Settings that control the bid strategy for YouTube and Partners resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroupEffectiveTargetCpaSource** | [**AdGroupEffectiveTargetCpaSourceEnum**](#AdGroupEffectiveTargetCpaSourceEnum) | Output only. Source of the effective target CPA value for ad group. |  [optional] [readonly] |
|**adGroupEffectiveTargetCpaValue** | **String** | Output only. The effective target CPA for ad group, in micros of advertiser&#39;s currency. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the bidding strategy. |  [optional] |
|**value** | **String** | The value used by the bidding strategy. When the bidding strategy is assigned at the line item level, this field is only applicable for the following strategy types: * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS&#x60; When the bidding strategy is assigned at the ad group level, this field is only applicable for the following strategy types: * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPM&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS&#x60; If not using an applicable strategy, the value of this field will be 0. |  [optional] |



## Enum: AdGroupEffectiveTargetCpaSourceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;BIDDING_SOURCE_UNSPECIFIED&quot; |
| LINE_ITEM | &quot;BIDDING_SOURCE_LINE_ITEM&quot; |
| AD_GROUP | &quot;BIDDING_SOURCE_AD_GROUP&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_UNSPECIFIED&quot; |
| MANUAL_CPV | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV&quot; |
| MANUAL_CPM | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM&quot; |
| TARGET_CPA | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA&quot; |
| TARGET_CPM | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPM&quot; |
| MAXIMIZE_LIFT | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_LIFT&quot; |
| MAXIMIZE_CONVERSIONS | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSIONS&quot; |
| TARGET_CPV | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPV&quot; |
| TARGET_ROAS | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSION_VALUE&quot; |



