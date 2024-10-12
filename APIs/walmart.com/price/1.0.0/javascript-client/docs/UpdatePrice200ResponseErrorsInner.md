# PriceManagement.UpdatePrice200ResponseErrorsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** |  | [optional] 
**causes** | [**[UpdatePrice200ResponseErrorsInnerCausesInner]**](UpdatePrice200ResponseErrorsInnerCausesInner.md) |  | [optional] 
**code** | **String** |  | 
**component** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**errorIdentifiers** | **{String: Object}** |  | [optional] 
**field** | **String** |  | [optional] 
**gatewayErrorCategory** | **String** |  | [optional] 
**info** | **String** |  | [optional] 
**serviceName** | **String** |  | [optional] 
**severity** | **String** |  | [optional] 
**type** | **String** |  | [optional] 



## Enum: CategoryEnum


* `APPLICATION` (value: `"APPLICATION"`)

* `SYSTEM` (value: `"SYSTEM"`)

* `REQUEST` (value: `"REQUEST"`)

* `DATA` (value: `"DATA"`)





## Enum: GatewayErrorCategoryEnum


* `INTERNAL_DATA_ERROR` (value: `"INTERNAL_DATA_ERROR"`)

* `EXTERNAL_DATA_ERROR` (value: `"EXTERNAL_DATA_ERROR"`)

* `SYSTEM_ERROR` (value: `"SYSTEM_ERROR"`)





## Enum: SeverityEnum


* `INFO` (value: `"INFO"`)

* `WARN` (value: `"WARN"`)

* `ERROR` (value: `"ERROR"`)




