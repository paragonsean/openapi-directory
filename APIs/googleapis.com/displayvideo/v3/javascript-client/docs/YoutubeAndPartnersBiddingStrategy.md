# DisplayVideo360Api.YoutubeAndPartnersBiddingStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupEffectiveTargetCpaSource** | **String** | Output only. Source of the effective target CPA value for ad group. | [optional] [readonly] 
**adGroupEffectiveTargetCpaValue** | **String** | Output only. The effective target CPA for ad group, in micros of advertiser&#39;s currency. | [optional] [readonly] 
**type** | **String** | The type of the bidding strategy. | [optional] 
**value** | **String** | The value used by the bidding strategy. When the bidding strategy is assigned at the line item level, this field is only applicable for the following strategy types: * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS&#x60; When the bidding strategy is assigned at the ad group level, this field is only applicable for the following strategy types: * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPM&#x60; * &#x60;YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS&#x60; If not using an applicable strategy, the value of this field will be 0. | [optional] 



## Enum: AdGroupEffectiveTargetCpaSourceEnum


* `UNSPECIFIED` (value: `"BIDDING_SOURCE_UNSPECIFIED"`)

* `LINE_ITEM` (value: `"BIDDING_SOURCE_LINE_ITEM"`)

* `AD_GROUP` (value: `"BIDDING_SOURCE_AD_GROUP"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_UNSPECIFIED"`)

* `MANUAL_CPV` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPV"`)

* `MANUAL_CPM` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MANUAL_CPM"`)

* `TARGET_CPA` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPA"`)

* `TARGET_CPM` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPM"`)

* `MAXIMIZE_LIFT` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_LIFT"`)

* `MAXIMIZE_CONVERSIONS` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSIONS"`)

* `TARGET_CPV` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_CPV"`)

* `TARGET_ROAS` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_TARGET_ROAS"`)

* `MAXIMIZE_CONVERSION_VALUE` (value: `"YOUTUBE_AND_PARTNERS_BIDDING_STRATEGY_TYPE_MAXIMIZE_CONVERSION_VALUE"`)




