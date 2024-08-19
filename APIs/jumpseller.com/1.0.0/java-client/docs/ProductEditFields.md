

# ProductEditFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**barcode** | **String** | Barcode of the product |  [optional] |
|**categories** | [**List&lt;CategoryFields&gt;**](CategoryFields.md) |  |  [optional] |
|**description** | **String** | Description of the product |  [optional] |
|**diameter** | **Float** | Diameter of the product |  [optional] |
|**featured** | **Boolean** | True if the product is featured |  [optional] |
|**googleProductCategory** | **String** | Category of a Product based on the Google product taxonomy |  [optional] |
|**height** | **Float** | Height of the product |  [optional] |
|**length** | **Float** | Length of the product |  [optional] |
|**metaDescription** | **String** | SEO meta description of the product |  [optional] |
|**name** | **String** | Name of the product |  |
|**packageFormat** | [**PackageFormatEnum**](#PackageFormatEnum) | Format the product package |  [optional] |
|**pageTitle** | **String** | SEO title of the product |  [optional] |
|**permalink** | **String** | Product unique URL path |  [optional] |
|**price** | **Float** | Price of the product |  |
|**shippingRequired** | **Boolean** | False if the product is digital |  [optional] |
|**sku** | **String** | Stock Keeping Unit of the product |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the product |  [optional] |
|**stock** | **Integer** | Quantity in stock for the product |  [optional] |
|**stockUnlimited** | **Boolean** | True if the Product has unlimited stock |  [optional] |
|**weight** | **Float** | Weight of the product |  [optional] |
|**width** | **Float** | Width of the product |  [optional] |



## Enum: PackageFormatEnum

| Name | Value |
|---- | -----|
| BOX | &quot;box&quot; |
| CYLINDER | &quot;cylinder&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| NOT_AVAILABLE | &quot;not-available&quot; |
| DISABLED | &quot;disabled&quot; |



