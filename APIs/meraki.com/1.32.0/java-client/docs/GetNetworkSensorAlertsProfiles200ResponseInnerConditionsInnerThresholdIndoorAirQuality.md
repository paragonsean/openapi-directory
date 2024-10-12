

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdIndoorAirQuality

Indoor air quality score threshold. One of 'score' or 'quality' must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quality** | [**QualityEnum**](#QualityEnum) | Alerting threshold as a qualitative indoor air quality level. |  [optional] |
|**score** | **Integer** | Alerting threshold as indoor air quality score. |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| FAIR | &quot;fair&quot; |
| GOOD | &quot;good&quot; |
| INADEQUATE | &quot;inadequate&quot; |
| POOR | &quot;poor&quot; |



