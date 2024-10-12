# JumpsellerApi.ShippingMethodFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | URL that receives the shipping data and returns rates | [optional] 
**city** | **String** | City/Municipality name of origin | [optional] 
**fetchServicesUrl** | **String** | URL that returns available shipping services | [optional] 
**id** | **Number** | Unique identifier of the Shipping Method | [optional] 
**name** | **String** | Name of the Shipping Method | [optional] 
**postal** | **String** | Postal/Zipcode of origin | [optional] 
**services** | [**[ShippingService]**](ShippingService.md) |  | [optional] 
**state** | **String** | State/Region code of origin | [optional] 
**type** | **String** | Type of the Shipping Method | [optional] 



## Enum: TypeEnum


* `free` (value: `"free"`)

* `tables` (value: `"tables"`)

* `correiosbr` (value: `"correiosbr"`)

* `correos_chile` (value: `"correos_chile"`)

* `chilexpress` (value: `"chilexpress"`)

* `flat` (value: `"flat"`)

* `ups` (value: `"ups"`)

* `external` (value: `"external"`)




