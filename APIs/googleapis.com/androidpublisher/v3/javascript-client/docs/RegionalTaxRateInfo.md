# GooglePlayAndroidDeveloperApi.RegionalTaxRateInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibleForStreamingServiceTaxRate** | **Boolean** | You must tell us if your app contains streaming products to correctly charge US state and local sales tax. Field only supported in the United States. | [optional] 
**streamingTaxType** | **String** | To collect communications or amusement taxes in the United States, choose the appropriate tax category. [Learn more](https://support.google.com/googleplay/android-developer/answer/10463498#streaming_tax). | [optional] 
**taxTier** | **String** | Tax tier to specify reduced tax rate. Developers who sell digital news, magazines, newspapers, books, or audiobooks in various regions may be eligible for reduced tax rates. [Learn more](https://support.google.com/googleplay/android-developer/answer/10463498). | [optional] 



## Enum: StreamingTaxTypeEnum


* `UNSPECIFIED` (value: `"STREAMING_TAX_TYPE_UNSPECIFIED"`)

* `TELCO_VIDEO_RENTAL` (value: `"STREAMING_TAX_TYPE_TELCO_VIDEO_RENTAL"`)

* `TELCO_VIDEO_SALES` (value: `"STREAMING_TAX_TYPE_TELCO_VIDEO_SALES"`)

* `TELCO_VIDEO_MULTI_CHANNEL` (value: `"STREAMING_TAX_TYPE_TELCO_VIDEO_MULTI_CHANNEL"`)

* `TELCO_AUDIO_RENTAL` (value: `"STREAMING_TAX_TYPE_TELCO_AUDIO_RENTAL"`)

* `TELCO_AUDIO_SALES` (value: `"STREAMING_TAX_TYPE_TELCO_AUDIO_SALES"`)

* `TELCO_AUDIO_MULTI_CHANNEL` (value: `"STREAMING_TAX_TYPE_TELCO_AUDIO_MULTI_CHANNEL"`)





## Enum: TaxTierEnum


* `UNSPECIFIED` (value: `"TAX_TIER_UNSPECIFIED"`)

* `BOOKS_1` (value: `"TAX_TIER_BOOKS_1"`)

* `NEWS_1` (value: `"TAX_TIER_NEWS_1"`)

* `NEWS_2` (value: `"TAX_TIER_NEWS_2"`)

* `MUSIC_OR_AUDIO_1` (value: `"TAX_TIER_MUSIC_OR_AUDIO_1"`)

* `LIVE_OR_BROADCAST_1` (value: `"TAX_TIER_LIVE_OR_BROADCAST_1"`)




