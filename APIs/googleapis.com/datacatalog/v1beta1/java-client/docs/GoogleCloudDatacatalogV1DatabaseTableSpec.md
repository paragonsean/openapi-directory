

# GoogleCloudDatacatalogV1DatabaseTableSpec

Specification that applies to a table resource. Valid only for entries with the `TABLE` type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseViewSpec** | [**GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec**](GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec.md) |  |  [optional] |
|**dataplexTable** | [**GoogleCloudDatacatalogV1DataplexTableSpec**](GoogleCloudDatacatalogV1DataplexTableSpec.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this table. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TABLE_TYPE_UNSPECIFIED | &quot;TABLE_TYPE_UNSPECIFIED&quot; |
| NATIVE | &quot;NATIVE&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |



