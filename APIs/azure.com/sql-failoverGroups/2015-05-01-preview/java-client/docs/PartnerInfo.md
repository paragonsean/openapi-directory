

# PartnerInfo

Partner server information for the failover group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Resource identifier of the partner server. |  |
|**location** | **String** | Geo location of the partner server. |  [optional] [readonly] |
|**replicationRole** | [**ReplicationRoleEnum**](#ReplicationRoleEnum) | Replication role of the partner server. |  [optional] [readonly] |



## Enum: ReplicationRoleEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;Primary&quot; |
| SECONDARY | &quot;Secondary&quot; |



