

# GetNetworkSensorAlertsProfiles200ResponseInnerConditionsInnerThresholdTvoc

TVOC concentration threshold. One of 'concentration' or 'quality' must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**concentration** | **Integer** | Alerting threshold as TVOC micrograms per cubic meter. |  [optional] |
|**quality** | [**QualityEnum**](#QualityEnum) | Alerting threshold as a qualitative TVOC level. |  [optional] |



## Enum: QualityEnum

| Name | Value |
|---- | -----|
| FAIR | &quot;fair&quot; |
| GOOD | &quot;good&quot; |
| INADEQUATE | &quot;inadequate&quot; |
| POOR | &quot;poor&quot; |



