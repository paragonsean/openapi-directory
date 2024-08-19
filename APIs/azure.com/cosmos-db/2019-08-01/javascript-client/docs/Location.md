# CosmosDb.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentEndpoint** | **String** | The connection endpoint for the specific region. Example: https://&amp;lt;accountName&amp;gt;-&amp;lt;locationName&amp;gt;.documents.azure.com:443/ | [optional] [readonly] 
**failoverPriority** | **Number** | The failover priority of the region. A failover priority of 0 indicates a write region. The maximum value for a failover priority &#x3D; (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. | [optional] 
**id** | **String** | The unique identifier of the region within the database account. Example: &amp;lt;accountName&amp;gt;-&amp;lt;locationName&amp;gt;. | [optional] [readonly] 
**isZoneRedundant** | **Boolean** | Flag to indicate whether or not this region is an AvailabilityZone region | [optional] 
**locationName** | **String** | The name of the region. | [optional] 
**provisioningState** | **String** | The status of the Cosmos DB account at the time the operation was called. The status can be one of following. &#39;Creating&#39; – the Cosmos DB account is being created. When an account is in Creating state, only properties that are specified as input for the Create Cosmos DB account operation are returned. &#39;Succeeded&#39; – the Cosmos DB account is active for use. &#39;Updating&#39; – the Cosmos DB account is being updated. &#39;Deleting&#39; – the Cosmos DB account is being deleted. &#39;Failed&#39; – the Cosmos DB account failed creation. | [optional] 


