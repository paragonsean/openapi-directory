

# DatabaseAccountCreateUpdateProperties

Properties to create and update Azure Cosmos DB database accounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;Capability&gt;**](Capability.md) | List of Cosmos DB capabilities for the account |  [optional] |
|**connectorOffer** | **ConnectorOffer** |  |  [optional] |
|**consistencyPolicy** | [**ConsistencyPolicy**](ConsistencyPolicy.md) |  |  [optional] |
|**databaseAccountOfferType** | **DatabaseAccountOfferType** |  |  |
|**disableKeyBasedMetadataWriteAccess** | **Boolean** | Disable write operations on metadata resources (databases, containers, throughput) via account keys |  [optional] |
|**enableAutomaticFailover** | **Boolean** | Enables automatic failover of the write region in the rare event that the region is unavailable due to an outage. Automatic failover will result in a new write region for the account and is chosen based on the failover priorities configured for the account. |  [optional] |
|**enableCassandraConnector** | **Boolean** | Enables the cassandra connector on the Cosmos DB C* account |  [optional] |
|**enableMultipleWriteLocations** | **Boolean** | Enables the account to write in multiple locations |  [optional] |
|**ipRangeFilter** | **String** | Cosmos DB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IPs for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces. |  [optional] |
|**isVirtualNetworkFilterEnabled** | **Boolean** | Flag to indicate whether to enable/disable Virtual Network ACL rules. |  [optional] |
|**keyVaultKeyUri** | **String** | The URI of the key vault |  [optional] |
|**locations** | [**List&lt;Location&gt;**](Location.md) | An array that contains the georeplication locations enabled for the Cosmos DB account. |  |
|**virtualNetworkRules** | [**List&lt;VirtualNetworkRule&gt;**](VirtualNetworkRule.md) | List of Virtual Network ACL rules configured for the Cosmos DB account. |  [optional] |



