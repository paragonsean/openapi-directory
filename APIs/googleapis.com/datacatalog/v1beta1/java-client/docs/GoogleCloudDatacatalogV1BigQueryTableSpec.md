

# GoogleCloudDatacatalogV1BigQueryTableSpec

Describes a BigQuery table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableSourceType** | [**TableSourceTypeEnum**](#TableSourceTypeEnum) | Output only. The table source type. |  [optional] [readonly] |
|**tableSpec** | [**GoogleCloudDatacatalogV1TableSpec**](GoogleCloudDatacatalogV1TableSpec.md) |  |  [optional] |
|**viewSpec** | [**GoogleCloudDatacatalogV1ViewSpec**](GoogleCloudDatacatalogV1ViewSpec.md) |  |  [optional] |



## Enum: TableSourceTypeEnum

| Name | Value |
|---- | -----|
| TABLE_SOURCE_TYPE_UNSPECIFIED | &quot;TABLE_SOURCE_TYPE_UNSPECIFIED&quot; |
| BIGQUERY_VIEW | &quot;BIGQUERY_VIEW&quot; |
| BIGQUERY_TABLE | &quot;BIGQUERY_TABLE&quot; |
| BIGQUERY_MATERIALIZED_VIEW | &quot;BIGQUERY_MATERIALIZED_VIEW&quot; |



