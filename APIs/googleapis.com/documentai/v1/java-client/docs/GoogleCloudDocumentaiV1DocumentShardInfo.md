

# GoogleCloudDocumentaiV1DocumentShardInfo

For a large document, sharding may be performed to produce several document shards. Each document shard contains this field to detail which shard it is.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**shardCount** | **String** | Total number of shards. |  [optional] |
|**shardIndex** | **String** | The 0-based index of this shard. |  [optional] |
|**textOffset** | **String** | The index of the first character in Document.text in the overall document global text. |  [optional] |



