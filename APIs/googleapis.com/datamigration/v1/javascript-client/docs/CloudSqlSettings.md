# DatabaseMigrationApi.CloudSqlSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activationPolicy** | **String** | The activation policy specifies when the instance is activated; it is applicable only when the instance state is &#39;RUNNABLE&#39;. Valid values: &#39;ALWAYS&#39;: The instance is on, and remains so even in the absence of connection requests. &#x60;NEVER&#x60;: The instance is off; it is not activated, even if a connection request arrives. | [optional] 
**autoStorageIncrease** | **Boolean** | [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB. | [optional] 
**availabilityType** | **String** | Optional. Availability type. Potential values: * &#x60;ZONAL&#x60;: The instance serves data from only one zone. Outages in that zone affect data availability. * &#x60;REGIONAL&#x60;: The instance can serve data from more than one zone in a region (it is highly available). | [optional] 
**cmekKeyName** | **String** | The KMS key name used for the csql instance. | [optional] 
**collation** | **String** | The Cloud SQL default instance level collation. | [optional] 
**dataCacheConfig** | [**DataCacheConfig**](DataCacheConfig.md) |  | [optional] 
**dataDiskSizeGb** | **String** | The storage capacity available to the database, in GB. The minimum (and default) size is 10GB. | [optional] 
**dataDiskType** | **String** | The type of storage: &#x60;PD_SSD&#x60; (default) or &#x60;PD_HDD&#x60;. | [optional] 
**databaseFlags** | **{String: String}** | The database flags passed to the Cloud SQL instance at startup. An object containing a list of \&quot;key\&quot;: value pairs. Example: { \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }. | [optional] 
**databaseVersion** | **String** | The database engine type and version. | [optional] 
**edition** | **String** | Optional. The edition of the given Cloud SQL instance. | [optional] 
**ipConfig** | [**SqlIpConfig**](SqlIpConfig.md) |  | [optional] 
**rootPassword** | **String** | Input only. Initial root password. | [optional] 
**rootPasswordSet** | **Boolean** | Output only. Indicates If this connection profile root password is stored. | [optional] [readonly] 
**secondaryZone** | **String** | Optional. The Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). | [optional] 
**sourceId** | **String** | The Database Migration Service source connection profile ID, in the format: &#x60;projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID&#x60; | [optional] 
**storageAutoResizeLimit** | **String** | The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. | [optional] 
**tier** | **String** | The tier (or machine type) for this instance, for example: &#x60;db-n1-standard-1&#x60; (MySQL instances) or &#x60;db-custom-1-3840&#x60; (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings). | [optional] 
**userLabels** | **{String: String}** | The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;18kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. | [optional] 
**zone** | **String** | The Google Cloud Platform zone where your Cloud SQL database instance is located. | [optional] 



## Enum: ActivationPolicyEnum


* `SQL_ACTIVATION_POLICY_UNSPECIFIED` (value: `"SQL_ACTIVATION_POLICY_UNSPECIFIED"`)

* `ALWAYS` (value: `"ALWAYS"`)

* `NEVER` (value: `"NEVER"`)





## Enum: AvailabilityTypeEnum


* `SQL_AVAILABILITY_TYPE_UNSPECIFIED` (value: `"SQL_AVAILABILITY_TYPE_UNSPECIFIED"`)

* `ZONAL` (value: `"ZONAL"`)

* `REGIONAL` (value: `"REGIONAL"`)





## Enum: DataDiskTypeEnum


* `SQL_DATA_DISK_TYPE_UNSPECIFIED` (value: `"SQL_DATA_DISK_TYPE_UNSPECIFIED"`)

* `PD_SSD` (value: `"PD_SSD"`)

* `PD_HDD` (value: `"PD_HDD"`)





## Enum: DatabaseVersionEnum


* `SQL_DATABASE_VERSION_UNSPECIFIED` (value: `"SQL_DATABASE_VERSION_UNSPECIFIED"`)

* `MYSQL_5_6` (value: `"MYSQL_5_6"`)

* `MYSQL_5_7` (value: `"MYSQL_5_7"`)

* `MYSQL_8_0` (value: `"MYSQL_8_0"`)

* `MYSQL_8_0_18` (value: `"MYSQL_8_0_18"`)

* `MYSQL_8_0_26` (value: `"MYSQL_8_0_26"`)

* `MYSQL_8_0_27` (value: `"MYSQL_8_0_27"`)

* `MYSQL_8_0_28` (value: `"MYSQL_8_0_28"`)

* `MYSQL_8_0_30` (value: `"MYSQL_8_0_30"`)

* `MYSQL_8_0_31` (value: `"MYSQL_8_0_31"`)

* `MYSQL_8_0_32` (value: `"MYSQL_8_0_32"`)

* `MYSQL_8_0_33` (value: `"MYSQL_8_0_33"`)

* `MYSQL_8_0_34` (value: `"MYSQL_8_0_34"`)

* `MYSQL_8_0_35` (value: `"MYSQL_8_0_35"`)

* `POSTGRES_9_6` (value: `"POSTGRES_9_6"`)

* `POSTGRES_11` (value: `"POSTGRES_11"`)

* `POSTGRES_10` (value: `"POSTGRES_10"`)

* `POSTGRES_12` (value: `"POSTGRES_12"`)

* `POSTGRES_13` (value: `"POSTGRES_13"`)

* `POSTGRES_14` (value: `"POSTGRES_14"`)

* `POSTGRES_15` (value: `"POSTGRES_15"`)





## Enum: EditionEnum


* `EDITION_UNSPECIFIED` (value: `"EDITION_UNSPECIFIED"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `ENTERPRISE_PLUS` (value: `"ENTERPRISE_PLUS"`)




