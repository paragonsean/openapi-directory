

# JobPatchParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | If omitted, the existing job metadata is left unchanged. |  [optional] |
|**onAllTasksComplete** | [**OnAllTasksCompleteEnum**](#OnAllTasksCompleteEnum) | If omitted, the completion behavior is left unchanged. You may not change the value from terminateJob to noAction – that is, once you have engaged automatic job termination, you cannot turn it off again. If you try to do this, the request fails with an &#39;invalid property value&#39; error response; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  [optional] |
|**priority** | **Integer** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, the priority of the job is left unchanged. |  [optional] |



## Enum: OnAllTasksCompleteEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;noAction&quot; |
| TERMINATE_JOB | &quot;terminateJob&quot; |



