# PeopleApi.ListConnectionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**[Person]**](Person.md) | The list of people that the requestor is connected to. | [optional] 
**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**nextSyncToken** | **String** | A token, which can be sent as &#x60;sync_token&#x60; to retrieve changes since the last request. Request must set &#x60;request_sync_token&#x60; to return the sync token. When the response is paginated, only the last page will contain &#x60;nextSyncToken&#x60;. | [optional] 
**totalItems** | **Number** | The total number of items in the list without pagination. | [optional] 
**totalPeople** | **Number** | **DEPRECATED** (Please use totalItems) The total number of people in the list without pagination. | [optional] 


