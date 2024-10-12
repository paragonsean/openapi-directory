# PersonalizedOffers.RedemedOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationDate** | **Date** | Day on which the offer became ready for redemption. | [optional] 
**activationId** | **String** | Distinct identifier for the offer being available for redemption by the user, not intended for end-user display. | [optional] 
**currencyCode** | **String** | ISO 4217 code in which the redeeming transaction must be made to qualify for the offer. | [optional] 
**detailPostpaidCreditOffer** | [**DetailPostpaidCreditOffer**](DetailPostpaidCreditOffer.md) |  | [optional] 
**eventEndDate** | **Date** | Last day that redemption can be made. | [optional] 
**eventStartDate** | **Date** | First day that redemption can be made. | [optional] 
**headline** | **String** | Brief details about the deal. | [optional] 
**language** | **String** | Tongue of offer display text. | [optional] 
**linkoutUrl** | **String** | Deprecated, disregard. | [optional] 
**longDescription** | **String** | Explanation of the deal, typically displayed beneath the headline in a detail view. Often the same as the ShortDescription. | [optional] 
**maxUserRedemptions** | **Number** | The number of times that the cardholder may take advantage of this offer. | [optional] 
**merchant** | [**RedemedOfferMerchant**](RedemedOfferMerchant.md) |  | [optional] 
**offerDisplay** | [**OfferDisplay**](OfferDisplay.md) |  | [optional] 
**offerId** | **String** | System-wide identifier for the campaign, not intended for end-user display. | [optional] 
**offerMedia** | [**OfferMedia**](OfferMedia.md) |  | [optional] 
**offerSource** | **String** | Platform that made the offer available, not intended for end-user display. | [optional] 
**offerType** | **String** | The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase. | [optional] 
**offerUrl** | **String** | Deprecated, disregard. | [optional] 
**redemptionMode** | **String** | Type of credit made upon redemption of the offer- CASH, POINTS, or EITHER. | [optional] 
**redemptionType** | **String** | Where a purchase may be made to qualify for the offer- INSTORE, ONLINE, or ONLINE-INSTORE (either). | [optional] 
**shortDescription** | **String** | Summary of the deal, typically displayed beneath the headline in a list view. | [optional] 
**transactions** | [**Transaction**](Transaction.md) |  | [optional] 


