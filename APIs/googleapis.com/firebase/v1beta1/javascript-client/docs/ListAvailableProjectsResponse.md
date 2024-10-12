# FirebaseManagementApi.ListAvailableProjectsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent calls to &#x60;ListAvailableProjects&#x60; to find the next group of Projects. Page tokens are short-lived and should not be persisted. | [optional] 
**projectInfo** | [**[ProjectInfo]**](ProjectInfo.md) | The list of GCP &#x60;Projects&#x60; which can have Firebase resources added to them. | [optional] 


