# ViatorApiDocumentationAmpSpecificationMerchantPartners.TaxonomyCategories200ResponseAllOfDataInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupName** | **String** | **natural-language name** of *this* product category | [optional] 
**groupUrlName** | **String** | **URL-formatted name** of *this* product category | [optional] 
**id** | **Number** | **unique numeric identifier** for the category | [optional] 
**productCount** | **Number** | **number** of products in this category in the destination specified by &#x60;destId&#x60; - **note**: will be &#x60;null&#x60; if no &#x60;destId&#x60; is included in the query  | [optional] 
**subcategories** | [**[TaxonomyCategories200ResponseAllOfDataInnerSubcategoriesInner]**](TaxonomyCategories200ResponseAllOfDataInnerSubcategoriesInner.md) | **array** of subcategory objects | [optional] 
**thumbnailURL** | **String** | **URL** for this category&#39;s thumbnail image, selected from the most popular product within the category - **note:** will be &#x60;null&#x60; if no &#x60;destId&#x60; is included in the query  | [optional] 


