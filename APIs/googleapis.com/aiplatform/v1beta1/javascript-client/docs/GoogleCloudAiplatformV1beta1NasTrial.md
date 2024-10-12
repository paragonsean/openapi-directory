# VertexAiApi.GoogleCloudAiplatformV1beta1NasTrial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | Output only. Time when the NasTrial&#39;s status changed to &#x60;SUCCEEDED&#x60; or &#x60;INFEASIBLE&#x60;. | [optional] [readonly] 
**finalMeasurement** | [**GoogleCloudAiplatformV1beta1Measurement**](GoogleCloudAiplatformV1beta1Measurement.md) |  | [optional] 
**id** | **String** | Output only. The identifier of the NasTrial assigned by the service. | [optional] [readonly] 
**startTime** | **String** | Output only. Time when the NasTrial was started. | [optional] [readonly] 
**state** | **String** | Output only. The detailed state of the NasTrial. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `STOPPING` (value: `"STOPPING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `INFEASIBLE` (value: `"INFEASIBLE"`)




