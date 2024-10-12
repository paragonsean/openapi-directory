

# BookingBook200ResponseAllOfData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookerEmail** | **String** | **email address** of the entity that made *this* booking |  [optional] |
|**bookingDate** | **String** | **date** of *this* booking |  [optional] |
|**bookingStatus** | [**BookingStatusItinerary**](BookingStatusItinerary.md) |  |  [optional] |
|**currencyCode** | **String** | **currency code** of the currency in which *this* booking was made |  [optional] |
|**distributorRef** | **String** | ignore (Viator only) |  [optional] |
|**exchangeRate** | **Integer** | ignore (Viator only) |  [optional] |
|**hasVoucher** | **Boolean** | ignore (Viator only) |  [optional] |
|**itemSummaries** | [**List&lt;BookingBook200ResponseAllOfDataItemSummariesInner&gt;**](BookingBook200ResponseAllOfDataItemSummariesInner.md) | **array** of item summaries |  [optional] |
|**itineraryId** | **Integer** | ignore (Viator only) |  [optional] |
|**omniPreRuleList** | **String** | ignore (Viator only) |  [optional] |
|**paypalRedirectURL** | **String** | ignore (Viator only) |  [optional] |
|**rulesApplied** | **String** | ignore (Viator only) |  [optional] |
|**securityToken** | **String** | ignore (Viator only) |  [optional] |
|**sortOrder** | **Integer** | **sort order** for *this* object |  [optional] |
|**totalPrice** | **BigDecimal** | **numeric merchant total price** for *this* booking - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**totalPriceFormatted** | **String** | **currency-formatted merchant total price** for *this* booking - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**totalPriceUSD** | **BigDecimal** | **numeric merchant total price** of *this* booking in USD |  [optional] |
|**userId** | **String** | ignore (Viator only) |  [optional] |
|**voucherKey** | **String** | Unique reference for the voucher for this booking that can be used as a request parameter to search for existing bookings using the [/booking/mybookings](#operation/bookingMybookings) and [/booking/pastbooking](#operation/bookingPastbooking) endpoints |  [optional] |
|**voucherURL** | **String** | **URL of the voucher** for *this* product (if available). The customer can access this URL to retrieve their voucher. |  [optional] |



