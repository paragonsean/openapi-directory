# LinodeApi.DatabaseMySQLRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowList** | **[String]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  | [optional] 
**clusterSize** | **Number** | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.  | [optional] [default to ClusterSizeEnum.1]
**encrypted** | **Boolean** | Whether the Managed Databases is encrypted. | [optional] [default to false]
**engine** | **String** | The Managed Database engine in engine/version format. | 
**label** | **String** | A unique, user-defined string referring to the Managed Database. | 
**region** | **String** | The [Region](/docs/api/regions/) ID for the Managed Database. | 
**replicationType** | **String** | The replication method used for the Managed Database.  Defaults to &#x60;none&#x60; for a single cluster and &#x60;semi_synch&#x60; for a high availability cluster.  Must be &#x60;none&#x60; for a single node cluster.  Must be &#x60;asynch&#x60; or &#x60;semi_synch&#x60; for a high availability cluster.  | [optional] 
**sslConnection** | **Boolean** | Whether to require SSL credentials to establish a connection to the Managed Database.  Use the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command for access information.  | [optional] [default to true]
**type** | **String** | The Linode Instance type used by the Managed Database for its nodes. | 



## Enum: ClusterSizeEnum


* `1` (value: `1`)

* `3` (value: `3`)





## Enum: ReplicationTypeEnum


* `none` (value: `"none"`)

* `asynch` (value: `"asynch"`)

* `semi_synch` (value: `"semi_synch"`)




