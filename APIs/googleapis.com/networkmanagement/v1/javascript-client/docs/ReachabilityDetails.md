# NetworkManagementApi.ReachabilityDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**Status**](Status.md) |  | [optional] 
**result** | **String** | The overall result of the test&#39;s configuration analysis. | [optional] 
**traces** | [**[Trace]**](Trace.md) | Result may contain a list of traces if a test has multiple possible paths in the network, such as when destination endpoint is a load balancer with multiple backends. | [optional] 
**verifyTime** | **String** | The time of the configuration analysis. | [optional] 



## Enum: ResultEnum


* `RESULT_UNSPECIFIED` (value: `"RESULT_UNSPECIFIED"`)

* `REACHABLE` (value: `"REACHABLE"`)

* `UNREACHABLE` (value: `"UNREACHABLE"`)

* `AMBIGUOUS` (value: `"AMBIGUOUS"`)

* `UNDETERMINED` (value: `"UNDETERMINED"`)




