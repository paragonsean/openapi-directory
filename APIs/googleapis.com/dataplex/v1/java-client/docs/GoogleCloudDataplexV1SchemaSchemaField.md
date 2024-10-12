

# GoogleCloudDataplexV1SchemaSchemaField

Represents a column field within a table schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. User friendly field description. Must be less than or equal to 1024 characters. |  [optional] |
|**fields** | [**List&lt;GoogleCloudDataplexV1SchemaSchemaField&gt;**](GoogleCloudDataplexV1SchemaSchemaField.md) | Optional. Any nested field for complex types. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Required. Additional field semantics. |  [optional] |
|**name** | **String** | Required. The name of the field. Must contain only letters, numbers and underscores, with a maximum length of 767 characters, and must begin with a letter or underscore. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of field. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| REQUIRED | &quot;REQUIRED&quot; |
| NULLABLE | &quot;NULLABLE&quot; |
| REPEATED | &quot;REPEATED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| BYTE | &quot;BYTE&quot; |
| INT16 | &quot;INT16&quot; |
| INT32 | &quot;INT32&quot; |
| INT64 | &quot;INT64&quot; |
| FLOAT | &quot;FLOAT&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| DECIMAL | &quot;DECIMAL&quot; |
| STRING | &quot;STRING&quot; |
| BINARY | &quot;BINARY&quot; |
| TIMESTAMP | &quot;TIMESTAMP&quot; |
| DATE | &quot;DATE&quot; |
| TIME | &quot;TIME&quot; |
| RECORD | &quot;RECORD&quot; |
| NULL | &quot;NULL&quot; |



