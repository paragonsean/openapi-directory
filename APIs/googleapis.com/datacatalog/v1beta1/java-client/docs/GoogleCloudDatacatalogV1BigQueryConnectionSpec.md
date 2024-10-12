

# GoogleCloudDatacatalogV1BigQueryConnectionSpec

Specification for the BigQuery connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudSql** | [**GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec**](GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec.md) |  |  [optional] |
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) | The type of the BigQuery connection. |  [optional] |
|**hasCredential** | **Boolean** | True if there are credentials attached to the BigQuery connection; false otherwise. |  [optional] |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| CONNECTION_TYPE_UNSPECIFIED | &quot;CONNECTION_TYPE_UNSPECIFIED&quot; |
| CLOUD_SQL | &quot;CLOUD_SQL&quot; |



