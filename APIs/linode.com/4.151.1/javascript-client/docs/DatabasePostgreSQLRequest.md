# LinodeApi.DatabasePostgreSQLRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowList** | **[String]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  | [optional] 
**clusterSize** | **Number** | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.  | [optional] [default to ClusterSizeEnum.1]
**encrypted** | **Boolean** | Whether the Managed Databases is encrypted. | [optional] [default to false]
**engine** | **String** | The Managed Database engine in engine/version format. | 
**label** | **String** | A unique, user-defined string referring to the Managed Database. | 
**region** | **String** | The [Region](/docs/api/regions/) ID for the Managed Database. | 
**replicationCommitType** | **String** | The synchronization level of the replicating server.  Must be &#x60;local&#x60; or &#x60;off&#x60; for the &#x60;asynch&#x60; replication type.  Must be &#x60;on&#x60;, &#x60;remote_write&#x60;, or &#x60;remote_apply&#x60; for the &#x60;semi_synch&#x60; replication type.  | [optional] [default to &#39;local&#39;]
**replicationType** | **String** | The replication method used for the Managed Database.  Defaults to &#x60;none&#x60; for a single cluster and &#x60;semi_synch&#x60; for a high availability cluster.  Must be &#x60;none&#x60; for a single node cluster.  Must be &#x60;asynch&#x60; or &#x60;semi_synch&#x60; for a high availability cluster.  | [optional] 
**sslConnection** | **Boolean** | Whether to require SSL credentials to establish a connection to the Managed Database.  Use the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command for access information.  | [optional] [default to true]
**type** | **String** | The Linode Instance type used by the Managed Database for its nodes. | 



## Enum: ClusterSizeEnum


* `1` (value: `1`)

* `3` (value: `3`)





## Enum: ReplicationCommitTypeEnum


* `true` (value: `"true"`)

* `local` (value: `"local"`)

* `remote_write` (value: `"remote_write"`)

* `remote_apply` (value: `"remote_apply"`)

* `false` (value: `"false"`)





## Enum: ReplicationTypeEnum


* `none` (value: `"none"`)

* `asynch` (value: `"asynch"`)

* `semi_synch` (value: `"semi_synch"`)




