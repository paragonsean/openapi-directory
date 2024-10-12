

# DatabaseMongoDB

Managed MongoDB Databases object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowList** | **List&lt;String&gt;** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  |  [optional] |
|**clusterSize** | [**ClusterSizeEnum**](#ClusterSizeEnum) | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.  |  [optional] |
|**compressionType** | [**CompressionTypeEnum**](#CompressionTypeEnum) | The type of data compression for this Database.  Snappy has a lower comparative compression ratio and resource consumption rate.  Zlip has a higher comparative compression ratio and resource consumption rate.  |  [optional] |
|**created** | **OffsetDateTime** | When this Managed Database was created. |  [optional] [readonly] |
|**encrypted** | **Boolean** | Whether the Managed Databases is encrypted. |  [optional] |
|**engine** | **String** | The Managed Database engine type. |  [optional] [readonly] |
|**hosts** | [**DatabaseMongoDBHosts**](DatabaseMongoDBHosts.md) |  |  [optional] |
|**id** | **Integer** | A unique ID that can be used to identify and reference the Managed Database. |  [optional] [readonly] |
|**label** | **String** | A unique, user-defined string referring to the Managed Database. |  [optional] |
|**peers** | **List&lt;String&gt;** | An array of peer addresses for this Database.  |  [optional] |
|**port** | **Integer** | The access port for this Managed Database. |  [optional] |
|**region** | **String** | The [Region](/docs/api/regions/) ID for the Managed Database. |  [optional] |
|**replicaSet** | **String** | Label for configuring a MongoDB [replica set](https://www.mongodb.com/docs/manual/replication/). Choose the same label on multiple Databases to include them in the same replica set.  If &#x60;null&#x60;, the Database is not included in any replica set.  |  [optional] |
|**sslConnection** | **Boolean** | Whether to require SSL credentials to establish a connection to the Managed Database.  Use the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command for access information.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The operating status of the Managed Database. |  [optional] [readonly] |
|**storageEngine** | [**StorageEngineEnum**](#StorageEngineEnum) | The type of storage engine for this Database.  **Note:** MMAPV1 is not available for MongoDB versions 4.0 and above.  |  [optional] |
|**type** | **String** | The Linode Instance type used by the Managed Database for its nodes. |  [optional] |
|**updated** | **OffsetDateTime** | When this Managed Database was last updated. |  [optional] [readonly] |
|**updates** | [**DatabaseUpdates**](DatabaseUpdates.md) |  |  [optional] |
|**version** | **String** | The Managed Database engine version. |  [optional] [readonly] |



## Enum: ClusterSizeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_3 | 3 |



## Enum: CompressionTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| SNAPPY | &quot;snappy&quot; |
| ZLIP | &quot;zlip&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROVISIONING | &quot;provisioning&quot; |
| ACTIVE | &quot;active&quot; |
| SUSPENDING | &quot;suspending&quot; |
| SUSPENDED | &quot;suspended&quot; |
| RESUMING | &quot;resuming&quot; |
| RESTORING | &quot;restoring&quot; |
| FAILED | &quot;failed&quot; |
| DEGRADED | &quot;degraded&quot; |
| UPDATING | &quot;updating&quot; |
| BACKING_UP | &quot;backing_up&quot; |



## Enum: StorageEngineEnum

| Name | Value |
|---- | -----|
| MMAPV1 | &quot;mmapv1&quot; |
| WIREDTIGER | &quot;wiredtiger&quot; |



