# BatchService.JobPatchParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**JobConstraints**](JobConstraints.md) |  | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | If omitted, the existing Job metadata is left unchanged. | [optional] 
**onAllTasksComplete** | [**OnAllTasksComplete**](OnAllTasksComplete.md) |  | [optional] 
**poolInfo** | [**PoolInformation**](PoolInformation.md) |  | [optional] 
**priority** | **Number** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, the priority of the Job is left unchanged. | [optional] 


