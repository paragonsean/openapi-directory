# Suggestions.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandId** | **Number** | Marketplace&#39;s Brand ID that the product belongs to, configured in the Catalog. It should be the brand chosen for the received SKU to be matched with. The brandId is already mapped through the Get Suggestions API. This field is nulled when the inserted value is 0. | [default to 1234567]
**categoryId** | **Number** | Marketplace&#39;s Category ID that the product belongs to, configured in the Catalog. It should be the category chosen for the received SKU to be matched with. The &#x60;categoryId&#x60; is already mapped through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). You can choose to keep the same suggested &#x60;categoryID&#x60;, or overwrite it with another value in this request. This field is nulled when the inserted value is 0. | [default to 12]
**description** | **String** | Product&#39;s description. | [default to &#39;Description of the product, how it will appear on the marketplace.&#39;]
**name** | **String** | Name of the product that will be matched. | [default to &#39;Book&#39;]
**specifications** | **String** | This field is optional. Add here any product specifications or details. | [default to &#39;&#39;]


