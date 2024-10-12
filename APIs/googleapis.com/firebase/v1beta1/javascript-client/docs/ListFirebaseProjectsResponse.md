# FirebaseManagementApi.ListFirebaseProjectsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent calls to &#x60;ListFirebaseProjects&#x60; to find the next group of Projects. Page tokens are short-lived and should not be persisted. | [optional] 
**results** | [**[FirebaseProject]**](FirebaseProject.md) | One page of the list of Projects that are accessible to the caller. | [optional] 


