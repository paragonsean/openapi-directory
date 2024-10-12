

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdNoiseAmbient

Ambient noise threshold. One of 'level' or 'quality' must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**level** | **Integer** | Alerting threshold as adjusted decibels. |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | Alerting threshold as a qualitative ambient noise level. |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| FAIR | &quot;fair&quot; |
| GOOD | &quot;good&quot; |
| INADEQUATE | &quot;inadequate&quot; |
| POOR | &quot;poor&quot; |



