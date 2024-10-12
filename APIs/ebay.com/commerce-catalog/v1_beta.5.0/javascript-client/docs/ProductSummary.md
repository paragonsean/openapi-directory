# CatalogApi.ProductSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalImages** | [**[Image]**](Image.md) | Contains information about additional images associated with this product. For the primary image, see the &lt;b&gt;image&lt;/b&gt; container. | [optional] 
**aspects** | [**[Aspect]**](Aspect.md) | Contains an array of the category aspects and their values that are associated with this product. | [optional] 
**brand** | **String** | The manufacturer&#39;s brand name for this product. | [optional] 
**ean** | **[String]** | A list of all European Article Numbers (EANs) that identify this product. | [optional] 
**epid** | **String** | The eBay product ID of this product. | [optional] 
**gtin** | **[String]** | A list of all GTINs that identify this product. This includes all of the values returned in the &lt;b&gt;ean&lt;/b&gt;, &lt;b&gt;isbn&lt;/b&gt;, and &lt;b&gt;upc&lt;/b&gt; fields. | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**isbn** | **[String]** | A list of all International Standard Book Numbers (ISBNs) that identify this product. | [optional] 
**mpn** | **[String]** | A list of all Manufacturer Product Number (MPN) values that the manufacturer uses to identify this product. | [optional] 
**productHref** | **String** | The URI of the &lt;b&gt;getProduct&lt;/b&gt; call request that retrieves this product&#39;s details. | [optional] 
**productWebUrl** | **String** | The URL for this product&#39;s eBay product page. | [optional] 
**title** | **String** | The title of this product on eBay. | [optional] 
**upc** | **[String]** | A list of Universal Product Codes (UPCs) that identify this product. | [optional] 


