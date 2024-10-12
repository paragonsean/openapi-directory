# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingStatusItemsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingDateFrom** | **String** | **earliest date** for when the booking(s) in question were made (must be in the future) | [optional] 
**bookingDateTo** | **String** | **latest date** for when the booking(s) in question were made (must be in the future) | [optional] 
**distributorItemRefs** | **[String]** | **array** of partner-defined distributor item reference identifiers e.g. &#x60;[&#39;refItem1&#39;,&#39;refItem2&#39;,&#39;refItem3&#39;]&#x60; | [optional] 
**distributorRefs** | **[String]** | **array** of partner-defined distributor reference identifiers | [optional] 
**itemIds** | **[Number]** | **array** of booking-reference numbers to check   &#x60;itemId&#x60; (booking-reference provided by Viator). For more information, see [Booking references](#section/Key-concepts/Booking-references)  | [optional] 
**leadFirstName** | **String** | **first name** of the lead traveler | [optional] 
**leadSurname** | **String** | **surname** of the lead traveler | [optional] 
**test** | **Boolean** | **specifier**: - &#x60;true&#x60;: bypass the poll limit in the prelive environment only - &#x60;false&#x60;: (default) make a *real* booking, not a test  | [optional] 


