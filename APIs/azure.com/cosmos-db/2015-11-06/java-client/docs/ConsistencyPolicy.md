

# ConsistencyPolicy

The consistency policy for the Cosmos DB database account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultConsistencyLevel** | [**DefaultConsistencyLevelEnum**](#DefaultConsistencyLevelEnum) | The default consistency level and configuration settings of the Cosmos DB account. |  |
|**maxIntervalInSeconds** | **Integer** | When used with the Bounded Staleness consistency level, this value represents the time amount of staleness (in seconds) tolerated. Accepted range for this value is 5 - 86400. Required when defaultConsistencyPolicy is set to &#39;BoundedStaleness&#39;. |  [optional] |
|**maxStalenessPrefix** | **Long** | When used with the Bounded Staleness consistency level, this value represents the number of stale requests tolerated. Accepted range for this value is 1 – 2,147,483,647. Required when defaultConsistencyPolicy is set to &#39;BoundedStaleness&#39;. |  [optional] |



## Enum: DefaultConsistencyLevelEnum

| Name | Value |
|---- | -----|
| EVENTUAL | &quot;Eventual&quot; |
| SESSION | &quot;Session&quot; |
| BOUNDED_STALENESS | &quot;BoundedStaleness&quot; |
| STRONG | &quot;Strong&quot; |
| CONSISTENT_PREFIX | &quot;ConsistentPrefix&quot; |



