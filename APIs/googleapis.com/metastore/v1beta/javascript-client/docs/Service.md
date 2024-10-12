# DataprocMetastoreApi.Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactGcsUri** | **String** | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the metastore service was created. | [optional] [readonly] 
**databaseType** | **String** | Immutable. The database type that the Metastore service stores its data. | [optional] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**endpointUri** | **String** | Output only. The URI of the endpoint used to access the metastore service. | [optional] [readonly] 
**hiveMetastoreConfig** | [**HiveMetastoreConfig**](HiveMetastoreConfig.md) |  | [optional] 
**labels** | **{String: String}** | User-defined labels for the metastore service. | [optional] 
**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**metadataIntegration** | [**MetadataIntegration**](MetadataIntegration.md) |  | [optional] 
**metadataManagementActivity** | [**MetadataManagementActivity**](MetadataManagementActivity.md) |  | [optional] 
**name** | **String** | Immutable. The relative resource name of the metastore service, in the following format:projects/{project_number}/locations/{location_id}/services/{service_id}. | [optional] 
**network** | **String** | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}. | [optional] 
**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  | [optional] 
**port** | **Number** | The TCP port at which the metastore service is reached. Default: 9083. | [optional] 
**releaseChannel** | **String** | Immutable. The release channel of the service. If unspecified, defaults to STABLE. | [optional] 
**scalingConfig** | [**ScalingConfig**](ScalingConfig.md) |  | [optional] 
**scheduledBackup** | [**ScheduledBackup**](ScheduledBackup.md) |  | [optional] 
**state** | **String** | Output only. The current state of the metastore service. | [optional] [readonly] 
**stateMessage** | **String** | Output only. Additional information about the current state of the metastore service, if available. | [optional] [readonly] 
**telemetryConfig** | [**TelemetryConfig**](TelemetryConfig.md) |  | [optional] 
**tier** | **String** | The tier of the service. | [optional] 
**uid** | **String** | Output only. The globally unique resource identifier of the metastore service. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the metastore service was last updated. | [optional] [readonly] 



## Enum: DatabaseTypeEnum


* `DATABASE_TYPE_UNSPECIFIED` (value: `"DATABASE_TYPE_UNSPECIFIED"`)

* `MYSQL` (value: `"MYSQL"`)

* `SPANNER` (value: `"SPANNER"`)





## Enum: ReleaseChannelEnum


* `RELEASE_CHANNEL_UNSPECIFIED` (value: `"RELEASE_CHANNEL_UNSPECIFIED"`)

* `CANARY` (value: `"CANARY"`)

* `STABLE` (value: `"STABLE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUSPENDING` (value: `"SUSPENDING"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `ERROR` (value: `"ERROR"`)





## Enum: TierEnum


* `TIER_UNSPECIFIED` (value: `"TIER_UNSPECIFIED"`)

* `DEVELOPER` (value: `"DEVELOPER"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)




