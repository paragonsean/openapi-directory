# FirebaseManagementApi.ListIosAppsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**[IosApp]**](IosApp.md) | List of each &#x60;IosApp&#x60; associated with the specified &#x60;FirebaseProject&#x60;. | [optional] 
**nextPageToken** | **String** | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent call to &#x60;ListIosApps&#x60; to find the next group of Apps. Page tokens are short-lived and should not be persisted. | [optional] 


