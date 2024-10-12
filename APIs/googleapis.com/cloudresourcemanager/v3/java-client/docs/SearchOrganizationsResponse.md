

# SearchOrganizationsResponse

The response returned from the `SearchOrganizations` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A pagination token to be used to retrieve the next page of results. If the result is too large to fit within the page size specified in the request, this field will be set with a token that can be used to fetch the next page of results. If this field is empty, it indicates that this response contains the last page of results. |  [optional] |
|**organizations** | [**List&lt;Organization&gt;**](Organization.md) | The list of Organizations that matched the search query, possibly paginated. |  [optional] |



