# CloudVisionApi.GoogleCloudVisionV1p4beta1Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | User-provided metadata to be stored with this product. Must be at most 4096 characters long. | [optional] 
**displayName** | **String** | The user-provided name for this Product. Must not be empty. Must be at most 4096 characters long. | [optional] 
**name** | **String** | The resource name of the product. Format is: &#x60;projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID&#x60;. This field is ignored when creating a product. | [optional] 
**productCategory** | **String** | Immutable. The category for the product identified by the reference image. This should be one of \&quot;homegoods-v2\&quot;, \&quot;apparel-v2\&quot;, \&quot;toys-v2\&quot;, \&quot;packagedgoods-v1\&quot; or \&quot;general-v1\&quot;. The legacy categories \&quot;homegoods\&quot;, \&quot;apparel\&quot;, and \&quot;toys\&quot; are still supported, but these should not be used for new products. | [optional] 
**productLabels** | [**[GoogleCloudVisionV1p4beta1ProductKeyValue]**](GoogleCloudVisionV1p4beta1ProductKeyValue.md) | Key-value pairs that can be attached to a product. At query time, constraints can be specified based on the product_labels. Note that integer values can be provided as strings, e.g. \&quot;1199\&quot;. Only strings with integer values can match a range-based restriction which is to be supported soon. Multiple values can be assigned to the same key. One product may have up to 500 product_labels. Notice that the total number of distinct product_labels over all products in one ProductSet cannot exceed 1M, otherwise the product search pipeline will refuse to work for that ProductSet. | [optional] 


