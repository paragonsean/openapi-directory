# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingCalculatepriceRequestItemsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**productCode** | **String** | **unique alphanumeric identifier** of the product the total price for which you which to calculate | [optional] 
**tourGradeCode** | **String** | **alphanumeric identifier** for the tour grade for which to calculate the total price | [optional] 
**travelDate** | **String** | **date** for which to calculate the total price (must be in the future) | [optional] 
**travellers** | [**[BookingCalculatepriceRequestItemsInnerTravellersInner]**](BookingCalculatepriceRequestItemsInnerTravellersInner.md) | **array of objects** detailing the age bands for which to calculate the total price | [optional] 


