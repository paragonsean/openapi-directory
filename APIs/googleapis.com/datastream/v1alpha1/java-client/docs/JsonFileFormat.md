

# JsonFileFormat

JSON file format configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compression** | [**CompressionEnum**](#CompressionEnum) | Compression of the loaded JSON file. |  [optional] |
|**schemaFileFormat** | [**SchemaFileFormatEnum**](#SchemaFileFormatEnum) | The schema file format along JSON data files. |  [optional] |



## Enum: CompressionEnum

| Name | Value |
|---- | -----|
| JSON_COMPRESSION_UNSPECIFIED | &quot;JSON_COMPRESSION_UNSPECIFIED&quot; |
| NO_COMPRESSION | &quot;NO_COMPRESSION&quot; |
| GZIP | &quot;GZIP&quot; |



## Enum: SchemaFileFormatEnum

| Name | Value |
|---- | -----|
| SCHEMA_FILE_FORMAT_UNSPECIFIED | &quot;SCHEMA_FILE_FORMAT_UNSPECIFIED&quot; |
| NO_SCHEMA_FILE | &quot;NO_SCHEMA_FILE&quot; |
| AVRO_SCHEMA_FILE | &quot;AVRO_SCHEMA_FILE&quot; |



