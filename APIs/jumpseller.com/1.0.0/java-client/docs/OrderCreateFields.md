

# OrderCreateFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | [**CustomerFieldsWithBillingAddressAndShippingAddressFields**](CustomerFieldsWithBillingAddressAndShippingAddressFields.md) |  |  [optional] |
|**products** | [**List&lt;OrderProductOrderCreate&gt;**](OrderProductOrderCreate.md) |  |  [optional] |
|**shippingMethodId** | **Integer** | Shipping method id |  [optional] |
|**shippingMethodName** | **String** | Shipping method name e.g. Royal Mail |  [optional] |
|**shippingPrice** | **Float** | Shipping method&#39;s price (applicable if shipping_method_name is provided instead of a shipping_method_id) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Order |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;Abandoned&quot; |
| CANCELED | &quot;Canceled&quot; |
| PENDING_PAYMENT | &quot;Pending Payment&quot; |
| PAID | &quot;Paid&quot; |



