

# ApiProductsListByApis200ResponseValueInner

Product profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approvalRequired** | **Boolean** | whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of true. |  [optional] |
|**description** | **String** | Product description. May include HTML formatting tags. |  [optional] |
|**id** | **String** | Uniquely identifies the product within the current API Management service instance. The value is a valid relative URL in the format of /products/{productId} where {productId} is a product identifier. |  [optional] [readonly] |
|**name** | **String** | Product name. |  |
|**state** | [**StateEnum**](#StateEnum) | whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is NotPublished. |  [optional] |
|**subscriptionRequired** | **Boolean** | Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as \&quot;protected\&quot; and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as \&quot;open\&quot; and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it&#39;s value is assumed to be true. |  [optional] |
|**subscriptionsLimit** | **Integer** | Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of true. |  [optional] |
|**terms** | **String** | Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NOT_PUBLISHED | &quot;NotPublished&quot; |
| PUBLISHED | &quot;Published&quot; |



