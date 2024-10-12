

# FailoverGroupProperties

Properties of a failover group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databases** | **List&lt;String&gt;** | List of databases in the failover group. |  [optional] |
|**partnerServers** | [**List&lt;PartnerInfo&gt;**](PartnerInfo.md) | List of partner server information for the failover group. |  |
|**readOnlyEndpoint** | [**FailoverGroupReadOnlyEndpoint**](FailoverGroupReadOnlyEndpoint.md) |  |  [optional] |
|**readWriteEndpoint** | [**FailoverGroupReadWriteEndpoint**](FailoverGroupReadWriteEndpoint.md) |  |  |
|**replicationRole** | [**ReplicationRoleEnum**](#ReplicationRoleEnum) | Local replication role of the failover group instance. |  [optional] [readonly] |
|**replicationState** | **String** | Replication state of the failover group instance. |  [optional] [readonly] |



## Enum: ReplicationRoleEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



