

# ServerProperties

The properties of a server.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**administratorLogin** | **String** | The administrator&#39;s login name of a server. Can only be specified when the server is being created (and is required for creation). |  [optional] |
|**earliestRestoreDate** | **OffsetDateTime** | Earliest restore point creation time (ISO8601 format) |  [optional] |
|**fullyQualifiedDomainName** | **String** | The fully qualified domain name of a server. |  [optional] |
|**masterServerId** | **String** | The master server id of a replica server. |  [optional] |
|**replicaCapacity** | **Integer** | The maximum number of replicas that a master server can have. |  [optional] |
|**replicationRole** | **String** | The replication role of the server. |  [optional] |
|**sslEnforcement** | **SslEnforcement** |  |  [optional] |
|**storageProfile** | [**StorageProfile**](StorageProfile.md) |  |  [optional] |
|**userVisibleState** | [**UserVisibleStateEnum**](#UserVisibleStateEnum) | A state of a server that is visible to user. |  [optional] |
|**version** | **ServerVersion** |  |  [optional] |



## Enum: UserVisibleStateEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| DROPPING | &quot;Dropping&quot; |
| DISABLED | &quot;Disabled&quot; |



