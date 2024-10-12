

# GoogleCloudAiplatformV1NasTrial

Represents a uCAIP NasJob trial.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Output only. Time when the NasTrial&#39;s status changed to &#x60;SUCCEEDED&#x60; or &#x60;INFEASIBLE&#x60;. |  [optional] [readonly] |
|**finalMeasurement** | [**GoogleCloudAiplatformV1Measurement**](GoogleCloudAiplatformV1Measurement.md) |  |  [optional] |
|**id** | **String** | Output only. The identifier of the NasTrial assigned by the service. |  [optional] [readonly] |
|**startTime** | **String** | Output only. Time when the NasTrial was started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of the NasTrial. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| STOPPING | &quot;STOPPING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| INFEASIBLE | &quot;INFEASIBLE&quot; |



