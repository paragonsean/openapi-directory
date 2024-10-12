# CatalogApi.ApiCatalogPvtProductProductIdPutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adWordsRemarketingCode** | **String** | This is a legacy field. Do not take this information into consideration. | [optional] 
**brandId** | **Number** | Brand ID associated with this product. | 
**categoryId** | **Number** | Category ID associated with this product. | 
**departmentId** | **Number** | Department ID according to the product&#39;s category. | [optional] 
**description** | **String** | Product description. | [optional] 
**descriptionShort** | **String** | Short product description. This information can be displayed on both the product page and the shelf, using the following controls:   Store Framework:  &#x60;$product.DescriptionShort&#x60;.   Legacy CMS Portal: &#x60;&lt;vtex.cmc:productDescriptionShort/&gt;&#x60;.   | [optional] 
**isActive** | **Boolean** | Activate (&#x60;true&#x60;) or inactivate (&#x60;false&#x60;) product. | [optional] 
**isVisible** | **Boolean** | Shows (&#x60;true&#x60;) or hides (&#x60;false&#x60;) the product in search result and product pages, but the product can still be added to the shopping cart. Usually applicable for gifts. | [optional] 
**keyWords** | **String** | Store Framework: Deprecated.   Legacy CMS Portal: Keywords or synonyms related to the product, separated by comma (&#x60;,&#x60;). \&quot;Television\&quot;, for example, can have a substitute word like \&quot;TV\&quot;. This field is important to make your searches more comprehensive.   | [optional] 
**linkId** | **String** | Slug that will be used to build the product page URL. If it not informed, it will be generated according to the product&#39;s name replacing spaces and special characters by hyphens (&#x60;-&#x60;). | [optional] 
**lomadeeCampaignCode** | **String** | This is a legacy field. Do not take this information into consideration. | [optional] 
**metaTagDescription** | **String** | Brief description of the product for SEO. It is recommended not to exceed 150 characters. | [optional] 
**name** | **String** | Product&#39;s name. Limited to 150 characters. | 
**refId** | **String** | Product Reference Code. | [optional] 
**releaseDate** | **String** | Used to assist in the ordering of the search result of the site. Using the &#x60;O&#x3D;OrderByReleaseDateDESC&#x60; query string, you can pull this value and show the display order by release date. This attribute is also used as a condition for dynamic collections. | [optional] 
**score** | **Number** | Value used to set the priority on the search result page. | [optional] 
**showWithoutStock** | **Boolean** | If &#x60;true&#x60;, activates the [Notify Me](https://help.vtex.com/en/tutorial/setting-up-the-notify-me-option--2VqVifQuf6Co2KG048Yu6e) option when the product is out of stock. | [optional] 
**supplierId** | **Number** |  | [optional] 
**taxCode** | **String** | Product tax code, used for tax calculation. | [optional] 
**title** | **String** | Product&#39;s Title tag. Limited to 150 characters. It is presented in the browser tab and corresponds to the title of the product page. This field is important for SEO. | [optional] 


