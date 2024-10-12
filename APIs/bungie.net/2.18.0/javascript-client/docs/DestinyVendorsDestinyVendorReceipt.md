# BungieNetApi.DestinyVendorsDestinyVendorReceipt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyPaid** | [**[DestinyDestinyItemQuantity]**](DestinyDestinyItemQuantity.md) | The amount paid for the item, in terms of items that were consumed in the purchase and their quantity. | [optional] 
**expiresOn** | **Date** | The date at which this receipt is rendered invalid. | [optional] 
**itemReceived** | [**DestinyDestinyItemQuantity**](DestinyDestinyItemQuantity.md) | The item that was received, and its quantity. | [optional] 
**licenseUnlockHash** | **Number** | The unlock flag used to determine whether you still have the purchased item. | [optional] 
**purchasedByCharacterId** | **Number** | The ID of the character who made the purchase. | [optional] 
**refundPolicy** | **Number** | Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details. | [optional] 
**sequenceNumber** | **Number** | The identifier of this receipt. | [optional] 
**timeToExpiration** | **Number** | The seconds since epoch at which this receipt is rendered invalid. | [optional] 


