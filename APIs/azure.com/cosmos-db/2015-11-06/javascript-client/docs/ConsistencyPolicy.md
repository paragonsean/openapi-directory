# CosmosDb.ConsistencyPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultConsistencyLevel** | **String** | The default consistency level and configuration settings of the Cosmos DB account. | 
**maxIntervalInSeconds** | **Number** | When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is 5 - 86400. Required when defaultConsistencyPolicy is set to &#39;BoundedStaleness&#39;. | [optional] 
**maxStalenessPrefix** | **Number** | When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is 1 – 2,147,483,647. Required when defaultConsistencyPolicy is set to &#39;BoundedStaleness&#39;. | [optional] 



## Enum: DefaultConsistencyLevelEnum


* `Eventual` (value: `"Eventual"`)

* `Session` (value: `"Session"`)

* `BoundedStaleness` (value: `"BoundedStaleness"`)

* `Strong` (value: `"Strong"`)

* `ConsistentPrefix` (value: `"ConsistentPrefix"`)




