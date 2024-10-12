# CloudDnsApi.ResourceRecordSetsListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**ResponseHeader**](ResponseHeader.md) |  | [optional] 
**kind** | **String** | Type of resource. | [optional] [default to &#39;dns#resourceRecordSetsListResponse&#39;]
**nextPageToken** | **String** | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your pagination token. This lets you retrieve the complete contents of even larger collections, one page at a time. However, if the collection changes between paginated list requests, the set of elements returned is an inconsistent view of the collection. You cannot retrieve a consistent snapshot of a collection larger than the maximum page size. | [optional] 
**rrsets** | [**[ResourceRecordSet]**](ResourceRecordSet.md) | The resource record set resources. | [optional] 


