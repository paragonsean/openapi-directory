

# ShippingMethodFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUrl** | **String** | URL that receives the shipping data and returns rates |  [optional] |
|**city** | **String** | City/Municipality name of origin |  [optional] |
|**fetchServicesUrl** | **String** | URL that returns available shipping services |  [optional] |
|**id** | **Integer** | Unique identifier of the Shipping Method |  [optional] |
|**name** | **String** | Name of the Shipping Method |  [optional] |
|**postal** | **String** | Postal/Zipcode of origin |  [optional] |
|**services** | [**List&lt;ShippingService&gt;**](ShippingService.md) |  |  [optional] |
|**state** | **String** | State/Region code of origin |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Shipping Method |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FREE | &quot;free&quot; |
| TABLES | &quot;tables&quot; |
| CORREIOSBR | &quot;correiosbr&quot; |
| CORREOS_CHILE | &quot;correos_chile&quot; |
| CHILEXPRESS | &quot;chilexpress&quot; |
| FLAT | &quot;flat&quot; |
| UPS | &quot;ups&quot; |
| EXTERNAL | &quot;external&quot; |



