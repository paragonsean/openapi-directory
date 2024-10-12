

# ProbingDetails

Results of active probing from the last run of the test.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abortCause** | [**AbortCauseEnum**](#AbortCauseEnum) | The reason probing was aborted. |  [optional] |
|**destinationEgressLocation** | [**EdgeLocation**](EdgeLocation.md) |  |  [optional] |
|**endpointInfo** | [**EndpointInfo**](EndpointInfo.md) |  |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**probingLatency** | [**LatencyDistribution**](LatencyDistribution.md) |  |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | The overall result of active probing. |  [optional] |
|**sentProbeCount** | **Integer** | Number of probes sent. |  [optional] |
|**successfulProbeCount** | **Integer** | Number of probes that reached the destination. |  [optional] |
|**verifyTime** | **String** | The time that reachability was assessed through active probing. |  [optional] |



## Enum: AbortCauseEnum

| Name | Value |
|---- | -----|
| PROBING_ABORT_CAUSE_UNSPECIFIED | &quot;PROBING_ABORT_CAUSE_UNSPECIFIED&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| NO_SOURCE_LOCATION | &quot;NO_SOURCE_LOCATION&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| PROBING_RESULT_UNSPECIFIED | &quot;PROBING_RESULT_UNSPECIFIED&quot; |
| REACHABLE | &quot;REACHABLE&quot; |
| UNREACHABLE | &quot;UNREACHABLE&quot; |
| REACHABILITY_INCONSISTENT | &quot;REACHABILITY_INCONSISTENT&quot; |
| UNDETERMINED | &quot;UNDETERMINED&quot; |



