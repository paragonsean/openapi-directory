

# ListFederationsResponse

Response message for ListFederations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**federations** | [**List&lt;Federation&gt;**](Federation.md) | The services in the specified location. |  [optional] |
|**nextPageToken** | **String** | A token that can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



