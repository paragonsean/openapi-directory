# JumpsellerApi.OrderCreateFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**CustomerFieldsWithBillingAddressAndShippingAddressFields**](CustomerFieldsWithBillingAddressAndShippingAddressFields.md) |  | [optional] 
**products** | [**[OrderProductOrderCreate]**](OrderProductOrderCreate.md) |  | [optional] 
**shippingMethodId** | **Number** | Shipping method id | [optional] 
**shippingMethodName** | **String** | Shipping method name e.g. Royal Mail | [optional] 
**shippingPrice** | **Number** | Shipping method&#39;s price (applicable if shipping_method_name is provided instead of a shipping_method_id) | [optional] 
**status** | **String** | Status of the Order | [optional] 



## Enum: StatusEnum


* `Abandoned` (value: `"Abandoned"`)

* `Canceled` (value: `"Canceled"`)

* `Pending Payment` (value: `"Pending Payment"`)

* `Paid` (value: `"Paid"`)




