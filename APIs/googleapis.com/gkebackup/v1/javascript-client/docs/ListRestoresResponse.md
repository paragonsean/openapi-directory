# BackupForGkeApi.ListRestoresResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token which may be sent as page_token in a subsequent &#x60;ListRestores&#x60; call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. | [optional] 
**restores** | [**[Restore]**](Restore.md) | The list of Restores matching the given criteria. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


