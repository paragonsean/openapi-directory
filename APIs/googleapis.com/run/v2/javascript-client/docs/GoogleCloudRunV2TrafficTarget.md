# CloudRunAdminApi.GoogleCloudRunV2TrafficTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **Number** | Specifies percent of the traffic to this Revision. This defaults to zero if unspecified. | [optional] 
**revision** | **String** | Revision to which to send this portion of traffic, if traffic allocation is by revision. | [optional] 
**tag** | **String** | Indicates a string to be part of the URI to exclusively reference this target. | [optional] 
**type** | **String** | The allocation type for this traffic target. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED"`)

* `LATEST` (value: `"TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"`)

* `REVISION` (value: `"TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION"`)




