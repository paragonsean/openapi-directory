

# FieldTransform

Describes the difference between two Streams.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addField** | [**FieldAdd**](FieldAdd.md) |  |  [optional] |
|**breaking** | **Boolean** |  |  |
|**fieldName** | **List&lt;String&gt;** | A field name is a list of strings that form the path to the field. |  |
|**removeField** | [**FieldRemove**](FieldRemove.md) |  |  [optional] |
|**transformType** | [**TransformTypeEnum**](#TransformTypeEnum) |  |  |
|**updateFieldSchema** | [**FieldSchemaUpdate**](FieldSchemaUpdate.md) |  |  [optional] |



## Enum: TransformTypeEnum

| Name | Value |
|---- | -----|
| ADD_FIELD | &quot;add_field&quot; |
| REMOVE_FIELD | &quot;remove_field&quot; |
| UPDATE_FIELD_SCHEMA | &quot;update_field_schema&quot; |



