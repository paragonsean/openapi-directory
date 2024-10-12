# NetworkManagementApi.ProbingDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abortCause** | **String** | The reason probing was aborted. | [optional] 
**destinationEgressLocation** | [**EdgeLocation**](EdgeLocation.md) |  | [optional] 
**endpointInfo** | [**EndpointInfo**](EndpointInfo.md) |  | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**probingLatency** | [**LatencyDistribution**](LatencyDistribution.md) |  | [optional] 
**result** | **String** | The overall result of active probing. | [optional] 
**sentProbeCount** | **Number** | Number of probes sent. | [optional] 
**successfulProbeCount** | **Number** | Number of probes that reached the destination. | [optional] 
**verifyTime** | **String** | The time that reachability was assessed through active probing. | [optional] 



## Enum: AbortCauseEnum


* `PROBING_ABORT_CAUSE_UNSPECIFIED` (value: `"PROBING_ABORT_CAUSE_UNSPECIFIED"`)

* `PERMISSION_DENIED` (value: `"PERMISSION_DENIED"`)

* `NO_SOURCE_LOCATION` (value: `"NO_SOURCE_LOCATION"`)





## Enum: ResultEnum


* `PROBING_RESULT_UNSPECIFIED` (value: `"PROBING_RESULT_UNSPECIFIED"`)

* `REACHABLE` (value: `"REACHABLE"`)

* `UNREACHABLE` (value: `"UNREACHABLE"`)

* `REACHABILITY_INCONSISTENT` (value: `"REACHABILITY_INCONSISTENT"`)

* `UNDETERMINED` (value: `"UNDETERMINED"`)




