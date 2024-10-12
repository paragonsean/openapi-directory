# MySqlManagementClient.ServerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administratorLogin** | **String** | The administrator&#39;s login name of a server. Can only be specified when the server is being created (and is required for creation). | [optional] 
**earliestRestoreDate** | **Date** | Earliest restore point creation time (ISO8601 format) | [optional] 
**fullyQualifiedDomainName** | **String** | The fully qualified domain name of a server. | [optional] 
**masterServerId** | **String** | The master server id of a replica server. | [optional] 
**replicaCapacity** | **Number** | The maximum number of replicas that a master server can have. | [optional] 
**replicationRole** | **String** | The replication role of the server. | [optional] 
**sslEnforcement** | [**SslEnforcement**](SslEnforcement.md) |  | [optional] 
**storageProfile** | [**StorageProfile**](StorageProfile.md) |  | [optional] 
**userVisibleState** | **String** | A state of a server that is visible to user. | [optional] 
**version** | [**ServerVersion**](ServerVersion.md) |  | [optional] 



## Enum: UserVisibleStateEnum


* `Ready` (value: `"Ready"`)

* `Dropping` (value: `"Dropping"`)

* `Disabled` (value: `"Disabled"`)




