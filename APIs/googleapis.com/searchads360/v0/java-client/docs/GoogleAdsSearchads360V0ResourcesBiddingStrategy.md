

# GoogleAdsSearchads360V0ResourcesBiddingStrategy

A bidding strategy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignCount** | **String** | Output only. The number of campaigns attached to this bidding strategy. This field is read-only. |  [optional] [readonly] |
|**currencyCode** | **String** | Immutable. The currency used by the bidding strategy (ISO 4217 three-letter code). For bidding strategies in manager customers, this currency can be set on creation and defaults to the manager customer&#39;s currency. For serving customers, this field cannot be set; all strategies in a serving customer implicitly use the serving customer&#39;s currency. In all cases the effective_currency_code field returns the currency used by the strategy. |  [optional] |
|**effectiveCurrencyCode** | **String** | Output only. The currency used by the bidding strategy (ISO 4217 three-letter code). For bidding strategies in manager customers, this is the currency set by the advertiser when creating the strategy. For serving customers, this is the customer&#39;s currency_code. Bidding strategy metrics are reported in this currency. This field is read-only. |  [optional] [readonly] |
|**enhancedCpc** | **Object** | An automated bidding strategy that raises bids for clicks that seem more likely to lead to a conversion and lowers them for clicks where they seem less likely. This bidding strategy is deprecated and cannot be created anymore. Use ManualCpc with enhanced_cpc_enabled set to true for equivalent functionality. |  [optional] |
|**id** | **String** | Output only. The ID of the bidding strategy. |  [optional] [readonly] |
|**maximizeConversionValue** | [**GoogleAdsSearchads360V0CommonMaximizeConversionValue**](GoogleAdsSearchads360V0CommonMaximizeConversionValue.md) |  |  [optional] |
|**maximizeConversions** | [**GoogleAdsSearchads360V0CommonMaximizeConversions**](GoogleAdsSearchads360V0CommonMaximizeConversions.md) |  |  [optional] |
|**name** | **String** | The name of the bidding strategy. All bidding strategies within an account must be named distinctly. The length of this string should be between 1 and 255, inclusive, in UTF-8 bytes, (trimmed). |  [optional] |
|**nonRemovedCampaignCount** | **String** | Output only. The number of non-removed campaigns attached to this bidding strategy. This field is read-only. |  [optional] [readonly] |
|**resourceName** | **String** | Immutable. The resource name of the bidding strategy. Bidding strategy resource names have the form: &#x60;customers/{customer_id}/biddingStrategies/{bidding_strategy_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the bidding strategy. This field is read-only. |  [optional] [readonly] |
|**targetCpa** | [**GoogleAdsSearchads360V0CommonTargetCpa**](GoogleAdsSearchads360V0CommonTargetCpa.md) |  |  [optional] |
|**targetImpressionShare** | [**GoogleAdsSearchads360V0CommonTargetImpressionShare**](GoogleAdsSearchads360V0CommonTargetImpressionShare.md) |  |  [optional] |
|**targetOutrankShare** | [**GoogleAdsSearchads360V0CommonTargetOutrankShare**](GoogleAdsSearchads360V0CommonTargetOutrankShare.md) |  |  [optional] |
|**targetRoas** | [**GoogleAdsSearchads360V0CommonTargetRoas**](GoogleAdsSearchads360V0CommonTargetRoas.md) |  |  [optional] |
|**targetSpend** | [**GoogleAdsSearchads360V0CommonTargetSpend**](GoogleAdsSearchads360V0CommonTargetSpend.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the bidding strategy. Create a bidding strategy by setting the bidding scheme. This field is read-only. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| COMMISSION | &quot;COMMISSION&quot; |
| ENHANCED_CPC | &quot;ENHANCED_CPC&quot; |
| INVALID | &quot;INVALID&quot; |
| MANUAL_CPA | &quot;MANUAL_CPA&quot; |
| MANUAL_CPC | &quot;MANUAL_CPC&quot; |
| MANUAL_CPM | &quot;MANUAL_CPM&quot; |
| MANUAL_CPV | &quot;MANUAL_CPV&quot; |
| MAXIMIZE_CONVERSIONS | &quot;MAXIMIZE_CONVERSIONS&quot; |
| MAXIMIZE_CONVERSION_VALUE | &quot;MAXIMIZE_CONVERSION_VALUE&quot; |
| PAGE_ONE_PROMOTED | &quot;PAGE_ONE_PROMOTED&quot; |
| PERCENT_CPC | &quot;PERCENT_CPC&quot; |
| TARGET_CPA | &quot;TARGET_CPA&quot; |
| TARGET_CPM | &quot;TARGET_CPM&quot; |
| TARGET_IMPRESSION_SHARE | &quot;TARGET_IMPRESSION_SHARE&quot; |
| TARGET_OUTRANK_SHARE | &quot;TARGET_OUTRANK_SHARE&quot; |
| TARGET_ROAS | &quot;TARGET_ROAS&quot; |
| TARGET_SPEND | &quot;TARGET_SPEND&quot; |



