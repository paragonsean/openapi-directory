

# Product200ResponseAllOfData

**object** containing product details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInfo** | **List&lt;String&gt;** | **array** of HTML-formatted clauses providing additional information about *this* product, such as: - when the confirmation will be received (i.e. at time of booking, or within 48 hours of booking etc) - accessibility options; such as whether wheelchair access is available - particulars about the pick-up location and process - **Note**: may contain basic HTML mark-up tags – e.g., br, li, b, u, p, i, ul and ol  |  [optional] |
|**admission** | **String** | ignore (Viator only) |  [optional] |
|**ageBands** | [**List&lt;Product200ResponseAllOfDataAgeBandsInner&gt;**](Product200ResponseAllOfDataAgeBandsInner.md) | **array** of age band objects detailing the age bands available for *this* product    - **note**: only the age bands listed here can book this product using the [/booking/book](#operation/bookingBook) service  |  [optional] |
|**allTravellerNamesRequired** | **Boolean** | **indicator**: &#x60;true&#x60; if all traveler names are required.&amp;lt;br /&amp;gt;**Note**: if set to &#x60;true&#x60;, then all passenger names must be included in the booking request, and all must be unique. Placeholder names cannot be used. |  [optional] |
|**applePassSupported** | **Boolean** | **indicator**: &#x60;true&#x60; if Apple Wallet is supported |  [optional] |
|**available** | **Boolean** | ignore (Viator only) |  [optional] |
|**bookingEngineId** | **BookingEngineId** |  |  [optional] |
|**bookingQuestions** | [**List&lt;Product200ResponseAllOfDataBookingQuestionsInner&gt;**](Product200ResponseAllOfDataBookingQuestionsInner.md) |  |  [optional] |
|**catIds** | **List&lt;Integer&gt;** | **list** of unique numeric category identifiers that *this* product falls under - &#x60;categoryId&#x60; is available from the [/taxonomy/categories](#operation/taxonomyCategories) service  |  [optional] |
|**city** | **String** | **name** of city or destination that *this* product operates in |  [optional] |
|**code** | **String** | **unique alphanumeric identifier** of *this* product |  [optional] |
|**country** | **String** | **natural-language name** of the country in which *this* product operates |  [optional] |
|**currencyCode** | **String** | **currency** in which to display *this* product&#39;s pricing details |  [optional] |
|**departurePoint** | **String** | **HTML-formatted natural-language description** of *this* product&#39;s departure location |  [optional] |
|**departureTime** | **String** | **HTML-formatted natural-language description** of *this* product&#39;s departure times - may contain basic HTML mark-up tags; e.g., br, li, b, u, p, i, ul and ol  |  [optional] |
|**departureTimeComments** | **String** | **HTML-formatted natural-language description** of extra information pertaining to product departure times |  [optional] |
|**description** | **String** | **HTML-formatted natural-language description** of *this* product (extended) |  [optional] |
|**destinationId** | **Integer** | **unique numeric identifier** of the destination in which *this* product is located - &#x60;destinationId&#x60; is available from the [/taxonomy/destinations](#operation/taxonomyDestinations) service  |  [optional] |
|**duration** | **String** | **natural-language description** of *this* product&#39;s duration |  [optional] |
|**essential** | **String** | ignore (Viator only) |  [optional] |
|**exclusions** | **List&lt;String&gt;** | **array** of HTML-formatted natural-language exclusions for *this* product - may contain basic HTML mark-up - e.g., br, li, b, u, p, i, ul and ol  |  [optional] |
|**highlights** | **Integer** | ignore (Viator only) |  [optional] |
|**hotelPickup** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* product offers hotel pick-up; if so, you will need to collect the user&#39;s hotel details |  [optional] |
|**inclusions** | **List&lt;String&gt;** | **array** of HTML-formatted features included in *this* product - may contain basic HTML mark-up tags; e.g., br, li, b, u, p, i, ul and ol  |  [optional] |
|**itinerary** | **String** | **HTML-formatted description** of the itinerary of *this* tour if available - may contain basic HTML tags; e.g., br, li, b, u, p, i, ul and ol  |  [optional] |
|**location** | **String** | **natural-language description** of *this* product&#39;s location -  can be a combination of the country and city, or a custom location  |  [optional] |
|**mapURL** | **String** | **URL** of this product&#39;s map (usually an image) |  [optional] |
|**maxTravellerCount** | **Integer** | **maximum number of travelers** allowed per-booking for *this* product |  [optional] |
|**merchantCancellable** | **Boolean** | ignore (Viator only)         For cancellation information regarding the booking, please refer to the &#x60;merchantTermsAndConditions&#x60; object  |  [optional] |
|**merchantNetPriceFrom** | **BigDecimal** | Numeric &#39;from&#39; (lowest possible) price that Viator will invoice the merchant for the sale of this product, excluding the transaction fee; i.e. the merchant net rate  For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  |  [optional] |
|**merchantNetPriceFromFormatted** | **String** | Currency-formatted &#39;from&#39; (lowest possible) price that Viator will invoice the merchant for the sale of this product, excluding the transaction fee (i.e. the merchant net rate)  For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  |  [optional] |
|**merchantTermsAndConditions** | [**Product200ResponseAllOfDataMerchantTermsAndConditions**](Product200ResponseAllOfDataMerchantTermsAndConditions.md) |  |  [optional] |
|**onRequestPeriod** | **Integer** | **number** of hours before the travel date that *this* product will be &#39;on-request&#39; for - this field will contain a value if the &#x60;bookingEngineId&#x60; is &#x60;&#39;FreesaleOnRequestBE&#39;&#x60; - an &#x60;onRequestPeriod&#x60; of 48 hours means that *this* product is freesale up until 48 hours before the travel date, and is on-request for 48 hours or less until the travel date - **note**: &#39;hours in advance&#39; (the number of hours a product is available for booking before the travel date) may also affect this; however, this value is not available in the API  |  [optional] |
|**onSale** | **Boolean** | Ignore (Viator only)  |  [optional] |
|**operates** | **String** | **HTML-formatted natural-language description** of *this* product&#39;s operation frequency |  [optional] |
|**panoramaCount** | **Integer** | **number** of panoramic images available for *this* product |  [optional] |
|**pas** | **Object** | ignore (Viator only) |  [optional] |
|**passengerAttributes** | [**List&lt;Product200ResponseAllOfDataPassengerAttributesInner&gt;**](Product200ResponseAllOfDataPassengerAttributesInner.md) | ignore (Viator only) |  [optional] |
|**photoCount** | **Integer** | **number** of user photos available for *this* product |  [optional] |
|**price** | **BigDecimal** | **suggested sell (&#39;from&#39;) price** for this product in the currency set in the &#x60;currencyCode&#x60; parameter. This is the cheapest sell price, taking into consideration off-peak periods and discounts on larger groups.     - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**priceFormatted** | **String** | **currency-formatted suggested sell (&#39;from&#39;) price** for this product in the currency set in the &#x60;currencyCode&#x60; parameter  - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**primaryDestinationId** | **Integer** | **unique numeric identifier** of *this* product&#39;s primary destination |  [optional] |
|**primaryDestinationName** | **String** | **natural-language name** of *this* product&#39;s primary destination |  [optional] |
|**primaryDestinationUrlName** | **String** | **URL-formatted name** of the destination in which *this* product is located |  [optional] |
|**primaryGroupId** | **String** | ignore (Viator only) |  [optional] |
|**productPhotos** | [**List&lt;Product200ResponseAllOfDataProductPhotosInner&gt;**](Product200ResponseAllOfDataProductPhotosInner.md) | **array** of image objects detailing images available for *this* product |  [optional] |
|**productUrlName** | **String** | **URL-formatted name** of *this* product |  [optional] |
|**rating** | **BigDecimal** | **average user rating** of *this* product  users rate products by assigning a star-rating from 1-5; this value shows the average of the star ratings provided by users;  the &#x60;ratingCounts&#x60; associative array in this response provides a breakdown of how many submissions for each star rating have been received  |  [optional] |
|**ratingCounts** | [**RatingCounts**](RatingCounts.md) |  |  [optional] |
|**region** | **String** | **natural-language name** of the region in which *this* product operates |  [optional] |
|**returnDetails** | **String** | **HTML-formatted natural-language description** of *this* product&#39;s drop-off details (if available) |  [optional] |
|**reviewCount** | **Integer** | **number** of user reviews that have been submitted by users for *this* product  If your account has been configured to limit the number of reviews you can receive, this value will never be higher than that. Otherwise, this value will show the total number of reviews available for this product. If there are more than 24 reviews available, you will need to use the [/product/reviews](#operation/productReviews) service to retrieve the remainder of the reviews.  |  [optional] |
|**reviews** | [**List&lt;ReviewObject&gt;**](ReviewObject.md) | **array** of user review objects  The number of reviews returned here will either be the number of reviews you are entitled to according to your account configuration; or, if you are not limited in the number of reviews you can receive, will be a maxiumum of 24 reviews. If the value of &#x60;reviewCount&#x60; in this response exceeds 24, you can use the [/product/reviews](#operation/productReviews) endpoint to retrieve the remainder of the reviews.  |  [optional] |
|**rrp** | **Integer** | **numeric original price** for this product if the product is on special / a discount has been applied. &#x60;0&#x60; if there is no discount on this product. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**rrpFormatted** | **String** | **currency-formatted original price** for this product if the product is on special / a discount has been applied. Empty string if there is no discount on this product. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**salesPoints** | **List&lt;String&gt;** | ignore (Viator only)  **Note**: The information that was previously returned in this field is available in the &#x60;additionalInfo&#x60;, &#x60;inclusions&#x60; and &#x60;description&#x60; fields  |  [optional] |
|**savingAmount** | **String** | Ignore (Viator only)  |  [optional] |
|**savingAmountFormated** | **String** | Ignore (Viator only)  |  [optional] |
|**shortDescription** | **String** | **natural-language description** (shortened) of *this* product |  [optional] |
|**shortTitle** | **String** | **natural-language title** (shortened) of *this* product |  [optional] |
|**specialOffer** | **String** | **natural-language description** of any special offers available for *this* product when &#x60;specialOfferAvailable&#x60; is &#x60;true&#x60;. - empty string if there are no specials available - See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information.  |  [optional] |
|**specialOfferAvailable** | **Boolean** | **indicator**: &#x60;true&#x60; if a special offer is available for *this* product. If &#x60;true&#x60; the &#x60;specialOffer&#x60; field will contain a text string providing details of the special offer which you may wish to display in your product search results. E.g. &#39;Book by May 27 to save 34% off our previously offered price!&#39;. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**specialReservation** | **Boolean** | ignore (Viator only) |  [optional] |
|**specialReservationDetails** | **String** | ignore (Viator only) |  [optional] |
|**sslSupported** | **Boolean** | ignore (Viator only) |  [optional] |
|**subCatIds** | **List&lt;Integer&gt;** | **list** of unique numeric subcategory identifiers that *this* product falls under - &#x60;subcategoryId&#x60; is available from the [/taxonomy/categories](#operation/taxonomyCategories) service  |  [optional] |
|**supplierCode** | **String** | **unique identification code** of *this* product&#39;s supplier |  [optional] |
|**supplierName** | **String** | **name** of *this* product&#39;s supplier |  [optional] |
|**thumbnailHiResURL** | **String** | **URL** of *this* product&#39;s high-resolution thumbnail image |  [optional] |
|**thumbnailURL** | **String** | **URL** for *this* product&#39;s thumbnail image |  [optional] |
|**title** | **String** | **natural-language title** of *this* product |  [optional] |
|**tourGrades** | [**List&lt;Product200ResponseAllOfDataTourGradesInner&gt;**](Product200ResponseAllOfDataTourGradesInner.md) | **array** of tour grade objects available for *this* product |  [optional] |
|**tourGradesAvailable** | **Boolean** | **indicator**:  - &#x60;true&#x60;: tour grades are available for this product, meaning you will need to display these tour grades to the user and include a tour grade when booking *this* product - &#x60;false&#x60;: only a default tour grade is available for *this* product  |  [optional] |
|**translationLevel** | **TranslationLevel** |  |  [optional] |
|**userPhotos** | [**List&lt;PhotoObject&gt;**](PhotoObject.md) | **array** of user photo objects |  [optional] |
|**videoCount** | **Integer** | ignore (Viator only) – videos are not available to partners |  [optional] |
|**videos** | **String** | ignore (Viator only) – videos are not available to partners |  [optional] |
|**voucherOption** | **String** | **specifier** of the type(s) of vouchers that can be used:    - &#x60;VOUCHER_PAPER_ONLY&#x60; - *only* printed paper vouchers accepted   - &#x60;VOUCHER_E&#x60; - e-vouchers + printed paper vouchers accepted  |  [optional] |
|**voucherRequirements** | **Object** | **natural-language description** of any requirements pertaining to the use of the voucher |  [optional] |
|**webURL** | **String** | ignore (Viator only) |  [optional] |



