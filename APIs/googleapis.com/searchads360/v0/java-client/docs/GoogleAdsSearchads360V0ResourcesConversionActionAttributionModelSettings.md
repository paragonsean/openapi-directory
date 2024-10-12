

# GoogleAdsSearchads360V0ResourcesConversionActionAttributionModelSettings

Settings related to this conversion action's attribution model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionModel** | [**AttributionModelEnum**](#AttributionModelEnum) | The attribution model type of this conversion action. |  [optional] |
|**dataDrivenModelStatus** | [**DataDrivenModelStatusEnum**](#DataDrivenModelStatusEnum) | Output only. The status of the data-driven attribution model for the conversion action. |  [optional] [readonly] |



## Enum: AttributionModelEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| GOOGLE_ADS_LAST_CLICK | &quot;GOOGLE_ADS_LAST_CLICK&quot; |
| GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK | &quot;GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK&quot; |
| GOOGLE_SEARCH_ATTRIBUTION_LINEAR | &quot;GOOGLE_SEARCH_ATTRIBUTION_LINEAR&quot; |
| GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY | &quot;GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY&quot; |
| GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED | &quot;GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED&quot; |
| GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN | &quot;GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN&quot; |



## Enum: DataDrivenModelStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| AVAILABLE | &quot;AVAILABLE&quot; |
| STALE | &quot;STALE&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| NEVER_GENERATED | &quot;NEVER_GENERATED&quot; |



