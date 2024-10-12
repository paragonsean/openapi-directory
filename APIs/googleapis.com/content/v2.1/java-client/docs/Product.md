

# Product

 Required product attributes are primarily defined by the product data specification. See the Product Data Specification Help Center article for information. Product data. After inserting, updating, or deleting a product, it may take several minutes before changes take effect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalImageLinks** | **List&lt;String&gt;** | Additional URLs of images of the item. |  [optional] |
|**additionalSizeType** | **String** | Additional cut of the item. Used together with size_type to represent combined size types for apparel items. |  [optional] |
|**adsGrouping** | **String** | Used to group items in an arbitrary way. Only for CPA%, discouraged otherwise. |  [optional] |
|**adsLabels** | **List&lt;String&gt;** | Similar to ads_grouping, but only works on CPC. |  [optional] |
|**adsRedirect** | **String** | Allows advertisers to override the item URL when the product is shown within the context of Product Ads. |  [optional] |
|**adult** | **Boolean** | Should be set to true if the item is targeted towards adults. |  [optional] |
|**ageGroup** | **String** | Target age group of the item. |  [optional] |
|**availability** | **String** | Availability status of the item. |  [optional] |
|**availabilityDate** | **String** | The day a pre-ordered product becomes available for delivery, in ISO 8601 format. |  [optional] |
|**brand** | **String** | Brand of the item. |  [optional] |
|**canonicalLink** | **String** | URL for the canonical version of your item&#39;s landing page. |  [optional] |
|**certifications** | [**List&lt;ProductCertification&gt;**](ProductCertification.md) | Product [certification](https://support.google.com/merchants/answer/13528839), introduced for EU energy efficiency labeling compliance using the [EU EPREL](https://eprel.ec.europa.eu/screen/home) database. |  [optional] |
|**channel** | **String** | Required. The item&#39;s channel (online or local). Acceptable values are: - \&quot;&#x60;local&#x60;\&quot; - \&quot;&#x60;online&#x60;\&quot;  |  [optional] |
|**cloudExportAdditionalProperties** | [**List&lt;CloudExportAdditionalProperties&gt;**](CloudExportAdditionalProperties.md) | Extra fields to export to the Cloud Retail program. |  [optional] |
|**color** | **String** | Color of the item. |  [optional] |
|**condition** | **String** | Condition or state of the item. |  [optional] |
|**contentLanguage** | **String** | Required. The two-letter ISO 639-1 language code for the item. |  [optional] |
|**costOfGoodsSold** | [**Price**](Price.md) |  |  [optional] |
|**customAttributes** | [**List&lt;CustomAttribute&gt;**](CustomAttribute.md) | A list of custom (merchant-provided) attributes. It can also be used for submitting any attribute of the feed specification in its generic form (for example, &#x60;{ \&quot;name\&quot;: \&quot;size type\&quot;, \&quot;value\&quot;: \&quot;regular\&quot; }&#x60;). This is useful for submitting attributes not explicitly exposed by the API, such as additional attributes used for Buy on Google (formerly known as Shopping Actions). |  [optional] |
|**customLabel0** | **String** | Custom label 0 for custom grouping of items in a Shopping campaign. |  [optional] |
|**customLabel1** | **String** | Custom label 1 for custom grouping of items in a Shopping campaign. |  [optional] |
|**customLabel2** | **String** | Custom label 2 for custom grouping of items in a Shopping campaign. |  [optional] |
|**customLabel3** | **String** | Custom label 3 for custom grouping of items in a Shopping campaign. |  [optional] |
|**customLabel4** | **String** | Custom label 4 for custom grouping of items in a Shopping campaign. |  [optional] |
|**description** | **String** | Description of the item. |  [optional] |
|**disclosureDate** | **String** | The date time when an offer becomes visible in search results across Google’s YouTube surfaces, in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format. See [Disclosure date](https://support.google.com/merchants/answer/13034208) for more information. |  [optional] |
|**displayAdsId** | **String** | An identifier for an item for dynamic remarketing campaigns. |  [optional] |
|**displayAdsLink** | **String** | URL directly to your item&#39;s landing page for dynamic remarketing campaigns. |  [optional] |
|**displayAdsSimilarIds** | **List&lt;String&gt;** | Advertiser-specified recommendations. |  [optional] |
|**displayAdsTitle** | **String** | Title of an item for dynamic remarketing campaigns. |  [optional] |
|**displayAdsValue** | **Double** | Offer margin for dynamic remarketing campaigns. |  [optional] |
|**energyEfficiencyClass** | **String** | The energy efficiency class as defined in EU directive 2010/30/EU. |  [optional] |
|**excludedDestinations** | **List&lt;String&gt;** | The list of destinations to exclude for this target (corresponds to cleared check boxes in Merchant Center). Products that are excluded from all destinations for more than 7 days are automatically deleted. |  [optional] |
|**expirationDate** | **String** | Date on which the item should expire, as specified upon insertion, in ISO 8601 format. The actual expiration date in Google Shopping is exposed in &#x60;productstatuses&#x60; as &#x60;googleExpirationDate&#x60; and might be earlier if &#x60;expirationDate&#x60; is too far in the future. |  [optional] |
|**externalSellerId** | **String** | Required for multi-seller accounts. Use this attribute if you&#39;re a marketplace uploading products for various sellers to your multi-seller account. |  [optional] |
|**feedLabel** | **String** | Feed label for the item. Either &#x60;targetCountry&#x60; or &#x60;feedLabel&#x60; is required. Must be less than or equal to 20 uppercase letters (A-Z), numbers (0-9), and dashes (-). |  [optional] |
|**gender** | **String** | Target gender of the item. |  [optional] |
|**googleProductCategory** | **String** | Google&#39;s category of the item (see [Google product taxonomy](https://support.google.com/merchants/answer/1705911)). When querying products, this field will contain the user provided value. There is currently no way to get back the auto assigned google product categories through the API. |  [optional] |
|**gtin** | **String** | Global Trade Item Number (GTIN) of the item. |  [optional] |
|**id** | **String** | The REST ID of the product. Content API methods that operate on products take this as their &#x60;productId&#x60; parameter. The REST ID for a product has one of the 2 forms channel:contentLanguage: targetCountry: offerId or channel:contentLanguage:feedLabel: offerId. |  [optional] |
|**identifierExists** | **Boolean** | False when the item does not have unique product identifiers appropriate to its category, such as GTIN, MPN, and brand. Required according to the Unique Product Identifier Rules for all target countries except for Canada. |  [optional] |
|**imageLink** | **String** | URL of an image of the item. |  [optional] |
|**includedDestinations** | **List&lt;String&gt;** | The list of destinations to include for this target (corresponds to checked check boxes in Merchant Center). Default destinations are always included unless provided in &#x60;excludedDestinations&#x60;. |  [optional] |
|**installment** | [**Installment**](Installment.md) |  |  [optional] |
|**isBundle** | **Boolean** | Whether the item is a merchant-defined bundle. A bundle is a custom grouping of different products sold by a merchant for a single price. |  [optional] |
|**itemGroupId** | **String** | Shared identifier for all variants of the same product. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#product&#x60;\&quot; |  [optional] |
|**lifestyleImageLinks** | **List&lt;String&gt;** | Additional URLs of lifestyle images of the item. Used to explicitly identify images that showcase your item in a real-world context. See the Help Center article for more information. |  [optional] |
|**link** | **String** | URL directly linking to your item&#39;s page on your website. |  [optional] |
|**linkTemplate** | **String** | URL template for merchant hosted local storefront. |  [optional] |
|**loyaltyPoints** | [**LoyaltyPoints**](LoyaltyPoints.md) |  |  [optional] |
|**material** | **String** | The material of which the item is made. |  [optional] |
|**maxEnergyEfficiencyClass** | **String** | The energy efficiency class as defined in EU directive 2010/30/EU. |  [optional] |
|**maxHandlingTime** | **String** | Maximal product handling time (in business days). |  [optional] |
|**minEnergyEfficiencyClass** | **String** | The energy efficiency class as defined in EU directive 2010/30/EU. |  [optional] |
|**minHandlingTime** | **String** | Minimal product handling time (in business days). |  [optional] |
|**mobileLink** | **String** | URL for the mobile-optimized version of your item&#39;s landing page. |  [optional] |
|**mobileLinkTemplate** | **String** | URL template for merchant hosted local storefront optimized for mobile devices. |  [optional] |
|**mpn** | **String** | Manufacturer Part Number (MPN) of the item. |  [optional] |
|**multipack** | **String** | The number of identical products in a merchant-defined multipack. |  [optional] |
|**offerId** | **String** | Required. A unique identifier for the item. Leading and trailing whitespaces are stripped and multiple whitespaces are replaced by a single whitespace upon submission. Only valid unicode characters are accepted. See the products feed specification for details. *Note:* Content API methods that operate on products take the REST ID of the product, *not* this identifier. |  [optional] |
|**pattern** | **String** | The item&#39;s pattern (for example, polka dots). |  [optional] |
|**pause** | **String** | Publication of this item should be temporarily paused. Acceptable values are: - \&quot;&#x60;ads&#x60;\&quot;  |  [optional] |
|**pickupMethod** | **String** | The pick up option for the item. Acceptable values are: - \&quot;&#x60;buy&#x60;\&quot; - \&quot;&#x60;reserve&#x60;\&quot; - \&quot;&#x60;ship to store&#x60;\&quot; - \&quot;&#x60;not supported&#x60;\&quot;  |  [optional] |
|**pickupSla** | **String** | Item store pickup timeline. Acceptable values are: - \&quot;&#x60;same day&#x60;\&quot; - \&quot;&#x60;next day&#x60;\&quot; - \&quot;&#x60;2-day&#x60;\&quot; - \&quot;&#x60;3-day&#x60;\&quot; - \&quot;&#x60;4-day&#x60;\&quot; - \&quot;&#x60;5-day&#x60;\&quot; - \&quot;&#x60;6-day&#x60;\&quot; - \&quot;&#x60;7-day&#x60;\&quot; - \&quot;&#x60;multi-week&#x60;\&quot;  |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**productDetails** | [**List&lt;ProductProductDetail&gt;**](ProductProductDetail.md) | Technical specification or additional product details. |  [optional] |
|**productHeight** | [**ProductDimension**](ProductDimension.md) |  |  [optional] |
|**productHighlights** | **List&lt;String&gt;** | Bullet points describing the most relevant highlights of a product. |  [optional] |
|**productLength** | [**ProductDimension**](ProductDimension.md) |  |  [optional] |
|**productTypes** | **List&lt;String&gt;** | Categories of the item (formatted as in product data specification). |  [optional] |
|**productWeight** | [**ProductWeight**](ProductWeight.md) |  |  [optional] |
|**productWidth** | [**ProductDimension**](ProductDimension.md) |  |  [optional] |
|**promotionIds** | **List&lt;String&gt;** | The unique ID of a promotion. |  [optional] |
|**salePrice** | [**Price**](Price.md) |  |  [optional] |
|**salePriceEffectiveDate** | **String** | Date range during which the item is on sale (see product data specification ). |  [optional] |
|**sellOnGoogleQuantity** | **String** | The quantity of the product that is available for selling on Google. Supported only for online products. |  [optional] |
|**shipping** | [**List&lt;ProductShipping&gt;**](ProductShipping.md) | Shipping rules. |  [optional] |
|**shippingHeight** | [**ProductShippingDimension**](ProductShippingDimension.md) |  |  [optional] |
|**shippingLabel** | **String** | The shipping label of the product, used to group product in account-level shipping rules. |  [optional] |
|**shippingLength** | [**ProductShippingDimension**](ProductShippingDimension.md) |  |  [optional] |
|**shippingWeight** | [**ProductShippingWeight**](ProductShippingWeight.md) |  |  [optional] |
|**shippingWidth** | [**ProductShippingDimension**](ProductShippingDimension.md) |  |  [optional] |
|**shoppingAdsExcludedCountries** | **List&lt;String&gt;** | List of country codes (ISO 3166-1 alpha-2) to exclude the offer from Shopping Ads destination. Countries from this list are removed from countries configured in MC feed settings. |  [optional] |
|**sizeSystem** | **String** | System in which the size is specified. Recommended for apparel items. |  [optional] |
|**sizeType** | **String** | The cut of the item. Recommended for apparel items. |  [optional] |
|**sizes** | **List&lt;String&gt;** | Size of the item. Only one value is allowed. For variants with different sizes, insert a separate product for each size with the same &#x60;itemGroupId&#x60; value (see size definition). |  [optional] |
|**source** | **String** | The source of the offer, that is, how the offer was created. Acceptable values are: - \&quot;&#x60;api&#x60;\&quot; - \&quot;&#x60;crawl&#x60;\&quot; - \&quot;&#x60;feed&#x60;\&quot;  |  [optional] |
|**subscriptionCost** | [**ProductSubscriptionCost**](ProductSubscriptionCost.md) |  |  [optional] |
|**targetCountry** | **String** | Required. The CLDR territory code for the item&#39;s country of sale. |  [optional] |
|**taxCategory** | **String** | The tax category of the product, used to configure detailed tax nexus in account-level tax settings. |  [optional] |
|**taxes** | [**List&lt;ProductTax&gt;**](ProductTax.md) | Tax information. |  [optional] |
|**title** | **String** | Title of the item. |  [optional] |
|**transitTimeLabel** | **String** | The transit time label of the product, used to group product in account-level transit time tables. |  [optional] |
|**unitPricingBaseMeasure** | [**ProductUnitPricingBaseMeasure**](ProductUnitPricingBaseMeasure.md) |  |  [optional] |
|**unitPricingMeasure** | [**ProductUnitPricingMeasure**](ProductUnitPricingMeasure.md) |  |  [optional] |
|**virtualModelLink** | **String** | URL of the 3D model of the item to provide more visuals. |  [optional] |



