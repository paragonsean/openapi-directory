

# ListSkusResponse

Response message for `ListSkus`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to retrieve the next page of results. To retrieve the next page, call &#x60;ListSkus&#x60; again with the &#x60;page_token&#x60; field set to this value. This field is empty if there are no more results to retrieve. |  [optional] |
|**skus** | [**List&lt;Sku&gt;**](Sku.md) | The list of public SKUs of the given service. |  [optional] |



