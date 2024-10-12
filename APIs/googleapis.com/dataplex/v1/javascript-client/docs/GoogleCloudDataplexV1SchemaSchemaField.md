# CloudDataplexApi.GoogleCloudDataplexV1SchemaSchemaField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. User friendly field description. Must be less than or equal to 1024 characters. | [optional] 
**fields** | [**[GoogleCloudDataplexV1SchemaSchemaField]**](GoogleCloudDataplexV1SchemaSchemaField.md) | Optional. Any nested field for complex types. | [optional] 
**mode** | **String** | Required. Additional field semantics. | [optional] 
**name** | **String** | Required. The name of the field. Must contain only letters, numbers and underscores, with a maximum length of 767 characters, and must begin with a letter or underscore. | [optional] 
**type** | **String** | Required. The type of field. | [optional] 



## Enum: ModeEnum


* `MODE_UNSPECIFIED` (value: `"MODE_UNSPECIFIED"`)

* `REQUIRED` (value: `"REQUIRED"`)

* `NULLABLE` (value: `"NULLABLE"`)

* `REPEATED` (value: `"REPEATED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `BOOLEAN` (value: `"BOOLEAN"`)

* `BYTE` (value: `"BYTE"`)

* `INT16` (value: `"INT16"`)

* `INT32` (value: `"INT32"`)

* `INT64` (value: `"INT64"`)

* `FLOAT` (value: `"FLOAT"`)

* `DOUBLE` (value: `"DOUBLE"`)

* `DECIMAL` (value: `"DECIMAL"`)

* `STRING` (value: `"STRING"`)

* `BINARY` (value: `"BINARY"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `DATE` (value: `"DATE"`)

* `TIME` (value: `"TIME"`)

* `RECORD` (value: `"RECORD"`)

* `NULL` (value: `"NULL"`)




