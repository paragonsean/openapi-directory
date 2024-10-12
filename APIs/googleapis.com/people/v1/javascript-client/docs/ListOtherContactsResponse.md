# PeopleApi.ListOtherContactsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**nextSyncToken** | **String** | A token, which can be sent as &#x60;sync_token&#x60; to retrieve changes since the last request. Request must set &#x60;request_sync_token&#x60; to return the sync token. | [optional] 
**otherContacts** | [**[Person]**](Person.md) | The list of \&quot;Other contacts\&quot; returned as Person resources. \&quot;Other contacts\&quot; support a limited subset of fields. See ListOtherContactsRequest.request_mask for more detailed information. | [optional] 
**totalSize** | **Number** | The total number of other contacts in the list without pagination. | [optional] 


