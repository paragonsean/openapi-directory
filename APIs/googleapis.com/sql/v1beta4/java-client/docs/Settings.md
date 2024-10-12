

# Settings

Database instance settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationPolicy** | [**ActivationPolicyEnum**](#ActivationPolicyEnum) | The activation policy specifies when the instance is activated; it is applicable only when the instance state is RUNNABLE. Valid values: * &#x60;ALWAYS&#x60;: The instance is on, and remains so even in the absence of connection requests. * &#x60;NEVER&#x60;: The instance is off; it is not activated, even if a connection request arrives. |  [optional] |
|**activeDirectoryConfig** | [**SqlActiveDirectoryConfig**](SqlActiveDirectoryConfig.md) |  |  [optional] |
|**advancedMachineFeatures** | [**AdvancedMachineFeatures**](AdvancedMachineFeatures.md) |  |  [optional] |
|**authorizedGaeApplications** | **List&lt;String&gt;** | The App Engine app IDs that can access this instance. (Deprecated) Applied to First Generation instances only. |  [optional] |
|**availabilityType** | [**AvailabilityTypeEnum**](#AvailabilityTypeEnum) | Availability type. Potential values: * &#x60;ZONAL&#x60;: The instance serves data from only one zone. Outages in that zone affect data accessibility. * &#x60;REGIONAL&#x60;: The instance can serve data from more than one zone in a region (it is highly available)./ For more information, see [Overview of the High Availability Configuration](https://cloud.google.com/sql/docs/mysql/high-availability). |  [optional] |
|**backupConfiguration** | [**BackupConfiguration**](BackupConfiguration.md) |  |  [optional] |
|**collation** | **String** | The name of server Instance collation. |  [optional] |
|**connectorEnforcement** | [**ConnectorEnforcementEnum**](#ConnectorEnforcementEnum) | Specifies if connections must use Cloud SQL connectors. Option values include the following: &#x60;NOT_REQUIRED&#x60; (Cloud SQL instances can be connected without Cloud SQL Connectors) and &#x60;REQUIRED&#x60; (Only allow connections that use Cloud SQL Connectors) Note that using REQUIRED disables all existing authorized networks. If this field is not specified when creating a new instance, NOT_REQUIRED is used. If this field is not specified when patching or updating an existing instance, it is left unchanged in the instance. |  [optional] |
|**crashSafeReplicationEnabled** | **Boolean** | Configuration specific to read replica instances. Indicates whether database flags for crash-safe replication are enabled. This property was only applicable to First Generation instances. |  [optional] |
|**dataCacheConfig** | [**DataCacheConfig**](DataCacheConfig.md) |  |  [optional] |
|**dataDiskSizeGb** | **String** | The size of data disk, in GB. The data disk size minimum is 10GB. |  [optional] |
|**dataDiskType** | [**DataDiskTypeEnum**](#DataDiskTypeEnum) | The type of data disk: &#x60;PD_SSD&#x60; (default) or &#x60;PD_HDD&#x60;. Not used for First Generation instances. |  [optional] |
|**databaseFlags** | [**List&lt;DatabaseFlags&gt;**](DatabaseFlags.md) | The database flags passed to the instance at startup. |  [optional] |
|**databaseReplicationEnabled** | **Boolean** | Configuration specific to read replica instances. Indicates whether replication is enabled or not. WARNING: Changing this restarts the instance. |  [optional] |
|**deletionProtectionEnabled** | **Boolean** | Configuration to protect against accidental instance deletion. |  [optional] |
|**denyMaintenancePeriods** | [**List&lt;DenyMaintenancePeriod&gt;**](DenyMaintenancePeriod.md) | Deny maintenance periods |  [optional] |
|**edition** | [**EditionEnum**](#EditionEnum) | Optional. The edition of the instance. |  [optional] |
|**insightsConfig** | [**InsightsConfig**](InsightsConfig.md) |  |  [optional] |
|**ipConfiguration** | [**IpConfiguration**](IpConfiguration.md) |  |  [optional] |
|**kind** | **String** | This is always &#x60;sql#settings&#x60;. |  [optional] |
|**locationPreference** | [**LocationPreference**](LocationPreference.md) |  |  [optional] |
|**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  |  [optional] |
|**passwordValidationPolicy** | [**PasswordValidationPolicy**](PasswordValidationPolicy.md) |  |  [optional] |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | The pricing plan for this instance. This can be either &#x60;PER_USE&#x60; or &#x60;PACKAGE&#x60;. Only &#x60;PER_USE&#x60; is supported for Second Generation instances. |  [optional] |
|**replicationType** | [**ReplicationTypeEnum**](#ReplicationTypeEnum) | The type of replication this instance uses. This can be either &#x60;ASYNCHRONOUS&#x60; or &#x60;SYNCHRONOUS&#x60;. (Deprecated) This property was only applicable to First Generation instances. |  [optional] |
|**settingsVersion** | **String** | The version of instance settings. This is a required field for update method to make sure concurrent updates are handled properly. During update, use the most recent settingsVersion value for this instance and do not try to update this value. |  [optional] |
|**sqlServerAuditConfig** | [**SqlServerAuditConfig**](SqlServerAuditConfig.md) |  |  [optional] |
|**storageAutoResize** | **Boolean** | Configuration to increase storage size automatically. The default value is true. |  [optional] |
|**storageAutoResizeLimit** | **String** | The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. |  [optional] |
|**tier** | **String** | The tier (or machine type) for this instance, for example &#x60;db-custom-1-3840&#x60;. WARNING: Changing this restarts the instance. |  [optional] |
|**timeZone** | **String** | Server timezone, relevant only for Cloud SQL for SQL Server. |  [optional] |
|**userLabels** | **Map&lt;String, String&gt;** | User-provided labels, represented as a dictionary where each label is a single key value pair. |  [optional] |



## Enum: ActivationPolicyEnum

| Name | Value |
|---- | -----|
| SQL_ACTIVATION_POLICY_UNSPECIFIED | &quot;SQL_ACTIVATION_POLICY_UNSPECIFIED&quot; |
| ALWAYS | &quot;ALWAYS&quot; |
| NEVER | &quot;NEVER&quot; |
| ON_DEMAND | &quot;ON_DEMAND&quot; |



## Enum: AvailabilityTypeEnum

| Name | Value |
|---- | -----|
| SQL_AVAILABILITY_TYPE_UNSPECIFIED | &quot;SQL_AVAILABILITY_TYPE_UNSPECIFIED&quot; |
| ZONAL | &quot;ZONAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |



## Enum: ConnectorEnforcementEnum

| Name | Value |
|---- | -----|
| CONNECTOR_ENFORCEMENT_UNSPECIFIED | &quot;CONNECTOR_ENFORCEMENT_UNSPECIFIED&quot; |
| NOT_REQUIRED | &quot;NOT_REQUIRED&quot; |
| REQUIRED | &quot;REQUIRED&quot; |



## Enum: DataDiskTypeEnum

| Name | Value |
|---- | -----|
| SQL_DATA_DISK_TYPE_UNSPECIFIED | &quot;SQL_DATA_DISK_TYPE_UNSPECIFIED&quot; |
| PD_SSD | &quot;PD_SSD&quot; |
| PD_HDD | &quot;PD_HDD&quot; |
| OBSOLETE_LOCAL_SSD | &quot;OBSOLETE_LOCAL_SSD&quot; |



## Enum: EditionEnum

| Name | Value |
|---- | -----|
| EDITION_UNSPECIFIED | &quot;EDITION_UNSPECIFIED&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |
| ENTERPRISE_PLUS | &quot;ENTERPRISE_PLUS&quot; |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| SQL_PRICING_PLAN_UNSPECIFIED | &quot;SQL_PRICING_PLAN_UNSPECIFIED&quot; |
| PACKAGE | &quot;PACKAGE&quot; |
| PER_USE | &quot;PER_USE&quot; |



## Enum: ReplicationTypeEnum

| Name | Value |
|---- | -----|
| SQL_REPLICATION_TYPE_UNSPECIFIED | &quot;SQL_REPLICATION_TYPE_UNSPECIFIED&quot; |
| SYNCHRONOUS | &quot;SYNCHRONOUS&quot; |
| ASYNCHRONOUS | &quot;ASYNCHRONOUS&quot; |



