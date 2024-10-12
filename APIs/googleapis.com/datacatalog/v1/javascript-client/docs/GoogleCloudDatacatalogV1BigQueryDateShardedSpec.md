# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1BigQueryDateShardedSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Output only. The Data Catalog resource name of the dataset entry the current table belongs to. For example: &#x60;projects/{PROJECT_ID}/locations/{LOCATION}/entrygroups/{ENTRY_GROUP_ID}/entries/{ENTRY_ID}&#x60;. | [optional] [readonly] 
**latestShardResource** | **String** | Output only. BigQuery resource name of the latest shard. | [optional] [readonly] 
**shardCount** | **String** | Output only. Total number of shards. | [optional] [readonly] 
**tablePrefix** | **String** | Output only. The table name prefix of the shards. The name of any given shard is &#x60;[table_prefix]YYYYMMDD&#x60;. For example, for the &#x60;MyTable20180101&#x60; shard, the &#x60;table_prefix&#x60; is &#x60;MyTable&#x60;. | [optional] [readonly] 


