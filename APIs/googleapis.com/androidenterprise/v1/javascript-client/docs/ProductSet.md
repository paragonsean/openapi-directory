# GooglePlayEmmApi.ProductSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**productId** | **[String]** | The list of product IDs making up the set of products. | [optional] 
**productSetBehavior** | **String** | The interpretation of this product set. \&quot;unknown\&quot; should never be sent and is ignored if received. \&quot;whitelist\&quot; means that the user is entitled to access the product set. \&quot;includeAll\&quot; means that all products are accessible, including products that are approved, products with revoked approval, and products that have never been approved. \&quot;allApproved\&quot; means that the user is entitled to access all products that are approved for the enterprise. If the value is \&quot;allApproved\&quot; or \&quot;includeAll\&quot;, the productId field is ignored. If no value is provided, it is interpreted as \&quot;whitelist\&quot; for backwards compatibility. Further \&quot;allApproved\&quot; or \&quot;includeAll\&quot; does not enable automatic visibility of \&quot;alpha\&quot; or \&quot;beta\&quot; tracks for Android app. Use ProductVisibility to enable \&quot;alpha\&quot; or \&quot;beta\&quot; tracks per user. | [optional] 
**productVisibility** | [**[ProductVisibility]**](ProductVisibility.md) | Additional list of product IDs making up the product set. Unlike the productID array, in this list It&#39;s possible to specify which tracks (alpha, beta, production) of a product are visible to the user. See ProductVisibility and its fields for more information. Specifying the same product ID both here and in the productId array is not allowed and it will result in an error. | [optional] 



## Enum: ProductSetBehaviorEnum


* `unknown` (value: `"unknown"`)

* `whitelist` (value: `"whitelist"`)

* `includeAll` (value: `"includeAll"`)

* `allApproved` (value: `"allApproved"`)




