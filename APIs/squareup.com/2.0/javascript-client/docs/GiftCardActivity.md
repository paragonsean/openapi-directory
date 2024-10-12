# SquareConnectApi.GiftCardActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activateActivityDetails** | [**GiftCardActivityActivate**](GiftCardActivityActivate.md) |  | [optional] 
**adjustDecrementActivityDetails** | [**GiftCardActivityAdjustDecrement**](GiftCardActivityAdjustDecrement.md) |  | [optional] 
**adjustIncrementActivityDetails** | [**GiftCardActivityAdjustIncrement**](GiftCardActivityAdjustIncrement.md) |  | [optional] 
**blockActivityDetails** | [**GiftCardActivityBlock**](GiftCardActivityBlock.md) |  | [optional] 
**clearBalanceActivityDetails** | [**GiftCardActivityClearBalance**](GiftCardActivityClearBalance.md) |  | [optional] 
**createdAt** | **String** | The timestamp when the gift card activity was created, in RFC 3339 format. | [optional] 
**deactivateActivityDetails** | [**GiftCardActivityDeactivate**](GiftCardActivityDeactivate.md) |  | [optional] 
**giftCardBalanceMoney** | [**Money**](Money.md) |  | [optional] 
**giftCardGan** | **String** | The gift card GAN. The GAN is not required if &#x60;gift_card_id&#x60; is present. | [optional] 
**giftCardId** | **String** | The gift card ID. The ID is not required if a GAN is present. | [optional] 
**id** | **String** | The unique ID of the gift card activity. | [optional] 
**importActivityDetails** | [**GiftCardActivityImport**](GiftCardActivityImport.md) |  | [optional] 
**importReversalActivityDetails** | [**GiftCardActivityImportReversal**](GiftCardActivityImportReversal.md) |  | [optional] 
**loadActivityDetails** | [**GiftCardActivityLoad**](GiftCardActivityLoad.md) |  | [optional] 
**locationId** | **String** | The ID of the location at which the activity occurred. | 
**redeemActivityDetails** | [**GiftCardActivityRedeem**](GiftCardActivityRedeem.md) |  | [optional] 
**refundActivityDetails** | [**GiftCardActivityRefund**](GiftCardActivityRefund.md) |  | [optional] 
**type** | **Object** |  | 
**unblockActivityDetails** | [**GiftCardActivityUnblock**](GiftCardActivityUnblock.md) |  | [optional] 
**unlinkedActivityRefundActivityDetails** | [**GiftCardActivityUnlinkedActivityRefund**](GiftCardActivityUnlinkedActivityRefund.md) |  | [optional] 


