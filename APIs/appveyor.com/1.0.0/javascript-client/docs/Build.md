# AppVeyorRestApi.Build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **String** |  | [optional] 
**buildId** | **Number** |  | [optional] 
**message** | **String** |  | [optional] 
**version** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**updated** | **Date** |  | [optional] [readonly] 
**authorName** | **String** |  | [optional] 
**authorUsername** | **String** |  | [optional] 
**buildNumber** | **Number** |  | [optional] 
**commitId** | **String** |  | [optional] 
**committed** | **Date** |  | [optional] 
**committerName** | **String** |  | [optional] 
**committerUsername** | **String** |  | [optional] 
**finished** | **Date** |  | [optional] 
**isTag** | **Boolean** |  | [optional] 
**jobs** | [**[BuildJob]**](BuildJob.md) | Always empty in getProjectHistory and startDeployment responses. | [optional] 
**messageExtended** | **String** |  | [optional] 
**messages** | [**[BuildMessage]**](BuildMessage.md) |  | [optional] 
**projectId** | **Number** |  | [optional] 
**pullRequestId** | **Number** |  | [optional] 
**pullRequestName** | **String** |  | [optional] 
**started** | **Date** |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 


