

# ProfileResponse

The profile response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | The profile creation time (UTC). |  [optional] |
|**description** | **String** | The profile description. |  [optional] |
|**error** | [**ModelErrorResponse**](ModelErrorResponse.md) |  |  [optional] |
|**imageId** | **String** | The Image Id. |  [optional] |
|**inputData** | **String** | The input data. |  [optional] |
|**kvTags** | **Map&lt;String, String&gt;** | The profile tags dictionary. Tags are mutable. |  [optional] |
|**name** | **String** | The profile name. |  [optional] |
|**profileRunResult** | **String** | The profile run result. |  [optional] |
|**profilingErrorLogs** | **String** | The profiling error logs. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | The profile properties dictionary. Properties are immutable. |  [optional] |
|**recommendationLatencyInMs** | **Double** | Latency associated with the recommended memory/cpu config |  [optional] |
|**recommendedCpu** | **Double** | The recommended CPU allocation. |  [optional] |
|**recommendedMemoryInGB** | **Double** | The recommended amount of memory to allocate in GB. |  [optional] |
|**state** | **String** | The state of the profile. |  [optional] |



