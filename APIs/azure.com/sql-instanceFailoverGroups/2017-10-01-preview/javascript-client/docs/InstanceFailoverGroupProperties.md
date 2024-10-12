# SqlManagementClient.InstanceFailoverGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managedInstancePairs** | [**[ManagedInstancePairInfo]**](ManagedInstancePairInfo.md) | List of managed instance pairs in the failover group. | 
**partnerRegions** | [**[PartnerRegionInfo]**](PartnerRegionInfo.md) | Partner region information for the failover group. | 
**readOnlyEndpoint** | [**InstanceFailoverGroupReadOnlyEndpoint**](InstanceFailoverGroupReadOnlyEndpoint.md) |  | [optional] 
**readWriteEndpoint** | [**InstanceFailoverGroupReadWriteEndpoint**](InstanceFailoverGroupReadWriteEndpoint.md) |  | 
**replicationRole** | **String** | Local replication role of the failover group instance. | [optional] [readonly] 
**replicationState** | **String** | Replication state of the failover group instance. | [optional] [readonly] 



## Enum: ReplicationRoleEnum


* `Primary` (value: `"Primary"`)

* `Secondary` (value: `"Secondary"`)




