# FirebaseManagementApi.ListAvailableLocationsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**[Location]**](Location.md) | One page of results from a call to &#x60;ListAvailableLocations&#x60;. | [optional] 
**nextPageToken** | **String** | If the result list is too large to fit in a single response, then a token is returned. If the string is empty, then this response is the last page of results and all available locations have been listed. This token can be used in a subsequent call to &#x60;ListAvailableLocations&#x60; to find more locations. Page tokens are short-lived and should not be persisted. | [optional] 


