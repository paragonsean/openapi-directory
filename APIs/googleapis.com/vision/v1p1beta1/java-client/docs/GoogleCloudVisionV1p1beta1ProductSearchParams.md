

# GoogleCloudVisionV1p1beta1ProductSearchParams

Parameters for a product search request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingPoly** | [**GoogleCloudVisionV1p1beta1BoundingPoly**](GoogleCloudVisionV1p1beta1BoundingPoly.md) |  |  [optional] |
|**filter** | **String** | The filtering expression. This can be used to restrict search results based on Product labels. We currently support an AND of OR of key-value expressions, where each expression within an OR must have the same key. An &#39;&#x3D;&#39; should be used to connect the key and value. For example, \&quot;(color &#x3D; red OR color &#x3D; blue) AND brand &#x3D; Google\&quot; is acceptable, but \&quot;(color &#x3D; red OR brand &#x3D; Google)\&quot; is not acceptable. \&quot;color: red\&quot; is not acceptable because it uses a &#39;:&#39; instead of an &#39;&#x3D;&#39;. |  [optional] |
|**productCategories** | **List&lt;String&gt;** | The list of product categories to search in. Currently, we only consider the first category, and either \&quot;homegoods-v2\&quot;, \&quot;apparel-v2\&quot;, \&quot;toys-v2\&quot;, \&quot;packagedgoods-v1\&quot;, or \&quot;general-v1\&quot; should be specified. The legacy categories \&quot;homegoods\&quot;, \&quot;apparel\&quot;, and \&quot;toys\&quot; are still supported but will be deprecated. For new products, please use \&quot;homegoods-v2\&quot;, \&quot;apparel-v2\&quot;, or \&quot;toys-v2\&quot; for better product search accuracy. It is recommended to migrate existing products to these categories as well. |  [optional] |
|**productSet** | **String** | The resource name of a ProductSet to be searched for similar images. Format is: &#x60;projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID&#x60;. |  [optional] |



