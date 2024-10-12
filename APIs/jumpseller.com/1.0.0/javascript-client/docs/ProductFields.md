# JumpsellerApi.ProductFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **String** | Barcode of the product | [optional] 
**categories** | [**[CategoryFields]**](CategoryFields.md) |  | [optional] 
**createdAt** | **String** | Date of product creation | [optional] 
**description** | **String** | Description of the product | [optional] 
**diameter** | **Number** | Diameter of the product | [optional] 
**discount** | **Number** | Discount of the product | [optional] 
**featured** | **Boolean** | True if the product is featured | [optional] [default to false]
**googleProductCategory** | **String** | Category of a Product based on the Google product taxonomy | [optional] 
**height** | **Number** | Height of the product | [optional] 
**id** | **Number** | Unique identifier of the product | [optional] 
**images** | [**[ImageFields]**](ImageFields.md) |  | [optional] 
**length** | **Number** | Length of the product | [optional] 
**name** | **String** | Name of the product | [optional] 
**packageFormat** | **String** | Format the product package | [optional] [default to &#39;box&#39;]
**permalink** | **String** | Product unique URL path | [optional] 
**price** | **Number** | Price of the product | [optional] 
**sku** | **String** | Stock Keeping Unit of the product | [optional] 
**status** | **String** | Status of the product | [optional] [default to &#39;available&#39;]
**stock** | **Number** | Quantity in stock for the product | [optional] [default to 100]
**stockUnlimited** | **Boolean** | True if the Product has unlimited stock | [optional] 
**variants** | [**[VariantFields]**](VariantFields.md) |  | [optional] 
**weight** | **Number** | Weight of the product | [optional] [default to 1]
**width** | **Number** | Width of the product | [optional] 



## Enum: PackageFormatEnum


* `box` (value: `"box"`)

* `cylinder` (value: `"cylinder"`)





## Enum: StatusEnum


* `available` (value: `"available"`)

* `not-available` (value: `"not-available"`)

* `disabled` (value: `"disabled"`)




