# CloudRunAdminApi.GoogleCloudRunV2TrafficTargetStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **Number** | Specifies percent of the traffic to this Revision. | [optional] 
**revision** | **String** | Revision to which this traffic is sent. | [optional] 
**tag** | **String** | Indicates the string used in the URI to exclusively reference this target. | [optional] 
**type** | **String** | The allocation type for this traffic target. | [optional] 
**uri** | **String** | Displays the target URI. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"TRAFFIC_TARGET_ALLOCATION_TYPE_UNSPECIFIED"`)

* `LATEST` (value: `"TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"`)

* `REVISION` (value: `"TRAFFIC_TARGET_ALLOCATION_TYPE_REVISION"`)




