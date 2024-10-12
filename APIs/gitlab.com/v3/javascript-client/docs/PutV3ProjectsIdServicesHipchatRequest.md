# Gitlab.PutV3ProjectsIdServicesHipchatRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **String** | The room token | 
**room** | **String** | The room name or ID | [optional] 
**color** | **String** | The room color | [optional] 
**notify** | **Boolean** | Enable notifications | [optional] 
**apiVersion** | **String** | Leave blank for default (v2) | [optional] 
**server** | **String** | Leave blank for default. https://hipchat.example.com | [optional] 
**pushEvents** | **String** | Event will be triggered by a push to the repository | [optional] 
**issueEvents** | **String** | Event will be triggered when an issue is created/updated/closed | [optional] 
**confidentialIssueEvents** | **String** | Event will be triggered when a confidential issue is created/updated/closed | [optional] 
**mergeRequestEvents** | **String** | Event will be triggered when a merge request is created/updated/merged | [optional] 
**noteEvents** | **String** | Event will be triggered when someone adds a comment | [optional] 
**tagPushEvents** | **String** | Event will be triggered when a new tag is pushed to the repository | [optional] 
**buildEvents** | **String** | Event will be triggered when a build status changes | [optional] 


