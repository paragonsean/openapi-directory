# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingBookRequestPartnerDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distributorRef** | **String** | **unique alphanumeric reference code** for the distributor - Merchant API partners must pass a &#x60;distributorRef&#x60; at the order (A.K.A. &#39;itinerary&#39;) level in the &#x60;partnerDetail&#x60; object. The &#x60;distributorRef&#x60; passed must be alphanumeric and unique to bookings made by the merchant. - Passing an existing &#x60;distributorRef&#x60;: If an existing &#x60;distributorRef&#x60; is passed, the booking with the matching &#x60;distributorRef&#x60; will be returned in the response and a new booking will not be made. The fields in the response are identical to the response for a new booking.  | [optional] 


