# CodeScanApi.NewJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisMode** | **String** | When set to preview, analysis is not added to the database | [optional] 
**commitOverride** | **String** | When the project is based on git, the git commit that this job should run. Leave blank to use the project&#39;s default | [optional] 
**emailReportTo** | **String** | List of usernames to email the report to | [optional] 
**projectBranch** | **String** | he project branch that this job is evaluating | [optional] 
**projectKey** | **String** | The key of the project to start | 
**version** | **String** | Use this as the analysis&#39; version. On success the Project&#39;s default version will be set to this | [optional] 


