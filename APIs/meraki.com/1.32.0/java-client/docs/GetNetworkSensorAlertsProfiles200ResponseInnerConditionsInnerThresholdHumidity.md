

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdHumidity

Humidity threshold. One of 'relativePercentage' or 'quality' must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quality** | [**QualityEnum**](#QualityEnum) | Alerting threshold as a qualitative humidity level. |  [optional] |
|**relativePercentage** | **Integer** | Alerting threshold in %RH. |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| FAIR | &quot;fair&quot; |
| GOOD | &quot;good&quot; |
| INADEQUATE | &quot;inadequate&quot; |
| POOR | &quot;poor&quot; |



