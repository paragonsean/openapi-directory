

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdPm25

PM2.5 concentration threshold. One of 'concentration' or 'quality' must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**concentration** | **Integer** | Alerting threshold as PM2.5 parts per million. |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | Alerting threshold as a qualitative PM2.5 level. |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| FAIR | &quot;fair&quot; |
| GOOD | &quot;good&quot; |
| INADEQUATE | &quot;inadequate&quot; |
| POOR | &quot;poor&quot; |



