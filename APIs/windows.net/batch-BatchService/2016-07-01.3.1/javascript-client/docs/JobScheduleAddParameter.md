# BatchService.JobScheduleAddParameter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024. | [optional] 
**id** | **String** | The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The id is case-preserving and case-insensitive (that is, you may not have two ids within an account that differ only by case). | 
**jobSpecification** | [**JobSpecification**](JobSpecification.md) |  | 
**metadata** | [**[MetadataItem]**](MetadataItem.md) | The Batch service does not assign any meaning to metadata; it is solely for the use of user code. | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | 


