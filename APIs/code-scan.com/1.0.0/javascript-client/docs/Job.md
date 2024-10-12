# CodeScanApi.Job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **String** | Quality Gate status of a completed job | [optional] 
**alertDescription** | **String** | Quality Gate errors of a completed job | [optional] 
**analysisMode** | **String** | When set to preview, analysis is not added to the database | [optional] 
**commit** | **String** | The git commit that this job is evaluating | [optional] 
**created** | **String** | DateTime that this job was queued | [optional] 
**emailReportTo** | **String** | List of usernames to email the report to | [optional] 
**finished** | **String** | If the job has finished, then the datetime that the job finished processing | [optional] 
**jobId** | **String** | The jobId of this job | [optional] 
**projectBranch** | **String** | The project branch that this job is evaluating | [optional] 
**projectKey** | **String** | The projectKey that this job is running | [optional] 
**started** | **String** | If the job has started, then the datetime that the job started processing | [optional] 
**status** | **String** | The status of the job | [optional] 
**url** | **String** | The url to view the output report | [optional] 
**version** | **String** | The project version that this job is evaluating | [optional] 
**warnings** | **String** | When creating a new job, any warnings will be listed here. | [optional] 


