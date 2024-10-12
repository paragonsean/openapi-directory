# PosApi.ServiceCharge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** |  | [optional] 
**amount** | **Number** |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**name** | **String** | Service charge name | [optional] 
**percentage** | **Number** | Service charge percentage. Use this field to calculate the amount of the service charge. Pass a percentage and amount at the same time. | [optional] 
**type** | **String** | The type of the service charge. | [optional] 



## Enum: TypeEnum


* `auto_gratuity` (value: `"auto_gratuity"`)

* `custom` (value: `"custom"`)




