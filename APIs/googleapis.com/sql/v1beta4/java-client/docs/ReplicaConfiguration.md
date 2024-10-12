

# ReplicaConfiguration

Read-replica configuration for connecting to the primary instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cascadableReplica** | **Boolean** | Optional. Specifies if a SQL Server replica is a cascadable replica. A cascadable replica is a SQL Server cross region replica that supports replica(s) under it. |  [optional] |
|**failoverTarget** | **Boolean** | Specifies if the replica is the failover target. If the field is set to &#x60;true&#x60; the replica will be designated as a failover replica. In case the primary instance fails, the replica instance will be promoted as the new primary instance. Only one replica can be specified as failover target, and the replica has to be in different zone with the primary instance. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#replicaConfiguration&#x60;. |  [optional] |
|**mysqlReplicaConfiguration** | [**MySqlReplicaConfiguration**](MySqlReplicaConfiguration.md) |  |  [optional] |



