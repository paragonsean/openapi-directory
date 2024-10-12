

# CreateRunGroupRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | A name for the group. |  [optional] |
|**maxCpus** | **Integer** | The maximum number of CPUs to use in the group. |  [optional] |
|**maxRuns** | **Integer** | The maximum number of concurrent runs for the group. |  [optional] |
|**maxDuration** | **Integer** | A maximum run time for the group in minutes. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Tags for the group. |  [optional] |
|**requestId** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique ID for each request. |  |
|**maxGpus** | **Integer** |  The maximum GPUs that can be used by a run group.  |  [optional] |



