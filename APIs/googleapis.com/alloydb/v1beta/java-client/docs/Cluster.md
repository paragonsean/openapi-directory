

# Cluster

A cluster is a collection of regional AlloyDB resources. It can include a primary instance and one or more read pool instances. All cluster resources share a storage layer, which scales as needed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 |  [optional] |
|**automatedBackupPolicy** | [**AutomatedBackupPolicy**](AutomatedBackupPolicy.md) |  |  [optional] |
|**backupSource** | [**BackupSource**](BackupSource.md) |  |  [optional] |
|**clusterType** | [**ClusterTypeEnum**](#ClusterTypeEnum) | Output only. The type of the cluster. This is an output-only field and it&#39;s populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. &#x60;CreateCluster&#x60; vs. &#x60;CreateSecondaryCluster&#x60; |  [optional] [readonly] |
|**continuousBackupConfig** | [**ContinuousBackupConfig**](ContinuousBackupConfig.md) |  |  [optional] |
|**continuousBackupInfo** | [**ContinuousBackupInfo**](ContinuousBackupInfo.md) |  |  [optional] |
|**createTime** | **String** | Output only. Create time stamp |  [optional] [readonly] |
|**databaseVersion** | [**DatabaseVersionEnum**](#DatabaseVersionEnum) | Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used. |  [optional] |
|**deleteTime** | **String** | Output only. Delete time stamp |  [optional] [readonly] |
|**displayName** | **String** | User-settable and human-readable display name for the Cluster. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  |  [optional] |
|**etag** | **String** | For Resource freshness validation (https://google.aip.dev/154) |  [optional] |
|**initialUser** | [**UserPassword**](UserPassword.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs |  [optional] |
|**migrationSource** | [**MigrationSource**](MigrationSource.md) |  |  [optional] |
|**name** | **String** | Output only. The name of the cluster resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression &#x60;[a-z0-9-]+&#x60;. For more details see https://google.aip.dev/122. The prefix of the cluster resource name is the name of the parent resource: * projects/{project}/locations/{region} |  [optional] [readonly] |
|**network** | **String** | Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: &#x60;projects/{project}/global/networks/{network_id}&#x60;. This is required to create a cluster. Deprecated, use network_config.network instead. |  [optional] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**primaryConfig** | [**PrimaryConfig**](PrimaryConfig.md) |  |  [optional] |
|**pscConfig** | [**PscConfig**](PscConfig.md) |  |  [optional] |
|**reconciling** | **Boolean** | Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Cluster does not match the user&#39;s intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**secondaryConfig** | [**SecondaryConfig**](SecondaryConfig.md) |  |  [optional] |
|**sslConfig** | [**SslConfig**](SslConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current serving state of the cluster. |  [optional] [readonly] |
|**uid** | **String** | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Update time stamp |  [optional] [readonly] |



## Enum: ClusterTypeEnum

| Name | Value |
|---- | -----|
| CLUSTER_TYPE_UNSPECIFIED | &quot;CLUSTER_TYPE_UNSPECIFIED&quot; |
| PRIMARY | &quot;PRIMARY&quot; |
| SECONDARY | &quot;SECONDARY&quot; |



## Enum: DatabaseVersionEnum

| Name | Value |
|---- | -----|
| DATABASE_VERSION_UNSPECIFIED | &quot;DATABASE_VERSION_UNSPECIFIED&quot; |
| POSTGRES_13 | &quot;POSTGRES_13&quot; |
| POSTGRES_14 | &quot;POSTGRES_14&quot; |
| POSTGRES_15 | &quot;POSTGRES_15&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| READY | &quot;READY&quot; |
| STOPPED | &quot;STOPPED&quot; |
| EMPTY | &quot;EMPTY&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| FAILED | &quot;FAILED&quot; |
| BOOTSTRAPPING | &quot;BOOTSTRAPPING&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| PROMOTING | &quot;PROMOTING&quot; |



