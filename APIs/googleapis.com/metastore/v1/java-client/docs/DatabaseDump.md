

# DatabaseDump

A specification of the location of and metadata about a database dump from a relational database management system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseType** | [**DatabaseTypeEnum**](#DatabaseTypeEnum) | The type of the database. |  [optional] |
|**gcsUri** | **String** | A Cloud Storage object or folder URI that specifies the source from which to import metadata. It must begin with gs://. |  [optional] |
|**sourceDatabase** | **String** | The name of the source database. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. The type of the database dump. If unspecified, defaults to MYSQL. |  [optional] |



## Enum: DatabaseTypeEnum

| Name | Value |
|---- | -----|
| DATABASE_TYPE_UNSPECIFIED | &quot;DATABASE_TYPE_UNSPECIFIED&quot; |
| MYSQL | &quot;MYSQL&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| MYSQL | &quot;MYSQL&quot; |
| AVRO | &quot;AVRO&quot; |



