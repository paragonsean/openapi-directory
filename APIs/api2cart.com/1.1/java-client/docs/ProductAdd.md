

# ProductAdd


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeName** | **String** | Defines product’s attribute name separated with a comma in Magento |  [optional] |
|**attributeSetName** | **String** | Defines product’s attribute set name in Magento |  [optional] |
|**availFrom** | **String** | Allows to schedule a time in the future that the item becomes available. The value should be greater than the current date and time. |  [optional] |
|**availableForSale** | **Boolean** | Specifies the set of visible/invisible products for sale |  [optional] |
|**availableForView** | **Boolean** | Specifies the set of visible/invisible products for users |  [optional] |
|**backorderStatus** | **String** | Set backorder status |  [optional] |
|**barcode** | **String** | A barcode is a unique code composed of numbers used as a product identifier. |  [optional] |
|**bestOffer** | **List&lt;String&gt;** | The price at which Best Offers are automatically accepted.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:&lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;&lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;best_offer[&lt;b&gt;minimum_offer_price&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;best_offer[&lt;b&gt;auto_accept_price&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;&lt;/code&gt;&lt;/div&gt;&lt;/div&gt; |  [optional] |
|**brandName** | **String** | Retrieves brands specified by brand name |  [optional] |
|**categoriesIds** | **String** | Defines product add that is specified by comma-separated categories id |  [optional] |
|**categoryId** | **String** | Defines product add that is specified by category id |  [optional] |
|**clearCache** | **Boolean** | Is cache clear required |  [optional] |
|**condition** | **String** | The human-readable label for the condition (e.g., \&quot;New\&quot;). |  [optional] |
|**costPrice** | **BigDecimal** | Defines new product&#39;s cost price |  [optional] |
|**countryOfOrigin** | **String** | The country where the inventory item was made |  [optional] |
|**createdAt** | **String** | Defines the date of entity creation |  [optional] |
|**description** | **String** | Defines product&#39;s description that has to be added |  |
|**downloadable** | **Boolean** | Defines whether the product is downloadable |  [optional] |
|**ean** | **String** | European Article Number. An EAN is a unique 8 or 13-digit identifier that many industries (such as book publishers) use to identify products. |  [optional] |
|**files** | [**List&lt;ProductAddFilesInner&gt;**](ProductAddFilesInner.md) | File Url |  [optional] |
|**groupPrices** | [**List&lt;ProductAddGroupPricesInner&gt;**](ProductAddGroupPricesInner.md) | Defines product&#39;s group prices |  [optional] |
|**gtin** | **String** | Global Trade Item Number. An GTIN is an identifier for trade items. |  [optional] |
|**harmonizedSystemCode** | **String** | Harmonized System Code. An HSC is a 6-digit identifier that allows participating countries to classify traded goods on a common basis for customs purposes |  [optional] |
|**height** | **BigDecimal** | Defines product&#39;s height |  [optional] |
|**imageName** | **String** | Defines image&#39;s name |  [optional] |
|**imageUrl** | **String** | Image Url |  [optional] |
|**isbn** | **String** | International Standard Book Number. An ISBN is a unique identifier for books. |  [optional] |
|**langId** | **String** | Language id |  [optional] |
|**length** | **BigDecimal** | Defines product&#39;s length |  [optional] |
|**listingDuration** | **String** | Describes the number of days the seller wants the listing to be active. Look at cart.info method response for allowed values. |  [optional] |
|**listingType** | **String** | Indicates the selling format of the marketplace listing. |  [optional] |
|**manageStock** | **Boolean** | Defines inventory tracking for product |  [optional] |
|**manufacturer** | **String** | Defines product&#39;s manufacturer |  [optional] |
|**marketplaceItemProperties** | **String** | String containing the JSON representation of the supplied data |  [optional] |
|**metaDescription** | **String** | Defines unique meta description of a entity |  [optional] |
|**metaKeywords** | **String** | Defines unique meta keywords for each entity |  [optional] |
|**metaTitle** | **String** | Defines unique meta title for each entity |  [optional] |
|**model** | **String** | Defines product&#39;s model that has to be added |  |
|**mpn** | **String** | Manufacturer Part Number. A MPN is an identifier of a particular part design or material used. |  [optional] |
|**name** | **String** | Defines product&#39;s name that has to be added |  |
|**oldPrice** | **BigDecimal** | Defines product&#39;s old price |  [optional] |
|**orderedCount** | **Integer** | Defines how many times the product was ordered |  [optional] |
|**packageDetails** | **List&lt;String&gt;** | If the seller is subscribed to \&quot;Business Policies\&quot;, use the seller_profiles instead of the shipping_details, payment_methods and return_accepted params.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:&lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;&lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;package_details[&lt;b&gt;measure_unit&lt;/b&gt;] &#x3D; string&lt;/br&gt; Allowed measure_unit values: [English or Metric] &lt;/br&gt; Default: Metric&lt;/br&gt;package_details[&lt;b&gt;weigh_unit&lt;/b&gt;] &#x3D; string&lt;/br&gt; Allowed weigh_unit values: [kg, g, lbs, oz]&lt;/br&gt;package_details[&lt;b&gt;package_depth&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;package_details[&lt;b&gt;package_length&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;package_details[&lt;b&gt;package_width&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;package_details[&lt;b&gt;weight_major&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;package_details[&lt;b&gt;weight_minor&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;package_details[&lt;b&gt;shipping_package&lt;/b&gt;] &#x3D; string&lt;/br&gt; See cart.info method, param &#x60;eBay_shipping_package_details&#x60;&lt;/code&gt;&lt;/div&gt;&lt;/div&gt; |  [optional] |
|**paymentMethods** | **List&lt;String&gt;** | Identifies the payment method (such as PayPal) that the seller will accept when the buyer pays for the item. Look at cart.info method response for allowed values.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:&lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;&lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;payment_methods[0] &#x3D; string&lt;/br&gt;payment_methods[1] &#x3D; string&lt;/br&gt;&lt;/code&gt;&lt;/div&gt;&lt;/div&gt; |  [optional] |
|**paypalEmail** | **String** | Valid PayPal email address for the PayPal account that the seller will use if they offer PayPal as a payment method for the listing. |  [optional] |
|**price** | **BigDecimal** | Defines product&#39;s price that has to be added |  |
|**productClass** | **String** | A categorization for the product |  [optional] |
|**quantity** | **BigDecimal** | Defines product&#39;s quantity that has to be added |  [optional] |
|**returnAccepted** | **Boolean** | Indicates whether the seller allows the buyer to return the item. |  [optional] |
|**salesTax** | **List&lt;String&gt;** | Percent of an item&#39;s price to be charged as the sales tax for the order. Look at cart.info method response for allowed values.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:&lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;&lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;sales_tax[&lt;b&gt;tax_percent&lt;/b&gt;] &#x3D; decimal (##.###)&lt;/br&gt;sales_tax[&lt;b&gt;tax_state&lt;/b&gt;] &#x3D; string&lt;/br&gt;sales_tax[&lt;b&gt;shipping_inc_in_tax&lt;/b&gt;] &#x3D; bool&lt;/br&gt;&lt;/code&gt;&lt;/div&gt;&lt;/div&gt; |  [optional] |
|**searchKeywords** | **String** | Defines unique search keywords |  [optional] |
|**sellerProfiles** | [**ProductAddSellerProfiles**](ProductAddSellerProfiles.md) |  |  [optional] |
|**seoUrl** | **String** | Defines unique URL for SEO |  [optional] |
|**shippingDetails** | [**List&lt;ProductAddShippingDetailsInner&gt;**](ProductAddShippingDetailsInner.md) | The shipping details, including flat and calculated shipping costs and shipping insurance costs. Look at cart.info method response for allowed values.&lt;hr&gt;&lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:&lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;&lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;shipping_details[0][&lt;b&gt;shipping_type&lt;/b&gt;] &#x3D; string &lt;/br&gt;shipping_details[0][&lt;b&gt;shipping_service&lt;/b&gt;] &#x3D; string&lt;/br&gt;shipping_details[0][&lt;b&gt;shipping_cost&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;shipping_details[1][&lt;b&gt;shipping_type&lt;/b&gt;] &#x3D; string &lt;/br&gt;shipping_details[1][&lt;b&gt;shipping_service&lt;/b&gt;] &#x3D; string&lt;/br&gt;shipping_details[1][&lt;b&gt;shipping_cost&lt;/b&gt;] &#x3D; decimal&lt;/br&gt;&lt;/code&gt;&lt;/div&gt;&lt;/div&gt; |  [optional] |
|**shippingTemplateId** | **Integer** | The numeric ID of the shipping template associated with the products in Etsy. |  [optional] |
|**shortDescription** | **String** | Defines short description |  [optional] |
|**sku** | **String** | Defines product&#39;s sku that has to be added |  [optional] |
|**specialPrice** | **BigDecimal** | Defines product&#39;s model that has to be added |  [optional] |
|**specifics** | **List&lt;String&gt;** | An array of Item Specific Name/Value pairs used by the seller to provide descriptive details of an item in a structured manner.         &lt;hr&gt;         &lt;div style&#x3D;\&quot;font-style:normal\&quot;&gt;Param structure:           &lt;div style&#x3D;\&quot;margin-left: 2%;\&quot;&gt;             &lt;code style&#x3D;\&quot;padding:0; background-color:#ffffff;font-size:85%;font-family:monospace;\&quot;&gt;               specifics[int][&lt;b&gt;name&lt;/b&gt;] &#x3D; string&lt;/br&gt;               specifics[int][&lt;b&gt;value&lt;/b&gt;] &#x3D; string&lt;/br&gt;             &lt;/code&gt;           &lt;/div&gt;         &lt;/div&gt; |  [optional] |
|**spriceCreate** | **String** | Defines the date of special price creation |  [optional] |
|**spriceExpire** | **String** | Defines the term of special price offer duration |  [optional] |
|**spriceModified** | **String** | Defines the date of special price modification |  [optional] |
|**status** | **String** | Defines product&#39;s status |  [optional] |
|**storeId** | **String** | Store Id |  [optional] |
|**storesIds** | **String** | Assign product to the stores that is specified by comma-separated stores&#39; id |  [optional] |
|**tags** | **String** | Product tags |  [optional] |
|**taxClassId** | **String** | Defines tax classes where entity has to be added |  [optional] |
|**taxable** | **Boolean** | Specifies whether a tax is charged |  [optional] |
|**tierPrices** | [**List&lt;ProductAddTierPricesInner&gt;**](ProductAddTierPricesInner.md) | Defines product&#39;s tier prices |  [optional] |
|**type** | **String** | Defines product&#39;s type |  [optional] |
|**upc** | **String** | Universal Product Code. A UPC (UPC-A) is a commonly used identifer for many different products. |  [optional] |
|**url** | **String** | Defines unique product&#39;s URL |  [optional] |
|**viewedCount** | **Integer** | Specifies the number of product&#39;s reviews |  [optional] |
|**visible** | **String** | Set visibility status |  [optional] |
|**warehouseId** | **String** | This parameter is used for selecting a warehouse where you need to set/modify a product quantity. |  [optional] |
|**weight** | **BigDecimal** | Weight |  [optional] |
|**weightUnit** | **String** | Weight Unit |  [optional] |
|**wholesalePrice** | **BigDecimal** | Defines product&#39;s sale price |  [optional] |
|**width** | **BigDecimal** | Defines product&#39;s width |  [optional] |



