

# Service

A managed metastore service that serves metadata queries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactGcsUri** | **String** | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The time when the metastore service was created. |  [optional] [readonly] |
|**databaseType** | [**DatabaseTypeEnum**](#DatabaseTypeEnum) | Immutable. The database type that the Metastore service stores its data. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**endpointUri** | **String** | Output only. The URI of the endpoint used to access the metastore service. |  [optional] [readonly] |
|**hiveMetastoreConfig** | [**HiveMetastoreConfig**](HiveMetastoreConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels for the metastore service. |  [optional] |
|**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  |  [optional] |
|**metadataIntegration** | [**MetadataIntegration**](MetadataIntegration.md) |  |  [optional] |
|**metadataManagementActivity** | [**MetadataManagementActivity**](MetadataManagementActivity.md) |  |  [optional] |
|**name** | **String** | Immutable. The relative resource name of the metastore service, in the following format:projects/{project_number}/locations/{location_id}/services/{service_id}. |  [optional] |
|**network** | **String** | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}. |  [optional] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**port** | **Integer** | The TCP port at which the metastore service is reached. Default: 9083. |  [optional] |
|**releaseChannel** | [**ReleaseChannelEnum**](#ReleaseChannelEnum) | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |  [optional] |
|**scalingConfig** | [**ScalingConfig**](ScalingConfig.md) |  |  [optional] |
|**scheduledBackup** | [**ScheduledBackup**](ScheduledBackup.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the metastore service. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. Additional information about the current state of the metastore service, if available. |  [optional] [readonly] |
|**telemetryConfig** | [**TelemetryConfig**](TelemetryConfig.md) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The tier of the service. |  [optional] |
|**uid** | **String** | Output only. The globally unique resource identifier of the metastore service. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the metastore service was last updated. |  [optional] [readonly] |



## Enum: DatabaseTypeEnum

| Name | Value |
|---- | -----|
| DATABASE_TYPE_UNSPECIFIED | &quot;DATABASE_TYPE_UNSPECIFIED&quot; |
| MYSQL | &quot;MYSQL&quot; |
| SPANNER | &quot;SPANNER&quot; |



## Enum: ReleaseChannelEnum

| Name | Value |
|---- | -----|
| RELEASE_CHANNEL_UNSPECIFIED | &quot;RELEASE_CHANNEL_UNSPECIFIED&quot; |
| CANARY | &quot;CANARY&quot; |
| STABLE | &quot;STABLE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUSPENDING | &quot;SUSPENDING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ERROR | &quot;ERROR&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| TIER_UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| DEVELOPER | &quot;DEVELOPER&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |



