# AirbyteConfigurationApi.FieldTransform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addField** | [**FieldAdd**](FieldAdd.md) |  | [optional] 
**breaking** | **Boolean** |  | 
**fieldName** | **[String]** | A field name is a list of strings that form the path to the field. | 
**removeField** | [**FieldRemove**](FieldRemove.md) |  | [optional] 
**transformType** | **String** |  | 
**updateFieldSchema** | [**FieldSchemaUpdate**](FieldSchemaUpdate.md) |  | [optional] 



## Enum: TransformTypeEnum


* `add_field` (value: `"add_field"`)

* `remove_field` (value: `"remove_field"`)

* `update_field_schema` (value: `"update_field_schema"`)




