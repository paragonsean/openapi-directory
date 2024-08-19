

# MongoDBCollectionGetPropertiesResource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Name of the Cosmos DB MongoDB collection |  |
|**indexes** | [**List&lt;MongoIndex&gt;**](MongoIndex.md) | List of index keys |  [optional] |
|**shardKey** | **Map&lt;String, String&gt;** | The shard key and partition kind pair, only support \&quot;Hash\&quot; partition kind |  [optional] |
|**etag** | **String** | A system generated property representing the resource etag required for optimistic concurrency control. |  [optional] [readonly] |
|**rid** | **String** | A system generated property. A unique identifier. |  [optional] [readonly] |
|**ts** | **Object** | A system generated property that denotes the last updated timestamp of the resource. |  [optional] [readonly] |



