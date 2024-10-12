# BitbucketApi.PipelineSchedulePostRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cronPattern** | **String** | The cron expression with second precision (7 fields) that the schedule applies. For example, for expression: 0 0 12 * * ? *, will execute at 12pm UTC every day. | 
**enabled** | **Boolean** | Whether the schedule is enabled. | [optional] 
**target** | [**RequestBodyForPipelineSchedulePOSTRequestTarget**](RequestBodyForPipelineSchedulePOSTRequestTarget.md) |  | 


