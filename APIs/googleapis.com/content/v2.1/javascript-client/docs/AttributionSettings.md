# ContentApiForShopping.AttributionSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributionLookbackWindowInDays** | **Number** | Required. Lookback windows (in days) used for attribution in this source. Supported values are 7, 30, 40. | [optional] 
**attributionModel** | **String** | Required. Attribution model. | [optional] 
**conversionType** | [**[AttributionSettingsConversionType]**](AttributionSettingsConversionType.md) | Immutable. Unordered list. List of different conversion types a conversion event can be classified as. A standard \&quot;purchase\&quot; type will be automatically created if this list is empty at creation time. | [optional] 



## Enum: AttributionModelEnum


* `ATTRIBUTION_MODEL_UNSPECIFIED` (value: `"ATTRIBUTION_MODEL_UNSPECIFIED"`)

* `CROSS_CHANNEL_LAST_CLICK` (value: `"CROSS_CHANNEL_LAST_CLICK"`)

* `ADS_PREFERRED_LAST_CLICK` (value: `"ADS_PREFERRED_LAST_CLICK"`)

* `CROSS_CHANNEL_DATA_DRIVEN` (value: `"CROSS_CHANNEL_DATA_DRIVEN"`)

* `CROSS_CHANNEL_FIRST_CLICK` (value: `"CROSS_CHANNEL_FIRST_CLICK"`)

* `CROSS_CHANNEL_LINEAR` (value: `"CROSS_CHANNEL_LINEAR"`)

* `CROSS_CHANNEL_POSITION_BASED` (value: `"CROSS_CHANNEL_POSITION_BASED"`)

* `CROSS_CHANNEL_TIME_DECAY` (value: `"CROSS_CHANNEL_TIME_DECAY"`)




