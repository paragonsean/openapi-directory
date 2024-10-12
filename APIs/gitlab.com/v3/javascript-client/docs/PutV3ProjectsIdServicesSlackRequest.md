# Gitlab.PutV3ProjectsIdServicesSlackRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook** | **String** | The Slack webhook. e.g. https://hooks.slack.com/services/... | 
**newIssueUrl** | **String** | The user name | [optional] 
**channel** | **String** | The channel name | [optional] 
**pushEvents** | **String** | Event will be triggered by a push to the repository | [optional] 
**issueEvents** | **String** | Event will be triggered when an issue is created/updated/closed | [optional] 
**confidentialIssueEvents** | **String** | Event will be triggered when a confidential issue is created/updated/closed | [optional] 
**mergeRequestEvents** | **String** | Event will be triggered when a merge request is created/updated/merged | [optional] 
**noteEvents** | **String** | Event will be triggered when someone adds a comment | [optional] 
**tagPushEvents** | **String** | Event will be triggered when a new tag is pushed to the repository | [optional] 
**buildEvents** | **String** | Event will be triggered when a build status changes | [optional] 
**pipelineEvents** | **String** |  | [optional] 
**wikiPageEvents** | **String** | Event will be triggered when a wiki page is created/updated | [optional] 


