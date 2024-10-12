

# DestinyVendorsDestinyVendorReceipt

If a character purchased an item that is refundable, a Vendor Receipt will be created on the user's Destiny Profile. These expire after a configurable period of time, but until then can be used to get refunds on items. BNet does not provide the ability to refund a purchase *yet*, but you know.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyPaid** | [**List&lt;DestinyDestinyItemQuantity&gt;**](DestinyDestinyItemQuantity.md) | The amount paid for the item, in terms of items that were consumed in the purchase and their quantity. |  [optional] |
|**expiresOn** | **OffsetDateTime** | The date at which this receipt is rendered invalid. |  [optional] |
|**itemReceived** | [**DestinyDestinyItemQuantity**](DestinyDestinyItemQuantity.md) | The item that was received, and its quantity. |  [optional] |
|**licenseUnlockHash** | **Integer** | The unlock flag used to determine whether you still have the purchased item. |  [optional] |
|**purchasedByCharacterId** | **Long** | The ID of the character who made the purchase. |  [optional] |
|**refundPolicy** | **Integer** | Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details. |  [optional] |
|**sequenceNumber** | **Integer** | The identifier of this receipt. |  [optional] |
|**timeToExpiration** | **Long** | The seconds since epoch at which this receipt is rendered invalid. |  [optional] |



