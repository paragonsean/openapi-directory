

# RegionalTaxRateInfo

Specified details about taxation in a given geographical region.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eligibleForStreamingServiceTaxRate** | **Boolean** | You must tell us if your app contains streaming products to correctly charge US state and local sales tax. Field only supported in the United States. |  [optional] |
|**streamingTaxType** | [**StreamingTaxTypeEnum**](#StreamingTaxTypeEnum) | To collect communications or amusement taxes in the United States, choose the appropriate tax category. [Learn more](https://support.google.com/googleplay/android-developer/answer/10463498#streaming_tax). |  [optional] |
|**taxTier** | [**TaxTierEnum**](#TaxTierEnum) | Tax tier to specify reduced tax rate. Developers who sell digital news, magazines, newspapers, books, or audiobooks in various regions may be eligible for reduced tax rates. [Learn more](https://support.google.com/googleplay/android-developer/answer/10463498). |  [optional] |



## Enum: StreamingTaxTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STREAMING_TAX_TYPE_UNSPECIFIED&quot; |
| TELCO_VIDEO_RENTAL | &quot;STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL&quot; |
| TELCO_VIDEO_SALES | &quot;STREAMING_TAX_TYPE_TELCO_VIDEO_SALES&quot; |
| TELCO_VIDEO_MULTI_CHANNEL | &quot;STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL&quot; |
| TELCO_AUDIO_RENTAL | &quot;STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL&quot; |
| TELCO_AUDIO_SALES | &quot;STREAMING_TAX_TYPE_TELCO_AUDIO_SALES&quot; |
| TELCO_AUDIO_MULTI_CHANNEL | &quot;STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL&quot; |



## Enum: TaxTierEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TAX_TIER_UNSPECIFIED&quot; |
| BOOKS_1 | &quot;TAX_TIER_BOOKS_1&quot; |
| NEWS_1 | &quot;TAX_TIER_NEWS_1&quot; |
| NEWS_2 | &quot;TAX_TIER_NEWS_2&quot; |
| MUSIC_OR_AUDIO_1 | &quot;TAX_TIER_MUSIC_OR_AUDIO_1&quot; |
| LIVE_OR_BROADCAST_1 | &quot;TAX_TIER_LIVE_OR_BROADCAST_1&quot; |



