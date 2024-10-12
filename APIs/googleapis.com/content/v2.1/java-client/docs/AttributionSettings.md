

# AttributionSettings

Represents attribution settings for conversion sources receiving pre-attribution data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionLookbackWindowInDays** | **Integer** | Required. Lookback windows (in days) used for attribution in this source. Supported values are 7, 30, 40. |  [optional] |
|**attributionModel** | [**AttributionModelEnum**](#AttributionModelEnum) | Required. Attribution model. |  [optional] |
|**conversionType** | [**List&lt;AttributionSettingsConversionType&gt;**](AttributionSettingsConversionType.md) | Immutable. Unordered list. List of different conversion types a conversion event can be classified as. A standard \&quot;purchase\&quot; type will be automatically created if this list is empty at creation time. |  [optional] |



## Enum: AttributionModelEnum

| Name | Value |
|---- | -----|
| ATTRIBUTION_MODEL_UNSPECIFIED | &quot;ATTRIBUTION_MODEL_UNSPECIFIED&quot; |
| CROSS_CHANNEL_LAST_CLICK | &quot;CROSS_CHANNEL_LAST_CLICK&quot; |
| ADS_PREFERRED_LAST_CLICK | &quot;ADS_PREFERRED_LAST_CLICK&quot; |
| CROSS_CHANNEL_DATA_DRIVEN | &quot;CROSS_CHANNEL_DATA_DRIVEN&quot; |
| CROSS_CHANNEL_FIRST_CLICK | &quot;CROSS_CHANNEL_FIRST_CLICK&quot; |
| CROSS_CHANNEL_LINEAR | &quot;CROSS_CHANNEL_LINEAR&quot; |
| CROSS_CHANNEL_POSITION_BASED | &quot;CROSS_CHANNEL_POSITION_BASED&quot; |
| CROSS_CHANNEL_TIME_DECAY | &quot;CROSS_CHANNEL_TIME_DECAY&quot; |



