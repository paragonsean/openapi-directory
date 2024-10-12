# PosApi.Merchant

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**mainLocationId** | **String** | The main location ID of the merchant | [optional] 
**name** | **String** | The name of the merchant | [optional] 
**ownerId** | **String** |  | [optional] 
**serviceCharges** | [**[ServiceCharge]**](ServiceCharge.md) |  | [optional] 
**status** | **String** | Status of this merchant. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `other` (value: `"other"`)




