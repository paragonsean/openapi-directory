

# ProductImageAdd


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | Content(body) encoded in base64 of image file |  [optional] |
|**imageName** | **String** | Defines image&#39;s name |  |
|**label** | **String** | Defines alternative text that has to be attached to the picture |  [optional] |
|**langId** | **String** | Add product image on specified language id |  [optional] |
|**mime** | **String** | Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. |  [optional] |
|**position** | **Integer** | Defines image’s position in the list |  [optional] |
|**productId** | **String** | Defines product id where the image should be added |  [optional] |
|**productVariantId** | **Integer** | Defines product&#39;s variants specified by variant id |  [optional] |
|**storeId** | **String** | Store Id |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Defines image&#39;s types that are specified by comma-separated list |  |
|**url** | **String** | Defines URL of the image that has to be added |  [optional] |
|**variantIds** | **String** | Defines product&#39;s variants ids |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SMALL | &quot;small&quot; |
| BASE | &quot;base&quot; |
| ADDITIONAL | &quot;additional&quot; |
| THUMBNAIL | &quot;thumbnail&quot; |



