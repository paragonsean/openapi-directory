# PeopleApi.ListDirectoryPeopleResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**nextSyncToken** | **String** | A token, which can be sent as &#x60;sync_token&#x60; to retrieve changes since the last request. Request must set &#x60;request_sync_token&#x60; to return the sync token. | [optional] 
**people** | [**[Person]**](Person.md) | The list of people in the domain directory. | [optional] 


