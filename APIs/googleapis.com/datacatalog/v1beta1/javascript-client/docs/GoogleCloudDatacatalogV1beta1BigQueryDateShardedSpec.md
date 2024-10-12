# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **String** | Output only. The Data Catalog resource name of the dataset entry the current table belongs to, for example, &#x60;projects/{project_id}/locations/{location}/entrygroups/{entry_group_id}/entries/{entry_id}&#x60;. | [optional] [readonly] 
**shardCount** | **String** | Output only. Total number of shards. | [optional] [readonly] 
**tablePrefix** | **String** | Output only. The table name prefix of the shards. The name of any given shard is &#x60;[table_prefix]YYYYMMDD&#x60;, for example, for shard &#x60;MyTable20180101&#x60;, the &#x60;table_prefix&#x60; is &#x60;MyTable&#x60;. | [optional] [readonly] 


