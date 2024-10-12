

# CartItem

The type that defines the fields for the individual items in a cart.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cartItemId** | **String** | The identifier for the item being added to the cart. This is generated when the item is added to the cart. |  [optional] |
|**cartItemSubtotal** | [**Amount**](Amount.md) |  |  [optional] |
|**image** | [**Image**](Image.md) |  |  [optional] |
|**itemId** | **String** | The RESTful identifier of the item. This identifier is generated when the item was listed. RESTful Item ID Format: v1|#|# For example: v1|272394640372|0 v1|162846450672|461882996982 |  [optional] |
|**itemWebUrl** | **String** | The URL of the eBay view item page for the item. |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**quantity** | **Integer** | The number of this item the buyer wants to purchase. |  [optional] |
|**title** | **String** | The title of the item. This can be written by the seller or come from the eBay product catalog. |  [optional] |



