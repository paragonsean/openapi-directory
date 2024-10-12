

# ListTagValuesResponse

The ListTagValues response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A pagination token returned from a previous call to &#x60;ListTagValues&#x60; that indicates from where listing should continue. This is currently not used, but the server may at any point start supplying a valid token. |  [optional] |
|**tagValues** | [**List&lt;TagValue&gt;**](TagValue.md) | A possibly paginated list of TagValues that are direct descendants of the specified parent TagKey. |  [optional] |



