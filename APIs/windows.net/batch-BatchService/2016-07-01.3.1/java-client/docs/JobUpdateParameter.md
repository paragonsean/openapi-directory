

# JobUpdateParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**constraints** | [**JobConstraints**](JobConstraints.md) |  |  [optional] |
|**metadata** | [**List&lt;MetadataItem&gt;**](MetadataItem.md) | If omitted, it takes the default value of an empty list; in effect, any existing metadata is deleted. |  [optional] |
|**onAllTasksComplete** | [**OnAllTasksCompleteEnum**](#OnAllTasksCompleteEnum) | If omitted, the completion behavior is set to noAction. If the current value is terminateJob, this is an error because a job&#39;s completion behavior may not be changed from terminateJob to noAction. |  [optional] |
|**poolInfo** | [**PoolInformation**](PoolInformation.md) |  |  |
|**priority** | **Integer** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, it is set to the default value 0. |  [optional] |



## Enum: OnAllTasksCompleteEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;noAction&quot; |
| TERMINATE_JOB | &quot;terminateJob&quot; |



