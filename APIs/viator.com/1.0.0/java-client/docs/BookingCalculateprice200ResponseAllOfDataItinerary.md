

# BookingCalculateprice200ResponseAllOfDataItinerary

**summary results** for all itinerary items

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookerEmail** | **String** | ignore (Viator only) |  [optional] |
|**bookingDate** | **String** | **date** of *this* booking |  [optional] |
|**bookingStatus** | [**BookingStatusItinerary**](BookingStatusItinerary.md) |  |  [optional] |
|**currencyCode** | **String** | **specifier** of the currency in which pricing details are displayed |  [optional] |
|**distributorRef** | **String** | ignore (Viator only) |  [optional] |
|**exchangeRate** | **Integer** | ignore (Viator only) |  [optional] |
|**hasVoucher** | **Boolean** | ignore (Viator only) |  [optional] |
|**itemSummaries** | [**List&lt;BookingCalculateprice200ResponseAllOfDataItineraryItemSummariesInner&gt;**](BookingCalculateprice200ResponseAllOfDataItineraryItemSummariesInner.md) | **array** of item summaries |  [optional] |
|**itineraryId** | **Integer** | **numeric identifier** for *this* order |  [optional] |
|**omniPreRuleList** | **Integer** | ignore (Viator only) |  [optional] |
|**paypalRedirectURL** | **String** | ignore (Viator only) |  [optional] |
|**rulesApplied** | **List&lt;String&gt;** | ignore (Viator only) |  [optional] |
|**securityToken** | **String** | ignore (Viator only) |  [optional] |
|**sortOrder** | **Integer** | **sort order** for *this* itinerary |  [optional] |
|**totalPrice** | **BigDecimal** | **numeric total price (total)** for *this* order - For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  |  [optional] |
|**totalPriceFormatted** | **String** | **currency-formatted total price (including transaction fee)** for *this* order - For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  |  [optional] |
|**totalPriceUSD** | **BigDecimal** | **numeric total price** of *this* order in USD |  [optional] |
|**userId** | **Integer** | ignore (Viator only) |  [optional] |
|**voucherKey** | **String** | Unique reference for the voucher for this booking that can be used as a request parameter to search for existing bookings using the [/booking/mybookings](#operation/bookingMybookings) and [/booking/pastbooking](#operation/bookingPastbooking) endpoints |  [optional] |
|**voucherURL** | **String** | **URL of the voucher** for *this* product (if available). The customer can access this URL to retrieve their voucher. |  [optional] |



