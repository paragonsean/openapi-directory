# AlloyDbApi.Backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 | [optional] 
**clusterName** | **String** | Required. The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}). | [optional] 
**clusterUid** | **String** | Output only. The system-generated UID of the cluster which was used to create this resource. | [optional] [readonly] 
**createTime** | **String** | Output only. Create time stamp | [optional] [readonly] 
**databaseVersion** | **String** | Output only. The database engine major version of the cluster this backup was created from. Any restored cluster created from this backup will have the same database version. | [optional] [readonly] 
**deleteTime** | **String** | Output only. Delete time stamp | [optional] [readonly] 
**description** | **String** | User-provided description of the backup. | [optional] 
**displayName** | **String** | User-settable and human-readable display name for the Backup. | [optional] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**encryptionInfo** | [**EncryptionInfo**](EncryptionInfo.md) |  | [optional] 
**etag** | **String** | For Resource freshness validation (https://google.aip.dev/154) | [optional] 
**expiryQuantity** | [**QuantityBasedExpiry**](QuantityBasedExpiry.md) |  | [optional] 
**expiryTime** | **String** | Output only. The time at which after the backup is eligible to be garbage collected. It is the duration specified by the backup&#39;s retention policy, added to the backup&#39;s create_time. | [optional] [readonly] 
**labels** | **{String: String}** | Labels as key value pairs | [optional] 
**name** | **String** | Output only. The name of the backup resource with the format: * projects/{project}/locations/{region}/backups/{backup_id} where the cluster and backup ID segments should satisfy the regex expression &#x60;[a-z]([a-z0-9-]{0,61}[a-z0-9])?&#x60;, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the backup resource name is the name of the parent resource: * projects/{project}/locations/{region} | [optional] [readonly] 
**reconciling** | **Boolean** | Output only. Reconciling (https://google.aip.dev/128#reconciliation), if true, indicates that the service is actively updating the resource. This can happen due to user-triggered updates or system actions like failover or maintenance. | [optional] [readonly] 
**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**sizeBytes** | **String** | Output only. The size of the backup in bytes. | [optional] [readonly] 
**state** | **String** | Output only. The current state of the backup. | [optional] [readonly] 
**type** | **String** | The backup type, which suggests the trigger for the backup. | [optional] 
**uid** | **String** | Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. | [optional] [readonly] 
**updateTime** | **String** | Output only. Update time stamp | [optional] [readonly] 



## Enum: DatabaseVersionEnum


* `DATABASE_VERSION_UNSPECIFIED` (value: `"DATABASE_VERSION_UNSPECIFIED"`)

* `POSTGRES_13` (value: `"POSTGRES_13"`)

* `POSTGRES_14` (value: `"POSTGRES_14"`)

* `POSTGRES_15` (value: `"POSTGRES_15"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `READY` (value: `"READY"`)

* `CREATING` (value: `"CREATING"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)

* `AUTOMATED` (value: `"AUTOMATED"`)

* `CONTINUOUS` (value: `"CONTINUOUS"`)




