# AlloyDbApi.Cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 | [optional] 
**automatedBackupPolicy** | [**AutomatedBackupPolicy**](AutomatedBackupPolicy.md) |  | [optional] 
**backupSource** | [**BackupSource**](BackupSource.md) |  | [optional] 
**clusterType** | **String** | Output only. The type of the cluster. This is an output-only field and it&#39;s populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. &#x60;CreateCluster&#x60; vs. &#x60;CreateSecondaryCluster&#x60; | [optional] [readonly] 
**continuousBackupConfig** | [**ContinuousBackupConfig**](ContinuousBackupConfig.md) |  | [optional] 
**continuousBackupInfo** | [**ContinuousBackupInfo**](ContinuousBackupInfo.md) |  | [optional] 
**createTime** | **String** | Output only. Create time stamp | [optional] [readonly] 
**databaseVersion** | **String** | Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used. | [optional] 
**deleteTime** | **String** | Output only. Delete time stamp | [optional] [readonly] 
**displayName** | **String** | User-settable and human-readable display name for the Cluster. | [optional] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  | [optional] 
**etag** | **String** | For Resource freshness validation (https://google.aip.dev/154) | [optional] 
**initialUser** | [**UserPassword**](UserPassword.md) |  | [optional] 
**labels** | **{String: String}** | Labels as key value pairs | [optional] 
**migrationSource** | [**MigrationSource**](MigrationSource.md) |  | [optional] 
**name** | **String** | Output only. The name of the cluster resource with the format: * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression &#x60;[a-z0-9-]+&#x60;. For more details see https://google.aip.dev/122. The prefix of the cluster resource name is the name of the parent resource: * projects/{project}/locations/{region} | [optional] [readonly] 
**network** | **String** | Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: &#x60;projects/{project}/global/networks/{network_id}&#x60;. This is required to create a cluster. Deprecated, use network_config.network instead. | [optional] 
**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  | [optional] 
**primaryConfig** | [**PrimaryConfig**](PrimaryConfig.md) |  | [optional] 
**pscConfig** | [**PscConfig**](PscConfig.md) |  | [optional] 
**reconciling** | **Boolean** | Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Cluster does not match the user&#39;s intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**secondaryConfig** | [**SecondaryConfig**](SecondaryConfig.md) |  | [optional] 
**sslConfig** | [**SslConfig**](SslConfig.md) |  | [optional] 
**state** | **String** | Output only. The current serving state of the cluster. | [optional] [readonly] 
**uid** | **String** | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. | [optional] [readonly] 
**updateTime** | **String** | Output only. Update time stamp | [optional] [readonly] 



## Enum: ClusterTypeEnum


* `CLUSTER_TYPE_UNSPECIFIED` (value: `"CLUSTER_TYPE_UNSPECIFIED"`)

* `PRIMARY` (value: `"PRIMARY"`)

* `SECONDARY` (value: `"SECONDARY"`)





## Enum: DatabaseVersionEnum


* `DATABASE_VERSION_UNSPECIFIED` (value: `"DATABASE_VERSION_UNSPECIFIED"`)

* `POSTGRES_13` (value: `"POSTGRES_13"`)

* `POSTGRES_14` (value: `"POSTGRES_14"`)

* `POSTGRES_15` (value: `"POSTGRES_15"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `READY` (value: `"READY"`)

* `STOPPED` (value: `"STOPPED"`)

* `EMPTY` (value: `"EMPTY"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED` (value: `"FAILED"`)

* `BOOTSTRAPPING` (value: `"BOOTSTRAPPING"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)

* `PROMOTING` (value: `"PROMOTING"`)




