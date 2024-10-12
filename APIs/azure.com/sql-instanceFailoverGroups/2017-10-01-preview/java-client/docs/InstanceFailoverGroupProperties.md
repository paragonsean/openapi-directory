

# InstanceFailoverGroupProperties

Properties of a instance failover group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managedInstancePairs** | [**List&lt;ManagedInstancePairInfo&gt;**](ManagedInstancePairInfo.md) | List of managed instance pairs in the failover group. |  |
|**partnerRegions** | [**List&lt;PartnerRegionInfo&gt;**](PartnerRegionInfo.md) | Partner region information for the failover group. |  |
|**readOnlyEndpoint** | [**InstanceFailoverGroupReadOnlyEndpoint**](InstanceFailoverGroupReadOnlyEndpoint.md) |  |  [optional] |
|**readWriteEndpoint** | [**InstanceFailoverGroupReadWriteEndpoint**](InstanceFailoverGroupReadWriteEndpoint.md) |  |  |
|**replicationRole** | [**ReplicationRoleEnum**](#ReplicationRoleEnum) | Local replication role of the failover group instance. |  [optional] [readonly] |
|**replicationState** | **String** | Replication state of the failover group instance. |  [optional] [readonly] |



## Enum: ReplicationRoleEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



