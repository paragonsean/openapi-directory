

# ListTagBindingsResponse

The ListTagBindings response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Pagination token. If the result set is too large to fit in a single response, this token is returned. It encodes the position of the current result cursor. Feeding this value into a new list request with the &#x60;page_token&#x60; parameter gives the next page of the results. When &#x60;next_page_token&#x60; is not filled in, there is no next page and the list returned is the last page in the result set. Pagination tokens have a limited lifetime. |  [optional] |
|**tagBindings** | [**List&lt;TagBinding&gt;**](TagBinding.md) | A possibly paginated list of TagBindings for the specified resource. |  [optional] |



