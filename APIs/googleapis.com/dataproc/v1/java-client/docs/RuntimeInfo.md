

# RuntimeInfo

Runtime information about workload execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approximateUsage** | [**UsageMetrics**](UsageMetrics.md) |  |  [optional] |
|**currentUsage** | [**UsageSnapshot**](UsageSnapshot.md) |  |  [optional] |
|**diagnosticOutputUri** | **String** | Output only. A URI pointing to the location of the diagnostics tarball. |  [optional] [readonly] |
|**endpoints** | **Map&lt;String, String&gt;** | Output only. Map of remote access endpoints (such as web interfaces and APIs) to their URIs. |  [optional] [readonly] |
|**outputUri** | **String** | Output only. A URI pointing to the location of the stdout and stderr of the workload. |  [optional] [readonly] |



