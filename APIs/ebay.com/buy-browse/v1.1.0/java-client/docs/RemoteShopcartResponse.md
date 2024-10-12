

# RemoteShopcartResponse

The type that defines the fields and containers for the member's eBay cart information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cartItems** | [**List&lt;CartItem&gt;**](CartItem.md) | An array of the items in the member&#39;s eBay cart. |  [optional] |
|**cartSubtotal** | [**Amount**](Amount.md) |  |  [optional] |
|**cartWebUrl** | **String** | The URL of the member&#39;s eBay cart. |  [optional] |
|**unavailableCartItems** | [**List&lt;CartItem&gt;**](CartItem.md) | An array of items in the cart that are unavailable. This can be for a variety of reasons such as, when the listing has ended or the item is out of stock. Because a cart never expires, these items will remain in the cart until they are removed. |  [optional] |
|**warnings** | [**List&lt;Error&gt;**](Error.md) | An array of warning messages. These type of errors do not prevent the call from executing but should be checked. |  [optional] |



