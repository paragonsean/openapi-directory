

# Status

Gets or sets the object containing the job status information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cleanupProgress** | **Double** | The progress made on the cleanup. |  [optional] |
|**failureInfo** | **String** | The information about any failures that have occurred. |  [optional] |
|**finishTime** | **Long** | The time at which the job completed. It is an integer in milliseconds, as a Unix timestamp relative to 1/1/1970 00:00:00. |  [optional] |
|**historyFile** | **String** | The history file of the job. |  [optional] |
|**jobACLs** | **Object** | The object containing the job ACLs. |  [optional] |
|**jobComplete** | **Boolean** | Whether or not the job has completed. |  [optional] |
|**jobFile** | **String** | The job configuration file. |  [optional] |
|**jobID** | [**JobID**](JobID.md) |  |  [optional] |
|**jobId** | **String** | The full ID of the job. |  [optional] |
|**jobName** | **String** | The user-specified job name. |  [optional] |
|**jobPriority** | **String** | The priority of the job. |  [optional] |
|**mapProgress** | **Double** | The progress made on the maps. |  [optional] |
|**neededMem** | **Long** | The amount of memory needed for the job. |  [optional] |
|**numReservedSlots** | **Integer** | The number of slots reserved. |  [optional] |
|**numUsedSlots** | **Integer** | The number of slots used for the job. |  [optional] |
|**priority** | **String** | The priority of the job. |  [optional] |
|**queue** | **String** | The job queue name. |  [optional] |
|**reduceProgress** | **Double** | The progress made on the reduces. |  [optional] |
|**reservedMem** | **Long** | The amount of memory reserved for the job. |  [optional] |
|**retired** | **Boolean** | Whether or not the job has been retired.  |  [optional] |
|**runState** | **Integer** | The current state of the job. |  [optional] |
|**schedulingInfo** | **String** | The information about the scheduling of the job. |  [optional] |
|**setupProgress** | **Double** | The progress made on the setup. |  [optional] |
|**startTime** | **Long** | The time at which the job started. It is an integer in milliseconds, as a Unix timestamp relative to 1/1/1970 00:00:00. |  [optional] |
|**state** | **String** | The state of the job. |  [optional] |
|**trackingUrl** | **String** | The link to the web-ui for details of the job. |  [optional] |
|**uber** | **Boolean** | Whether job running in uber mode. |  [optional] |
|**usedMem** | **Long** | The amount of memory used by the job. |  [optional] |
|**username** | **String** | The userid of the person who submitted the job. |  [optional] |



