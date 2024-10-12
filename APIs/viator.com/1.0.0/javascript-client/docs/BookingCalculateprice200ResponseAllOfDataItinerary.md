# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingCalculateprice200ResponseAllOfDataItinerary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookerEmail** | **String** | ignore (Viator only) | [optional] 
**bookingDate** | **String** | **date** of *this* booking | [optional] 
**bookingStatus** | [**BookingStatusItinerary**](BookingStatusItinerary.md) |  | [optional] 
**currencyCode** | **String** | **specifier** of the currency in which pricing details are displayed | [optional] 
**distributorRef** | **String** | ignore (Viator only) | [optional] 
**exchangeRate** | **Number** | ignore (Viator only) | [optional] 
**hasVoucher** | **Boolean** | ignore (Viator only) | [optional] 
**itemSummaries** | [**[BookingCalculateprice200ResponseAllOfDataItineraryItemSummariesInner]**](BookingCalculateprice200ResponseAllOfDataItineraryItemSummariesInner.md) | **array** of item summaries | [optional] 
**itineraryId** | **Number** | **numeric identifier** for *this* order | [optional] 
**omniPreRuleList** | **Number** | ignore (Viator only) | [optional] 
**paypalRedirectURL** | **String** | ignore (Viator only) | [optional] 
**rulesApplied** | **[String]** | ignore (Viator only) | [optional] 
**securityToken** | **String** | ignore (Viator only) | [optional] 
**sortOrder** | **Number** | **sort order** for *this* itinerary | [optional] 
**totalPrice** | **Number** | **numeric total price (total)** for *this* order - For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  | [optional] 
**totalPriceFormatted** | **String** | **currency-formatted total price (including transaction fee)** for *this* order - For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  | [optional] 
**totalPriceUSD** | **Number** | **numeric total price** of *this* order in USD | [optional] 
**userId** | **Number** | ignore (Viator only) | [optional] 
**voucherKey** | **String** | Unique reference for the voucher for this booking that can be used as a request parameter to search for existing bookings using the [/booking/mybookings](#operation/bookingMybookings) and [/booking/pastbooking](#operation/bookingPastbooking) endpoints | [optional] 
**voucherURL** | **String** | **URL of the voucher** for *this* product (if available). The customer can access this URL to retrieve their voucher. | [optional] 


