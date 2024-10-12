# BatchService.TaskDependencies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taskIdRanges** | [**[TaskIdRange]**](TaskIdRange.md) |  | [optional] 
**taskIds** | **[String]** | The taskIds collection is limited to 64000 characters total (i.e. the combined length of all Task IDs). If the taskIds collection exceeds the maximum length, the Add Task request fails with error code TaskDependencyListTooLong. In this case consider using Task ID ranges instead. | [optional] 


