

# UpdateSourceServerReplicationTypeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountID** | **String** | Account ID on which to update replication type. |  [optional] |
|**replicationType** | [**ReplicationTypeEnum**](#ReplicationTypeEnum) | Replication type to which to update source server. |  |
|**sourceServerID** | **String** | ID of source server on which to update replication type. |  |



## Enum: ReplicationTypeEnum

| Name | Value |
|---- | -----|
| AGENT_BASED | &quot;AGENT_BASED&quot; |
| SNAPSHOT_SHIPPING | &quot;SNAPSHOT_SHIPPING&quot; |



