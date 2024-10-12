

# GoogleCloudDataplexV1SchemaPartitionField

Represents a key field within the entity's partition structure. You could have up to 20 partition fields, but only the first 10 partitions have the filtering ability due to performance consideration. Note: Partition fields are immutable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. Partition field name must consist of letters, numbers, and underscores only, with a maximum of length of 256 characters, and must begin with a letter or underscore.. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Immutable. The type of field. |  [optional] |



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



