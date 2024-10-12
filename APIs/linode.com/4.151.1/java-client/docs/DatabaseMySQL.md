

# DatabaseMySQL

Managed MySQL Databases object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowList** | **List&lt;String&gt;** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  |  [optional] |
|**clusterSize** | [**ClusterSizeEnum**](#ClusterSizeEnum) | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes.  |  [optional] |
|**created** | **OffsetDateTime** | When this Managed Database was created. |  [optional] [readonly] |
|**encrypted** | **Boolean** | Whether the Managed Databases is encrypted. |  [optional] |
|**engine** | **String** | The Managed Database engine type. |  [optional] [readonly] |
|**hosts** | [**DatabaseHosts**](DatabaseHosts.md) |  |  [optional] |
|**id** | **Integer** | A unique ID that can be used to identify and reference the Managed Database. |  [optional] [readonly] |
|**label** | **String** | A unique, user-defined string referring to the Managed Database. |  [optional] |
|**port** | **Integer** | The access port for this Managed Database. |  [optional] |
|**region** | **String** | The [Region](/docs/api/regions/) ID for the Managed Database. |  [optional] |
|**replicationType** | [**ReplicationTypeEnum**](#ReplicationTypeEnum) | The replication method used for the Managed Database.  Defaults to &#x60;none&#x60; for a single cluster and &#x60;semi_synch&#x60; for a high availability cluster.  Must be &#x60;none&#x60; for a single node cluster.  Must be &#x60;asynch&#x60; or &#x60;semi_synch&#x60; for a high availability cluster.  |  [optional] |
|**sslConnection** | **Boolean** | Whether to require SSL credentials to establish a connection to the Managed Database.  Use the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command for access information.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The operating status of the Managed Database. |  [optional] [readonly] |
|**type** | **String** | The Linode Instance type used by the Managed Database for its nodes. |  [optional] |
|**updated** | **OffsetDateTime** | When this Managed Database was last updated. |  [optional] [readonly] |
|**updates** | [**DatabaseUpdates**](DatabaseUpdates.md) |  |  [optional] |
|**version** | **String** | The Managed Database engine version. |  [optional] [readonly] |



## Enum: ClusterSizeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_3 | 3 |



## Enum: ReplicationTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| ASYNCH | &quot;asynch&quot; |
| SEMI_SYNCH | &quot;semi_synch&quot; |



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



