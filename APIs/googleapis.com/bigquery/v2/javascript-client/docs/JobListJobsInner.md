# BigQueryApi.JobListJobsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**JobConfiguration**](JobConfiguration.md) |  | [optional] 
**errorResult** | [**ErrorProto**](ErrorProto.md) |  | [optional] 
**id** | **String** | Unique opaque ID of the job. | [optional] 
**jobReference** | [**JobReference**](JobReference.md) |  | [optional] 
**kind** | **String** | The resource type. | [optional] 
**principalSubject** | **String** | [Full-projection-only] String representation of identity of requesting party. Populated for both first- and third-party identities. Only present for APIs that support third-party identities. | [optional] 
**state** | **String** | Running state of the job. When the state is DONE, errorResult can be checked to determine whether the job succeeded or failed. | [optional] 
**statistics** | [**JobStatistics**](JobStatistics.md) |  | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**userEmail** | **String** | [Full-projection-only] Email address of the user who ran the job. | [optional] 


