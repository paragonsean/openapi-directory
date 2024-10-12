# CloudSqlAdminApi.Settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationPolicy** | **String** | The activation policy specifies when the instance is activated; it is applicable only when the instance state is RUNNABLE. Valid values: * &#x60;ALWAYS&#x60;: The instance is on, and remains so even in the absence of connection requests. * &#x60;NEVER&#x60;: The instance is off; it is not activated, even if a connection request arrives. | [optional] 
**activeDirectoryConfig** | [**SqlActiveDirectoryConfig**](SqlActiveDirectoryConfig.md) |  | [optional] 
**advancedMachineFeatures** | [**AdvancedMachineFeatures**](AdvancedMachineFeatures.md) |  | [optional] 
**authorizedGaeApplications** | **[String]** | The App Engine app IDs that can access this instance. (Deprecated) Applied to First Generation instances only. | [optional] 
**availabilityType** | **String** | Availability type. Potential values: * &#x60;ZONAL&#x60;: The instance serves data from only one zone. Outages in that zone affect data accessibility. * &#x60;REGIONAL&#x60;: The instance can serve data from more than one zone in a region (it is highly available)./ For more information, see [Overview of the High Availability Configuration](https://cloud.google.com/sql/docs/mysql/high-availability). | [optional] 
**backupConfiguration** | [**BackupConfiguration**](BackupConfiguration.md) |  | [optional] 
**collation** | **String** | The name of server Instance collation. | [optional] 
**connectorEnforcement** | **String** | Specifies if connections must use Cloud SQL connectors. Option values include the following: &#x60;NOT_REQUIRED&#x60; (Cloud SQL instances can be connected without Cloud SQL Connectors) and &#x60;REQUIRED&#x60; (Only allow connections that use Cloud SQL Connectors) Note that using REQUIRED disables all existing authorized networks. If this field is not specified when creating a new instance, NOT_REQUIRED is used. If this field is not specified when patching or updating an existing instance, it is left unchanged in the instance. | [optional] 
**crashSafeReplicationEnabled** | **Boolean** | Configuration specific to read replica instances. Indicates whether database flags for crash-safe replication are enabled. This property was only applicable to First Generation instances. | [optional] 
**dataCacheConfig** | [**DataCacheConfig**](DataCacheConfig.md) |  | [optional] 
**dataDiskSizeGb** | **String** | The size of data disk, in GB. The data disk size minimum is 10GB. | [optional] 
**dataDiskType** | **String** | The type of data disk: &#x60;PD_SSD&#x60; (default) or &#x60;PD_HDD&#x60;. Not used for First Generation instances. | [optional] 
**databaseFlags** | [**[DatabaseFlags]**](DatabaseFlags.md) | The database flags passed to the instance at startup. | [optional] 
**databaseReplicationEnabled** | **Boolean** | Configuration specific to read replica instances. Indicates whether replication is enabled or not. WARNING: Changing this restarts the instance. | [optional] 
**deletionProtectionEnabled** | **Boolean** | Configuration to protect against accidental instance deletion. | [optional] 
**denyMaintenancePeriods** | [**[DenyMaintenancePeriod]**](DenyMaintenancePeriod.md) | Deny maintenance periods | [optional] 
**edition** | **String** | Optional. The edition of the instance. | [optional] 
**insightsConfig** | [**InsightsConfig**](InsightsConfig.md) |  | [optional] 
**ipConfiguration** | [**IpConfiguration**](IpConfiguration.md) |  | [optional] 
**kind** | **String** | This is always &#x60;sql#settings&#x60;. | [optional] 
**locationPreference** | [**LocationPreference**](LocationPreference.md) |  | [optional] 
**maintenanceWindow** | [**MaintenanceWindow**](MaintenanceWindow.md) |  | [optional] 
**passwordValidationPolicy** | [**PasswordValidationPolicy**](PasswordValidationPolicy.md) |  | [optional] 
**pricingPlan** | **String** | The pricing plan for this instance. This can be either &#x60;PER_USE&#x60; or &#x60;PACKAGE&#x60;. Only &#x60;PER_USE&#x60; is supported for Second Generation instances. | [optional] 
**replicationType** | **String** | The type of replication this instance uses. This can be either &#x60;ASYNCHRONOUS&#x60; or &#x60;SYNCHRONOUS&#x60;. (Deprecated) This property was only applicable to First Generation instances. | [optional] 
**settingsVersion** | **String** | The version of instance settings. This is a required field for update method to make sure concurrent updates are handled properly. During update, use the most recent settingsVersion value for this instance and do not try to update this value. | [optional] 
**sqlServerAuditConfig** | [**SqlServerAuditConfig**](SqlServerAuditConfig.md) |  | [optional] 
**storageAutoResize** | **Boolean** | Configuration to increase storage size automatically. The default value is true. | [optional] 
**storageAutoResizeLimit** | **String** | The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. | [optional] 
**tier** | **String** | The tier (or machine type) for this instance, for example &#x60;db-custom-1-3840&#x60;. WARNING: Changing this restarts the instance. | [optional] 
**timeZone** | **String** | Server timezone, relevant only for Cloud SQL for SQL Server. | [optional] 
**userLabels** | **{String: String}** | User-provided labels, represented as a dictionary where each label is a single key value pair. | [optional] 



## Enum: ActivationPolicyEnum


* `SQL_ACTIVATION_POLICY_UNSPECIFIED` (value: `"SQL_ACTIVATION_POLICY_UNSPECIFIED"`)

* `ALWAYS` (value: `"ALWAYS"`)

* `NEVER` (value: `"NEVER"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)





## Enum: AvailabilityTypeEnum


* `SQL_AVAILABILITY_TYPE_UNSPECIFIED` (value: `"SQL_AVAILABILITY_TYPE_UNSPECIFIED"`)

* `ZONAL` (value: `"ZONAL"`)

* `REGIONAL` (value: `"REGIONAL"`)





## Enum: ConnectorEnforcementEnum


* `CONNECTOR_ENFORCEMENT_UNSPECIFIED` (value: `"CONNECTOR_ENFORCEMENT_UNSPECIFIED"`)

* `NOT_REQUIRED` (value: `"NOT_REQUIRED"`)

* `REQUIRED` (value: `"REQUIRED"`)





## Enum: DataDiskTypeEnum


* `SQL_DATA_DISK_TYPE_UNSPECIFIED` (value: `"SQL_DATA_DISK_TYPE_UNSPECIFIED"`)

* `PD_SSD` (value: `"PD_SSD"`)

* `PD_HDD` (value: `"PD_HDD"`)

* `OBSOLETE_LOCAL_SSD` (value: `"OBSOLETE_LOCAL_SSD"`)





## Enum: EditionEnum


* `EDITION_UNSPECIFIED` (value: `"EDITION_UNSPECIFIED"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `ENTERPRISE_PLUS` (value: `"ENTERPRISE_PLUS"`)





## Enum: PricingPlanEnum


* `SQL_PRICING_PLAN_UNSPECIFIED` (value: `"SQL_PRICING_PLAN_UNSPECIFIED"`)

* `PACKAGE` (value: `"PACKAGE"`)

* `PER_USE` (value: `"PER_USE"`)





## Enum: ReplicationTypeEnum


* `SQL_REPLICATION_TYPE_UNSPECIFIED` (value: `"SQL_REPLICATION_TYPE_UNSPECIFIED"`)

* `SYNCHRONOUS` (value: `"SYNCHRONOUS"`)

* `ASYNCHRONOUS` (value: `"ASYNCHRONOUS"`)




