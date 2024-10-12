# FirebaseManagementApi.ListWebAppsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**[WebApp]**](WebApp.md) | List of each &#x60;WebApp&#x60; associated with the specified &#x60;FirebaseProject&#x60;. | [optional] 
**nextPageToken** | **String** | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results. This token can be used in a subsequent call to &#x60;ListWebApps&#x60; to find the next group of Apps. Page tokens are short-lived and should not be persisted. | [optional] 


