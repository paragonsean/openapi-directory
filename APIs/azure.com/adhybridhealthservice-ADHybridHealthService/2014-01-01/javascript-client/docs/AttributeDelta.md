# AdHybridHealthService.AttributeDelta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multiValued** | **Boolean** | Indicates if the attribute delta is multivalued or not. | [optional] 
**name** | **String** | The name of the attribute delta. | [optional] 
**operationType** | **String** | The attribute delta operation type. | [optional] 
**valueType** | **String** | The value type. | [optional] 
**values** | [**[ValueDelta]**](ValueDelta.md) | The delta values. | [optional] 



## Enum: OperationTypeEnum


* `Undefined` (value: `"Undefined"`)

* `Add` (value: `"Add"`)

* `Replace` (value: `"Replace"`)

* `Update` (value: `"Update"`)

* `Delete` (value: `"Delete"`)





## Enum: ValueTypeEnum


* `Undefined` (value: `"Undefined"`)

* `Dn` (value: `"Dn"`)

* `Binary` (value: `"Binary"`)

* `String` (value: `"String"`)

* `Integer` (value: `"Integer"`)

* `Boolean` (value: `"Boolean"`)




