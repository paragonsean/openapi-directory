

# DatabaseAccountGetProperties

Properties for the database account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;Capability&gt;**](Capability.md) | List of Cosmos DB capabilities for the account |  [optional] |
|**connectorOffer** | **ConnectorOffer** |  |  [optional] |
|**consistencyPolicy** | [**ConsistencyPolicy**](ConsistencyPolicy.md) |  |  [optional] |
|**databaseAccountOfferType** | **DatabaseAccountOfferType** |  |  [optional] |
|**disableKeyBasedMetadataWriteAccess** | **Boolean** | Disable write operations on metadata resources (databases, containers, throughput) via account keys |  [optional] |
|**documentEndpoint** | **String** | The connection endpoint for the Cosmos DB database account. |  [optional] [readonly] |
|**enableAutomaticFailover** | **Boolean** | Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account. |  [optional] |
|**enableCassandraConnector** | **Boolean** | Enables the cassandra connector on the Cosmos DB C* account |  [optional] |
|**enableMultipleWriteLocations** | **Boolean** | Enables the account to write in multiple locations |  [optional] |
|**failoverPolicies** | [**List&lt;FailoverPolicy&gt;**](FailoverPolicy.md) | An array that contains the regions ordered by their failover priorities. |  [optional] [readonly] |
|**ipRangeFilter** | **String** | Cosmos DB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces. |  [optional] |
|**isVirtualNetworkFilterEnabled** | **Boolean** | Flag to indicate whether to enable/disable Virtual Network ACL rules. |  [optional] |
|**keyVaultKeyUri** | **String** | The URI of the key vault |  [optional] |
|**locations** | [**List&lt;Location&gt;**](Location.md) | An array that contains all of the locations enabled for the Cosmos DB account. |  [optional] [readonly] |
|**provisioningState** | **String** | The status of the Cosmos DB account at the time the operation was called. The status can be one of following. &#39;Creating&#39; – the Cosmos DB account is being created. When an account is in Creating state, only properties that are specified as input for the Create Cosmos DB account operation are returned. &#39;Succeeded&#39; – the Cosmos DB account is active for use. &#39;Updating&#39; – the Cosmos DB account is being updated. &#39;Deleting&#39; – the Cosmos DB account is being deleted. &#39;Failed&#39; – the Cosmos DB account failed creation. |  [optional] |
|**readLocations** | [**List&lt;Location&gt;**](Location.md) | An array that contains of the read locations enabled for the Cosmos DB account. |  [optional] [readonly] |
|**virtualNetworkRules** | [**List&lt;VirtualNetworkRule&gt;**](VirtualNetworkRule.md) | List of Virtual Network ACL rules configured for the Cosmos DB account. |  [optional] |
|**writeLocations** | [**List&lt;Location&gt;**](Location.md) | An array that contains the write location for the Cosmos DB account. |  [optional] [readonly] |



