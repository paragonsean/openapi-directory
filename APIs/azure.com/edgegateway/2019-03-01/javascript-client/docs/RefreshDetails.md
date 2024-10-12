# DataBoxEdgeManagementClient.RefreshDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorManifestFile** | **String** | Indicates the relative path of the error xml for the last refresh job on this particular share, if any. This could be a failed job or a successful job. | [optional] 
**inProgressRefreshJobId** | **String** | If a refresh share job is currently in progress on this share, this field indicates the ARM resource ID of that job. The field is empty if no job is in progress. | [optional] 
**lastCompletedRefreshJobTimeInUTC** | **Date** | Indicates the completed time for the last refresh job on this particular share, if any.This could be a failed job or a successful job. | [optional] 
**lastJob** | **String** | Indicates the id of the last refresh job on this particular share,if any. This could be a failed job or a successful job. | [optional] 


