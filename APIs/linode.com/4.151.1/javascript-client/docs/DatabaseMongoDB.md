# LinodeApi.DatabaseMongoDB

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowList** | **[String]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  | [optional] 
**clusterSize** | **Number** | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.  | [optional] [default to ClusterSizeEnum.1]
**compressionType** | **String** | The type of data compression for this Database.  Snappy has a lower comparative compression ratio and resource consumption rate.  Zlip has a higher comparative compression ratio and resource consumption rate.  | [optional] [default to &#39;none&#39;]
**created** | **Date** | When this Managed Database was created. | [optional] [readonly] 
**encrypted** | **Boolean** | Whether the Managed Databases is encrypted. | [optional] [default to false]
**engine** | **String** | The Managed Database engine type. | [optional] [readonly] 
**hosts** | [**DatabaseMongoDBHosts**](DatabaseMongoDBHosts.md) |  | [optional] 
**id** | **Number** | A unique ID that can be used to identify and reference the Managed Database. | [optional] [readonly] 
**label** | **String** | A unique, user-defined string referring to the Managed Database. | [optional] 
**peers** | **[String]** | An array of peer addresses for this Database.  | [optional] 
**port** | **Number** | The access port for this Managed Database. | [optional] 
**region** | **String** | The [Region](/docs/api/regions/) ID for the Managed Database. | [optional] 
**replicaSet** | **String** | Label for configuring a MongoDB [replica set](https://www.mongodb.com/docs/manual/replication/). Choose the same label on multiple Databases to include them in the same replica set.  If &#x60;null&#x60;, the Database is not included in any replica set.  | [optional] 
**sslConnection** | **Boolean** | Whether to require SSL credentials to establish a connection to the Managed Database.  Use the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command for access information.  | [optional] [default to true]
**status** | **String** | The operating status of the Managed Database. | [optional] [readonly] 
**storageEngine** | **String** | The type of storage engine for this Database.  **Note:** MMAPV1 is not available for MongoDB versions 4.0 and above.  | [optional] [default to &#39;wiredtiger&#39;]
**type** | **String** | The Linode Instance type used by the Managed Database for its nodes. | [optional] 
**updated** | **Date** | When this Managed Database was last updated. | [optional] [readonly] 
**updates** | [**DatabaseUpdates**](DatabaseUpdates.md) |  | [optional] 
**version** | **String** | The Managed Database engine version. | [optional] [readonly] 



## Enum: ClusterSizeEnum


* `1` (value: `1`)

* `3` (value: `3`)





## Enum: CompressionTypeEnum


* `none` (value: `"none"`)

* `snappy` (value: `"snappy"`)

* `zlip` (value: `"zlip"`)





## Enum: StatusEnum


* `provisioning` (value: `"provisioning"`)

* `active` (value: `"active"`)

* `suspending` (value: `"suspending"`)

* `suspended` (value: `"suspended"`)

* `resuming` (value: `"resuming"`)

* `restoring` (value: `"restoring"`)

* `failed` (value: `"failed"`)

* `degraded` (value: `"degraded"`)

* `updating` (value: `"updating"`)

* `backing_up` (value: `"backing_up"`)





## Enum: StorageEngineEnum


* `mmapv1` (value: `"mmapv1"`)

* `wiredtiger` (value: `"wiredtiger"`)




