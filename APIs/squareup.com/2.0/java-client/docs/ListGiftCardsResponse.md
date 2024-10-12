

# ListGiftCardsResponse

A response that contains one or more `GiftCard`. The response might contain a set of `Error` objects if the request resulted in errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | When a response is truncated, it includes a cursor that you can use in a subsequent request to fetch the next set of gift cards. If empty, this is the final response. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Any errors that occurred during the request. |  [optional] |
|**giftCards** | [**List&lt;GiftCard&gt;**](GiftCard.md) | Gift cards retrieved. |  [optional] |



