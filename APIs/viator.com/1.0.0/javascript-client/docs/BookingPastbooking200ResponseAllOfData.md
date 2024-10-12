# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingPastbooking200ResponseAllOfData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookerEmail** | **String** | **email address** of the entity that booked the tour | [optional] 
**bookingDate** | **String** | **date** on which the booking was made | [optional] 
**bookingStatus** | [**BookingStatusItinerary**](BookingStatusItinerary.md) |  | [optional] 
**currencyCode** | **String** | **currency code** for the currency in which pricing is displayed | [optional] 
**distributorRef** | **String** | **reference code** for the distributor | [optional] 
**exchangeRate** | **Number** | ignore (Viator only) | [optional] 
**hasVoucher** | **Boolean** | **indicator**: &#x60;true&#x60; if a voucher exists | [optional] 
**itemSummaries** | [**[BookingPastbooking200ResponseAllOfDataItemSummariesInner]**](BookingPastbooking200ResponseAllOfDataItemSummariesInner.md) | **array** of item summary objects | [optional] 
**itineraryId** | **Number** | ignore (Viator only) | [optional] 
**rulesApplied** | **String** | ignore (Viator only) | [optional] 
**sortOrder** | **Number** | **sort order** for *this* result | [optional] 
**totalPrice** | **Number** | **numeric merchant total price** for *this* booking - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  | [optional] 
**totalPriceFormatted** | **String** | **currency-formatted merchant total price** for *this* booking - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  | [optional] 
**totalPriceUSD** | **Number** | **numeric merchant total price** of this booking in USD | [optional] 
**userId** | **String** | ignore (Viator only) | [optional] 
**voucherKey** | **String** | Unique reference for the voucher for this booking that can be used as a request parameter to search for existing bookings using the [/booking/mybookings](#operation/bookingMybookings) and [/booking/pastbooking](#operation/bookingPastbooking) endpoints | [optional] 
**voucherURL** | **String** | **URL of the voucher** for *this* product (if available). The customer can access this URL to retrieve their voucher. | [optional] 


