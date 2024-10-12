# RubrikRestApi.InternalJobInstanceDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **Boolean** | Whether this job instance has been archived. | 
**childJobDebugInfo** | **String** | Some job types create other &#39;child&#39; jobs to perform their work. Here we show information on how this job is being affected by its child jobs (if any). | [optional] 
**endTime** | **String** | End time of the job instance. | [optional] 
**errorInfo** | **String** | Error information of the job instance. | [optional] 
**id** | **String** | ID of the instance. | 
**isDisabled** | **Boolean** | Whether this job is disabled or not. | 
**jobProgress** | **Number** | The current progress in terms of percentage of the async request. | [optional] 
**jobType** | **String** | Type of the job. | 
**nodeId** | **String** | ID of the node where the job runs. | 
**result** | **String** | Result of the job instance. Its meaning depends on the job type but is usually an ID. | [optional] 
**startTime** | **String** | Start time of the job instance. | [optional] 
**status** | **String** | Status of the job instance. | 


