

# PoliciesListResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**header** | [**ResponseHeader**](ResponseHeader.md) |  |  [optional] |
|**kind** | **String** | Type of resource. |  [optional] |
|**nextPageToken** | **String** | The presence of this field indicates that there exist more results following your last page of results in pagination order. To fetch them, make another list request using this value as your page token. This lets you the complete contents of even very large collections one page at a time. However, if the contents of the collection change between the first and last paginated list request, the set of all elements returned are an inconsistent view of the collection. You cannot retrieve a consistent snapshot of a collection larger than the maximum page size. |  [optional] |
|**policies** | [**List&lt;Policy&gt;**](Policy.md) | The policy resources. |  [optional] |



