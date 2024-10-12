# CatalogApi.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalImages** | [**[Image]**](Image.md) | Contains information about  additional images associated with this product. For the primary image, see the &lt;b&gt;image&lt;/b&gt; container. | [optional] 
**aspects** | [**[Aspect]**](Aspect.md) | Contains an array of the category aspects and their values that are associated with this product. | [optional] 
**brand** | **String** | The manufacturer&#39;s brand name for this product. | [optional] 
**description** | **String** | The rich description of this product, which might contain HTML. | [optional] 
**ean** | **[String]** | A list of all European Article Numbers (EANs) that identify this product. | [optional] 
**epid** | **String** | The eBay product ID of this product. | [optional] 
**gtin** | **[String]** | A list of all GTINs that identify this product. Currently this can include EAN, ISBN, and UPC identifier types. | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**isbn** | **[String]** | A list of all International Standard Book Numbers (ISBNs) that identify this product.  | [optional] 
**mpn** | **[String]** | A list of all MPN values that the manufacturer uses to identify this product. | [optional] 
**otherApplicableCategoryIds** | **[String]** | A list of category IDs (other than the value of &lt;b&gt;primaryCategoryId&lt;/b&gt;) for all the leaf categories to which this product might belong. | [optional] 
**primaryCategoryId** | **String** | The identifier of the leaf category that eBay recommends using to list this product, based on previous listings of similar products. Products in the eBay catalog are not automatically associated with any particular category, but using an inappropriate category can make it difficult for prospective buyers to find the product. For other possible categories that might be used, see &lt;b&gt;otherApplicableCategoryIds&lt;/b&gt;. | [optional] 
**productWebUrl** | **String** | The URL for this product&#39;s eBay product page. | [optional] 
**title** | **String** | The title of this product on eBay. | [optional] 
**upc** | **[String]** | A list of Universal Product Codes (UPCs) that identify this product. | [optional] 
**version** | **String** | The current version number of this product record in the catalog. | [optional] 


