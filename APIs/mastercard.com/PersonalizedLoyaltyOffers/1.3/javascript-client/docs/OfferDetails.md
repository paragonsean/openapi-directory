# PersonalizedOffers.OfferDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currencyCode** | **String** | ISO 4217 code in which the redeeming transaction must be made to qualify for the offer. | [optional] 
**detailPostpaidCreditOffer** | [**DetailPostpaidCreditOffer**](DetailPostpaidCreditOffer.md) |  | [optional] 
**eventEndDate** | **Date** | Last day that redemption can be made. | [optional] 
**eventStartDate** | **Date** | First day that redemption can be made by any user, may not apply to the specified user. | [optional] 
**headline** | **String** | Brief details about the deal. | [optional] 
**language** | **String** | Tongue of offer display text. | [optional] 
**linkOut** | **Object** | Deprecated. | [optional] 
**longDescription** | **String** | Explanation of the deal, typically displayed beneath the headline in a detail view. Often the same as the ShortDescription. | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**offerDisplay** | [**OfferDisplay**](OfferDisplay.md) |  | [optional] 
**offerId** | **String** | System-wide identifier for the campaign, not intended for end-user display. | [optional] 
**offerMedia** | [**OfferMedia**](OfferMedia.md) |  | [optional] 
**offerSource** | **String** | Platform that made the offer available, not intended for end-user display. | [optional] 
**offerType** | **String** | The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase. | [optional] 
**offerUrl** | **Object** | Deprecated. | [optional] 
**redemptionMode** | **String** | Type of credit made upon redemption of the offer- CASH, POINTS, or EITHER. | [optional] 
**redemptionType** | **String** | Where a purchase may be made to qualify for the offer- INSTORE, ONLINE, or ONLINE-INSTORE (either). | [optional] 
**shortDescription** | **String** | Summary of the deal, typically displayed beneath the headline in a list view. | [optional] 


