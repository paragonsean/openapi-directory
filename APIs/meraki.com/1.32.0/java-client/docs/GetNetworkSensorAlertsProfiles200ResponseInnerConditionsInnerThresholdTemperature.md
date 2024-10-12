

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTemperature

Temperature threshold. One of 'celsius', 'fahrenheit', or 'quality' must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**celsius** | **Float** | Alerting threshold in degrees Celsius. |  [optional] |
|**fahrenheit** | **Float** | Alerting threshold in degrees Fahrenheit. |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | Alerting threshold as a qualitative temperature level. |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| FAIR | &quot;fair&quot; |
| GOOD | &quot;good&quot; |
| INADEQUATE | &quot;inadequate&quot; |
| POOR | &quot;poor&quot; |



