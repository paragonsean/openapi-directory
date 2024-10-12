

# ProductFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**barcode** | **String** | Barcode of the product |  [optional] |
|**categories** | [**List&lt;CategoryFields&gt;**](CategoryFields.md) |  |  [optional] |
|**createdAt** | **String** | Date of product creation |  [optional] |
|**description** | **String** | Description of the product |  [optional] |
|**diameter** | **Float** | Diameter of the product |  [optional] |
|**discount** | **Float** | Discount of the product |  [optional] |
|**featured** | **Boolean** | True if the product is featured |  [optional] |
|**googleProductCategory** | **String** | Category of a Product based on the Google product taxonomy |  [optional] |
|**height** | **Float** | Height of the product |  [optional] |
|**id** | **Integer** | Unique identifier of the product |  [optional] |
|**images** | [**List&lt;ImageFields&gt;**](ImageFields.md) |  |  [optional] |
|**length** | **Float** | Length of the product |  [optional] |
|**name** | **String** | Name of the product |  [optional] |
|**packageFormat** | [**PackageFormatEnum**](#PackageFormatEnum) | Format the product package |  [optional] |
|**permalink** | **String** | Product unique URL path |  [optional] |
|**price** | **Float** | Price of the product |  [optional] |
|**sku** | **String** | Stock Keeping Unit of the product |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the product |  [optional] |
|**stock** | **Integer** | Quantity in stock for the product |  [optional] |
|**stockUnlimited** | **Boolean** | True if the Product has unlimited stock |  [optional] |
|**variants** | [**List&lt;VariantFields&gt;**](VariantFields.md) |  |  [optional] |
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



