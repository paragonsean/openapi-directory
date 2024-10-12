# CatalogApiSellerPortal.PostProduct200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[AttributesInner]**](AttributesInner.md) | Attributes of the product. Attributes are additional properties used to create site browsing filters. | 
**brandId** | **String** | Product&#39;s Brand unique identifier number. | 
**brandName** | **String** | Name of the Brand associated with the product. | 
**categoryIds** | **[String]** | Product&#39;s Categories unique identifier numbers. It can have multiples IDs for each Category and Subcategories. | 
**categoryNames** | **[String]** | Names of the product&#39;s categories, displayed in a path format. | 
**createdAt** | **String** | Date when the product was created. | 
**externalId** | **String** | Product reference unique identifier number in the store. | [optional] 
**id** | **String** | Product&#39;s unique identifier number. | [optional] 
**images** | [**[ImagesInner]**](ImagesInner.md) | Information of the images of the product. | 
**name** | **String** | Product Name. Use simple words and avoid other languages or complex writing. This field is essential for SEO and must respect the 150 character limit. | 
**origin** | **String** | Origin account of the product. It is not possible to alter products where the origin is &#x60;marketplace&#x60;. | 
**skus** | [**[SkusInner1]**](SkusInner1.md) | SKUs of the product. | 
**slug** | **String** | Reference of the product in the URL of the store. | 
**specs** | [**[SpecsInner1]**](SpecsInner1.md) | Specifications that will differentiate the possible product SKUs. | 
**status** | **String** | Status of the product. Its values can be &#x60;active&#x60; or &#x60;inactive&#x60;. | 
**taxCode** | **String** | Product tax code. | [optional] 
**transportModal** | **String** | Transport modal of the product. | [optional] 
**updatedAt** | **String** | Last date when the product was updated. | 


