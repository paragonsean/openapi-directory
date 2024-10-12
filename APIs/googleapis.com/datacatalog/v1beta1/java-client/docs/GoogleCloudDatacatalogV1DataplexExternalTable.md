

# GoogleCloudDatacatalogV1DataplexExternalTable

External table registered by Dataplex. Dataplex publishes data discovered from an asset into multiple other systems (BigQuery, DPMS) in form of tables. We call them \"external tables\". External tables are also synced into the Data Catalog. This message contains pointers to those external tables (fully qualified name, resource name et cetera) within the Data Catalog.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataCatalogEntry** | **String** | Name of the Data Catalog entry representing the external table. |  [optional] |
|**fullyQualifiedName** | **String** | Fully qualified name (FQN) of the external table. |  [optional] |
|**googleCloudResource** | **String** | Google Cloud resource name of the external table. |  [optional] |
|**system** | [**SystemEnum**](#SystemEnum) | Service in which the external table is registered. |  [optional] |



## Enum: SystemEnum

| Name | Value |
|---- | -----|
| INTEGRATED_SYSTEM_UNSPECIFIED | &quot;INTEGRATED_SYSTEM_UNSPECIFIED&quot; |
| BIGQUERY | &quot;BIGQUERY&quot; |
| CLOUD_PUBSUB | &quot;CLOUD_PUBSUB&quot; |
| DATAPROC_METASTORE | &quot;DATAPROC_METASTORE&quot; |
| DATAPLEX | &quot;DATAPLEX&quot; |
| CLOUD_SPANNER | &quot;CLOUD_SPANNER&quot; |
| CLOUD_BIGTABLE | &quot;CLOUD_BIGTABLE&quot; |
| CLOUD_SQL | &quot;CLOUD_SQL&quot; |
| LOOKER | &quot;LOOKER&quot; |
| VERTEX_AI | &quot;VERTEX_AI&quot; |



