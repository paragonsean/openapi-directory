

# SearchFreetextResponseProductAllOfData

**object** detailing a **product** that matches the search criteria

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**admission** | **String** | ignore (Viator only) |  [optional] |
|**attractionLatitude** | **String** | ignore (Viator only) |  [optional] |
|**attractionLongitude** | **String** | ignore (Viator only) |  [optional] |
|**available** | **Boolean** | ignore (Viator only) |  [optional] |
|**bookingEngineId** | **BookingEngineId** |  |  [optional] |
|**catIds** | **List&lt;Integer&gt;** | **list** of unique numeric product category identifiers  - &#x60;categoryId&#x60; is available for the destination from the [/taxonomy/categories](#operation/taxonomyCategories) service  |  [optional] |
|**code** | **String** | **unique alphanumeric identifier** of *this* product |  [optional] |
|**currencyCode** | **String** | **currency** in which *this* product&#39;s pricing is displayed |  [optional] |
|**duration** | **String** | **natural-language duration** of *this* product |  [optional] |
|**essential** | **String** | ignore (Viator only) |  [optional] |
|**merchantCancellable** | **Boolean** | ignore (Viator only)  For cancellation information regarding the booking, please refer to the &#x60;merchantTermsAndConditions&#x60; object  |  [optional] |
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
|**primaryGroupId** | **String** | ignore (Viator only) |  [optional] |
|**productURLName** | **String** | **URL-formatted name** of *this* product |  [optional] |
|**publishedDate** | **String** | ignore (Viator only) |  [optional] |
|**rating** | **BigDecimal** | **average user rating** of *this* product  users rate products by assigning a star-rating from 1-5; this value shows the average of the star ratings provided by users;  the &#x60;ratingCounts&#x60; associative array in this response provides a breakdown of how many submissions for each star rating have been received  |  [optional] |
|**reviewCount** | **Integer** | **number** of user reviews that have been submitted by users for *this* product  If your account has been configured to limit the number of reviews you can receive, this value will never be higher than that. Otherwise, this value will show the total number of reviews available for this product. If there are more than 24 reviews available, you will need to use the [/product/reviews](#operation/productReviews) service to retrieve the remainder of the reviews.  |  [optional] |
|**rrp** | **Integer** | **numeric original price** for this product if the product is on special / a discount has been applied. &#x60;0&#x60; if there is no discount on this product. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**rrpformatted** | **String** | **currency-formatted original price** for this product if the product is on special / a discount has been applied. Empty string if there is no discount on this product. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**savingAmount** | **String** | Ignore (Viator only)  |  [optional] |
|**savingAmountFormated** | **String** | Ignore (Viator only)  |  [optional] |
|**shortDescription** | **String** | **natural-language description** (shortened) of *this* product |  [optional] |
|**shortTitle** | **String** | **natural-language title** (shortened) of *this* product |  [optional] |
|**sortOrder** | **Integer** | ignore (Viator only) |  [optional] |
|**specialOfferAvailable** | **Boolean** | **indicator**: &#x60;true&#x60; if a special offer is available for *this* product. If &#x60;true&#x60; the &#x60;specialOffer&#x60; field will contain a text string providing details of the special offer which you may wish to display in your product search results. E.g. &#39;Book by May 27 to save 34% off our previously offered price!&#39;. See [Special offers and on-sale pricing](#section/Key-concepts/Special-offers-and-on-sale-pricing) for more information. |  [optional] |
|**specialReservation** | **Boolean** | ignore (Viator only) |  [optional] |
|**specialReservationDetails** | **String** | ignore (Viator only) |  [optional] |
|**sslSupported** | **Boolean** | ignore (Viator only) |  [optional] |
|**subCatIds** | **List&lt;Integer&gt;** | **list** of unique numeric subcategory identifiers that *this* product falls under - &#x60;subcategoryId&#x60; is available from [/taxonomy/categories](#operation/taxonomyCategories) service\&quot;  |  [optional] |
|**supplierCode** | **String** | **unique identifier** of *this* product&#39;s supplier |  [optional] |
|**supplierName** | **String** | **natural-language name** of *this* product&#39;s supplier |  [optional] |
|**thumbnailHiResURL** | **String** | **high-resolution thumbnail image URL** for *this* product |  [optional] |
|**thumbnailURL** | **String** | **URL** of *this* product&#39;s thumbnail image |  [optional] |
|**title** | **String** | **natural-language title** of *this* product |  [optional] |
|**translationLevel** | **TranslationLevel** |  |  [optional] |
|**uniqueShortDescription** | **String** | ignore (Viator only) |  [optional] |
|**videoCount** | **Integer** | ignore (Viator only) – videos are not available to partners |  [optional] |
|**webURL** | **String** | ignore (Viator only) |  [optional] |



