# AzureMlWebServicesManagementClient.ColumnSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_enum** | **[Object]** | If the data type is categorical, this provides the list of accepted categories. | [optional] 
**format** | **String** | Additional format information for the data type. | [optional] 
**type** | **String** | Data type of the column. | 
**xMsIsnullable** | **Boolean** | Flag indicating if the type supports null values or not. | [optional] 
**xMsIsordered** | **Boolean** | Flag indicating whether the categories are treated as an ordered set or not, if this is a categorical column. | [optional] 



## Enum: FormatEnum


* `Byte` (value: `"Byte"`)

* `Char` (value: `"Char"`)

* `Complex64` (value: `"Complex64"`)

* `Complex128` (value: `"Complex128"`)

* `Date-time` (value: `"Date-time"`)

* `Date-timeOffset` (value: `"Date-timeOffset"`)

* `Double` (value: `"Double"`)

* `Duration` (value: `"Duration"`)

* `Float` (value: `"Float"`)

* `Int8` (value: `"Int8"`)

* `Int16` (value: `"Int16"`)

* `Int32` (value: `"Int32"`)

* `Int64` (value: `"Int64"`)

* `Uint8` (value: `"Uint8"`)

* `Uint16` (value: `"Uint16"`)

* `Uint32` (value: `"Uint32"`)

* `Uint64` (value: `"Uint64"`)





## Enum: TypeEnum


* `Boolean` (value: `"Boolean"`)

* `Integer` (value: `"Integer"`)

* `Number` (value: `"Number"`)

* `String` (value: `"String"`)




