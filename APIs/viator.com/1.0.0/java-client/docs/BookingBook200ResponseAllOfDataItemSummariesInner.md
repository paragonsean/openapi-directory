

# BookingBook200ResponseAllOfDataItemSummariesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applePassSupported** | **Boolean** |  |  [optional] |
|**barcodeOption** | **String** | Indicates whether a voucher is required for each passenger; or, whether the requirement is one voucher per group booking. |  [optional] |
|**barcodeType** | **String** | **alphanumeric code** specifying the type of barcode |  [optional] |
|**bookingEngineId** | **BookingEngineIdResponse** |  |  [optional] |
|**bookingStatus** | [**BookingStatusItem**](BookingStatusItem.md) |  |  [optional] |
|**currencyCode** | **String** | **currency code** for the currency in which pricing is displayed for *this* item |  [optional] |
|**departsFrom** | **String** | **natural-language description** of *this* item&#39;s departure location |  [optional] |
|**departurePoint** | **String** | **natural-language description** of *this* item&#39;s departure point |  [optional] |
|**departurePointAddress** | **String** | **HTML-formatted address** of *this* item&#39;s departure point |  [optional] |
|**departurePointDirections** | **String** | **natural-language description** of directions regarding *this* item&#39;s departure point |  [optional] |
|**destId** | **Integer** | **unique numeric identifer** of the destination of *this* item |  [optional] |
|**distributorItemRef** | **String** | ignore (Viator only) |  [optional] |
|**hoursConfirmed** | **String** | The &#x60;hoursConfirmed&#x60; field also indicates if the product is freesale or on request. The &#x60;hoursConfirmed&#x60; value is the approximate window for confirmation in hours, which can be presented to the customer. A value of &#x60;0&#x60; means that the product is **freesale**, and a value greater than &#x60;0&#x60; means that the product is **on-request**.  |  [optional] |
|**itemId** | **Integer** | **numeric identifer** of *this* item |  [optional] |
|**itineraryId** | **Integer** | Ignore (Viator only) |  [optional] |
|**languageServicesCode** | **String** | **code** for the language that this product operates in |  [optional] |
|**lastRetailPrice** | **BigDecimal** | **numeric merchant net rate** of *this* item |  [optional] |
|**lastRetailPriceFormatted** | **String** | **currency-formatted merchant net rate** of *this* item |  [optional] |
|**leadTravellerFirstname** | **String** | **first name** of the lead traveler |  [optional] |
|**leadTravellerSurname** | **String** | **surname** of the lead traveler |  [optional] |
|**leadTravellerTitle** | **String** | **title** of the lead traveler&#39;s name |  [optional] |
|**merchantCancellable** | **Boolean** | ignore (Viator only)  For cancellation information regarding the booking, please refer to the &#x60;merchantTermsAndConditions&#x60; object  |  [optional] |
|**merchantNetPrice** | **BigDecimal** | **numeric merchant net rate** for *this* item\&quot; - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**merchantNetPriceFormatted** | **String** | **currency-formatted merchant net rate** for *this* item - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**merchantTermsAndConditions** | [**BookingBook200ResponseAllOfDataItemSummariesInnerMerchantTermsAndConditions**](BookingBook200ResponseAllOfDataItemSummariesInnerMerchantTermsAndConditions.md) |  |  [optional] |
|**obfsId** | **Integer** | ignore (Viator only) |  [optional] |
|**passbooks** | **String** | ignore (Viator only) |  [optional] |
|**pickupHotelId** | **String** | **identifer** for the pick-up hotel |  [optional] |
|**pickupHotelName** | **String** | **natural-language name** of the pick-up hotel |  [optional] |
|**price** | **BigDecimal** | **numeric merchant total price** for *this* item - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**priceFormatted** | **String** | **currency-formatted merchant total price** for *this* item - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**priceUSD** | **BigDecimal** | **numeric merchant total price** in USD |  [optional] |
|**productCode** | **String** | **unique alphanumeric identifier** of *this* product |  [optional] |
|**productPulledDown** | **Boolean** | ignore (Viator only) |  [optional] |
|**productTitle** | **String** | **natural-language title** of *this* product |  [optional] |
|**productWidgetList** | **String** | ignore (Viator only) |  [optional] |
|**rulesApplied** | **String** | ignore (Viator only) |  [optional] |
|**savingAmount** | **String** | Ignore (Viator only)  |  [optional] |
|**savingAmountFormated** | **String** | Ignore (Viator only)  |  [optional] |
|**sortOrder** | **Integer** | **sort order** of *this* item summary |  [optional] |
|**startingTime** | **String** | **starting time** of this product |  [optional] |
|**supplierName** | **String** | **natural-language name** of *this* product&#39;s supplier |  [optional] |
|**supplierPhoneNumber** | **String** | **telephone number** of *this* product&#39;s supplier |  [optional] |
|**termsAndConditions** | **Object** | ignore (Viator only) |  [optional] |
|**tourGradeCode** | **String** | **identifer** of *this* tour grade |  [optional] |
|**tourGradeDescription** | **String** | **natural-language description** of *this* tour grade |  [optional] |
|**travelDate** | **String** | **date** of travel |  [optional] |
|**travellerAgeBands** | [**List&lt;BookingBook200ResponseAllOfDataItemSummariesInnerTravellerAgeBandsInner&gt;**](BookingBook200ResponseAllOfDataItemSummariesInnerTravellerAgeBandsInner.md) | **array** of objects detailing the traveler age bands |  [optional] |
|**voucherKey** | **String** | Unique reference for the voucher for this booking that can be used as a request parameter to search for existing bookings using the [/booking/mybookings](#operation/bookingMybookings) and [/booking/pastbooking](#operation/bookingPastbooking) endpoints |  [optional] |
|**voucherOption** | **String** | ignore (Viator only) |  [optional] |
|**voucherRequirements** | **String** | **natural-language description** of the requirements pertaining to this voucher |  [optional] |
|**voucherURL** | **String** | **URL of the voucher** for *this* product (if available). The customer can access this URL to retrieve their voucher. |  [optional] |
|**vouchers** | **String** | ignore (Viator only) |  [optional] |



