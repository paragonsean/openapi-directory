# CloudDnsApi.ChangesListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**[Change]**](Change.md) | The requested changes. | [optional] 
**header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**kind** | **String** | Type of resource. | [optional] [default to &#39;dns#changesListResponse&#39;]
**nextPageToken** | **String** | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your pagination token. This lets you retrieve the complete contents of even very large collections one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You cannot retrieve a \&quot;snapshot\&quot; of collections larger than the maximum page size. | [optional] 


