# BeyondCorpApi.GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Required. Unique Id for the resource. | [optional] 
**resource** | **{String: Object}** | Specific details for the resource. This is for internal use only. | [optional] 
**status** | **String** | Overall health status. Overall status is derived based on the status of each sub level resources. | [optional] 
**sub** | [**[GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo]**](GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo.md) | List of Info for the sub level resources. | [optional] 
**time** | **String** | The timestamp to collect the info. It is suggested to be set by the topmost level resource only. | [optional] 



## Enum: StatusEnum


* `HEALTH_STATUS_UNSPECIFIED` (value: `"HEALTH_STATUS_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `UNHEALTHY` (value: `"UNHEALTHY"`)

* `UNRESPONSIVE` (value: `"UNRESPONSIVE"`)

* `DEGRADED` (value: `"DEGRADED"`)




