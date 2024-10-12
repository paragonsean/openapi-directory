

# MongoDBCollectionResource

Cosmos DB MongoDB collection resource object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Name of the Cosmos DB MongoDB collection |  |
|**indexes** | [**List&lt;MongoIndex&gt;**](MongoIndex.md) | List of index keys |  [optional] |
|**shardKey** | **Map&lt;String, String&gt;** | The shard key and partition kind pair, only support \&quot;Hash\&quot; partition kind |  [optional] |



