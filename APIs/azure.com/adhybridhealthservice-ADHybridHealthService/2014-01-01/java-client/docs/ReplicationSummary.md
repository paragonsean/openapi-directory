

# ReplicationSummary

The replication summary for a domain controller.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | **String** | The domain name for a given domain controller. |  [optional] |
|**inboundNeighborCollection** | [**List&lt;InboundReplicationNeighbor&gt;**](InboundReplicationNeighbor.md) | List of individual domain controller neighbor&#39;s inbound replication status. |  [optional] |
|**lastAttemptedSync** | **OffsetDateTime** | The last time when a sync was attempted for a given domain controller. |  [optional] |
|**lastSuccessfulSync** | **OffsetDateTime** | The time when the last successful sync happened for a given domain controller. |  [optional] |
|**site** | **String** | The site name for a given domain controller. |  [optional] |
|**status** | **Integer** | The health status for a domain controller. |  [optional] |
|**targetServer** | **String** | The domain controller name. |  [optional] |



