# BatchService.JobPatchParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**JobConstraints**](JobConstraints.md) |  | [optional] 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | Sets a list of name-value pairs associated with the job as metadata. If omitted, the existing job metadata is left unchanged. | [optional] 
**poolInfo** | [**PoolInformation**](PoolInformation.md) |  | [optional] 
**priority** | **Number** | Sets the priority of the job. Priority values can range from -1000 to 1000, with -1000 being the lowest priority and 1000 being the highest priority. If omitted, the priority of the job is left unchanged. | [optional] 


