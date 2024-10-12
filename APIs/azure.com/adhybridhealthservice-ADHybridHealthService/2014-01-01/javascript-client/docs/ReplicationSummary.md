# AdHybridHealthService.ReplicationSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **String** | The domain name for a given domain controller. | [optional] 
**inboundNeighborCollection** | [**[InboundReplicationNeighbor]**](InboundReplicationNeighbor.md) | List of individual domain controller neighbor&#39;s inbound replication status. | [optional] 
**lastAttemptedSync** | **Date** | The last time when a sync was attempted for a given domain controller. | [optional] 
**lastSuccessfulSync** | **Date** | The time when the last successful sync happened for a given domain controller. | [optional] 
**site** | **String** | The site name for a given domain controller. | [optional] 
**status** | **Number** | The health status for a domain controller. | [optional] 
**targetServer** | **String** | The domain controller name. | [optional] 


