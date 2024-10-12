

# SearchProducts200ResponseAllOfDataInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**admission** | **String** | ignore (Viator only) |  [optional] |
|**available** | **Boolean** | ignore (Viator only) |  [optional] |
|**bookingEngineId** | **BookingEngineId** |  |  [optional] |
|**catIds** | **List&lt;Integer&gt;** | **list** of unique numeric category identifiers for *this* product - the &#x60;categoryId&#x60; for the destination is available from the [/taxonomy/categories](#operation/taxonomyCategories) service  |  [optional] |
|**code** | **String** | **unique alphanumeric identifier** of *this* product |  [optional] |
|**currencyCode** | **String** | **indicator** of the currency in which *this* product&#39;s prices are displayed |  [optional] |
|**duration** | **String** | **natural-language description** of the duration of *this* product |  [optional] |
|**essential** | **String** | ignore (Viator only) |  [optional] |
|**merchantCancellable** | **Boolean** | ignore (Viator only)       For cancellation information regarding the booking, please refer to the &#x60;merchantTermsAndConditions&#x60; object  |  [optional] |
|**merchantNetPriceFrom** | **BigDecimal** | Numeric &#39;from&#39; (lowest possible) price that Viator will invoice the merchant for the sale of this product, excluding the transaction fee; i.e. the merchant net rate  For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  |  [optional] |
|**merchantNetPriceFromFormatted** | **String** | Currency-formatted &#39;from&#39; (lowest possible) price that Viator will invoice the merchant for the sale of this product, excluding the transaction fee (i.e. the merchant net rate)  For more information, see: [Merchant pricing](#section/Key-concepts/Merchant-pricing)  |  [optional] |
|**onRequestPeriod** | **Integer** | **number** of hours before the travel date that *this* product will be &#39;on-request&#39; for - this field will contain a value if the &#x60;bookingEngineId&#x60; is &#x60;&#39;FreesaleOnRequestBE&#39;&#x60; - an &#x60;onRequestPeriod&#x60; of 48 hours means that *this* product is freesale up until 48 hours before the travel date, and is on-request for 48 hours or less until the travel date - **note**: &#39;hours in advance&#39; (the number of hours a product is available for booking before the travel date) may also affect this; however, this value is not available in the API  |  [optional] |
|**onSale** | **Boolean** | Ignore (Viator only)  |  [optional] |
|**panoramaCount** | **Integer** | **number** of panoramic images available for *this* product |  [optional] |
|**pas** | **Object** | **object** detailing product availability - &#x60;pas&#x60; stands for Product Availability Schema  |  [optional] |
|**photoCount** | **Integer** | **number** of user photos published for *this* product |  [optional] |
|**price** | **BigDecimal** | **suggested sell (&#39;from&#39;) price** for this product in the currency set in the &#x60;currencyCode&#x60; parameter. This is the cheapest sell price, taking into consideration off-peak periods and discounts on larger groups.     - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**priceFormatted** | **String** | **currency-formatted suggested sell (&#39;from&#39;) price** for this product in the currency set in the &#x60;currencyCode&#x60; parameter  - For more information, see: [Merchant pricing](#section/Merchant-APIs/Merchant-pricing)  |  [optional] |
|**primaryDestinationId** | **Integer** | **unique numeric identifier** of *this* product&#39;s primary destination |  [optional] |
|**primaryDestinationName** | **String** | **natural-language name** of *this* product&#39;s primary destination |  [optional] |
|**primaryDestinationUrlName** | **String** | **URL-formatted name** of *this* product&#39;s primary destination |  [optional] |
|**primaryGroupId** | **Integer** | ignore (Viator only) |  [optional] |
|**productUrlName** | **String** | **URL-formatted name** of *this* product |  [optional] |
|**rating** | **BigDecimal** | **average user rating** of *this* product  users rate products by assigning a star-rating from 1-5; this value shows the average of the star ratings provided by users;  the &#x60;ratingCounts&#x60; associative array in this response provides a breakdown of how many submissions for each star rating have been received  |  [optional] |
|**reviewCount** | **Integer** | **number** of user reviews that have been submitted by users for *this* product  If your account has been configured to limit the number of reviews you can receive, this value will never be higher than that. Otherwise, this value will show the total number of reviews available for this product. If there are more than 24 reviews available, you will need to use the [/product/reviews](#operation/productReviews) service to retrieve the remainder of the reviews.  |  [optional] |
|**rrp** | **Integer** | **numeric original price** for this product if the product is on special / a discount has been applied. &#x60;0&#x60; if there is no discount on this product. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**rrpformatted** | **String** | **currency-formatted original price** for this product if the product is on special / a discount has been applied. Empty string if there is no discount on this product. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**savingAmount** | **String** | Ignore (Viator only)  |  [optional] |
|**savingAmountFormated** | **String** | Ignore (Viator only)  |  [optional] |
|**shortDescription** | **String** | **HTML-formatted natural-language description** of *this* product |  [optional] |
|**shortTitle** | **String** | **short natural-language title** of *this* product (for use when there is a need to conserve space) |  [optional] |
|**sortOrder** | **Integer** | **sort order** for *this* product |  [optional] |
|**specialOfferAvailable** | **Boolean** | ignore (Viator only) |  [optional] |
|**specialReservation** | **Boolean** | ignore (Viator only) |  [optional] |
|**specialReservationDetails** | **String** | ignore (Viator only) |  [optional] |
|**sslSupported** | **Object** | ignore (Viator only) |  [optional] |
|**subCatIds** | **List&lt;Integer&gt;** | **list** of unique numeric subcategory identifiers for *this* product - the &#x60;subcategoryId&#x60; for the destination is available from the [/taxonomy/categories](#operation/taxonomyCategories) service  |  [optional] |
|**supplierCode** | **String** | **unique identifier** of *this* product&#39;s supplier in text string format |  [optional] |
|**supplierName** | **String** | **natural-language name** of *this* product&#39;s supplier |  [optional] |
|**thumbnailHiResURL** | **String** | **URL** for the high resolution thumbnail for *this* product |  [optional] |
|**thumbnailURL** | **String** | **URL** for *this* product&#39;s thumbnail image |  [optional] |
|**title** | **String** | **natural-language title** of *this* product |  [optional] |
|**translationLevel** | **TranslationLevel** |  |  [optional] |
|**uniqueShortDescription** | **String** | ignore (Viator only) |  [optional] |
|**videoCount** | **Integer** | ignore (Viator only) – videos are not available to partners |  [optional] |
|**webURL** | **String** | ignore (Viator only) |  [optional] |



