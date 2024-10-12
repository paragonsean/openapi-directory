

# ReplicationRule

Specifies which S3 on Outposts objects to replicate and where to store the replicas.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ID** | [**String**](String.md) |  |  [optional] |
|**priority** | [**Integer**](Integer.md) |  |  [optional] |
|**prefix** | [**String**](String.md) |  |  [optional] |
|**filter** | [**ReplicationRuleFilter**](ReplicationRuleFilter.md) |  |  [optional] |
|**status** | [**ReplicationRuleStatus**](ReplicationRuleStatus.md) |  |  |
|**sourceSelectionCriteria** | [**ReplicationRuleSourceSelectionCriteria**](ReplicationRuleSourceSelectionCriteria.md) |  |  [optional] |
|**existingObjectReplication** | [**ReplicationRuleExistingObjectReplication**](ReplicationRuleExistingObjectReplication.md) |  |  [optional] |
|**destination** | [**ReplicationRuleDestination**](ReplicationRuleDestination.md) |  |  |
|**deleteMarkerReplication** | [**ReplicationRuleDeleteMarkerReplication**](ReplicationRuleDeleteMarkerReplication.md) |  |  [optional] |
|**bucket** | [**String**](String.md) |  |  |



