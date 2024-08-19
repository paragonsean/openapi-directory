# PersonalizedOffers.MatchedOffer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeSc** | **String** | ACTIVATED_STATEMENT_CREDIT- ready for redemption by the user. AVAILABLE- requires call to Activate Statement Credit Offer to make ready for redemption. | [optional] 
**currencyCode** | **String** | ISO 4217 code in which the redeeming transaction must be made to qualify for the offer. | [optional] 
**discount** | **String** | The markdown represented by the offer, in absolute value or percentage. | [optional] 
**discountType** | **String** | The kind of markdown represented by the offer. ABSOLUTE- fixed amount. PERCENTAGE- share of purchase. | [optional] 
**eventEndDate** | **Date** | Last day that redemption can be made. | [optional] 
**eventStartDate** | **Date** | First day that redemption can be made by any user, may not apply to the specified user. | [optional] 
**headline** | **String** | Brief details about the deal. | [optional] 
**language** | **String** | Tongue of offer display text. | [optional] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**merchantImageURL** | **String** | Square picture of the retailer logo. | [optional] 
**offerId** | **String** | System-wide identifier for the campaign, not intended for end-user display. | [optional] 
**offerSource** | **String** | Platform that made the offer available, not intended for end-user display. | [optional] 
**offerType** | **String** | The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase. | [optional] 
**price** | **String** | Reserved for future use. | [optional] 
**redemptionMode** | **String** | Type of credit made upon redemption of the offer- CASH, POINTS, or EITHER. | [optional] 
**shortDescription** | **String** | Summary of the deal, typically displayed beneath the headline in a list view. | [optional] 


