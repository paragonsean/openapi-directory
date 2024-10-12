

# ReachabilityDetails

Results of the configuration analysis from the last run of the test.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**Status**](Status.md) |  |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | The overall result of the test&#39;s configuration analysis. |  [optional] |
|**traces** | [**List&lt;Trace&gt;**](Trace.md) | Result may contain a list of traces if a test has multiple possible paths in the network, such as when destination endpoint is a load balancer with multiple backends. |  [optional] |
|**verifyTime** | **String** | The time of the configuration analysis. |  [optional] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| RESULT_UNSPECIFIED | &quot;RESULT_UNSPECIFIED&quot; |
| REACHABLE | &quot;REACHABLE&quot; |
| UNREACHABLE | &quot;UNREACHABLE&quot; |
| AMBIGUOUS | &quot;AMBIGUOUS&quot; |
| UNDETERMINED | &quot;UNDETERMINED&quot; |



