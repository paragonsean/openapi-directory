# BatchService.JobUpdateParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**JobConstraints**](JobConstraints.md) |  | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | If omitted, it takes the default value of an empty list; in effect, any existing metadata is deleted. | [optional] 
**onAllTasksComplete** | [**OnAllTasksComplete**](OnAllTasksComplete.md) |  | [optional] 
**poolInfo** | [**PoolInformation**](PoolInformation.md) |  | 
**priority** | **Number** | Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, it is set to the default value 0. | [optional] 


