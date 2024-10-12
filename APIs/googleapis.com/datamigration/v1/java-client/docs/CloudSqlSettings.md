

# CloudSqlSettings

Settings for creating a Cloud SQL database instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationPolicy** | [**ActivationPolicyEnum**](#ActivationPolicyEnum) | The activation policy specifies when the instance is activated; it is applicable only when the instance state is &#39;RUNNABLE&#39;. Valid values: &#39;ALWAYS&#39;: The instance is on, and remains so even in the absence of connection requests. &#x60;NEVER&#x60;: The instance is off; it is not activated, even if a connection request arrives. |  [optional] |
|**autoStorageIncrease** | **Boolean** | [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB. |  [optional] |
|**availabilityType** | [**AvailabilityTypeEnum**](#AvailabilityTypeEnum) | Optional. Availability type. Potential values: * &#x60;ZONAL&#x60;: The instance serves data from only one zone. Outages in that zone affect data availability. * &#x60;REGIONAL&#x60;: The instance can serve data from more than one zone in a region (it is highly available). |  [optional] |
|**cmekKeyName** | **String** | The KMS key name used for the csql instance. |  [optional] |
|**collation** | **String** | The Cloud SQL default instance level collation. |  [optional] |
|**dataCacheConfig** | [**DataCacheConfig**](DataCacheConfig.md) |  |  [optional] |
|**dataDiskSizeGb** | **String** | The storage capacity available to the database, in GB. The minimum (and default) size is 10GB. |  [optional] |
|**dataDiskType** | [**DataDiskTypeEnum**](#DataDiskTypeEnum) | The type of storage: &#x60;PD_SSD&#x60; (default) or &#x60;PD_HDD&#x60;. |  [optional] |
|**databaseFlags** | **Map&lt;String, String&gt;** | The database flags passed to the Cloud SQL instance at startup. An object containing a list of \&quot;key\&quot;: value pairs. Example: { \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }. |  [optional] |
|**databaseVersion** | [**DatabaseVersionEnum**](#DatabaseVersionEnum) | The database engine type and version. |  [optional] |
|**edition** | [**EditionEnum**](#EditionEnum) | Optional. The edition of the given Cloud SQL instance. |  [optional] |
|**ipConfig** | [**SqlIpConfig**](SqlIpConfig.md) |  |  [optional] |
|**rootPassword** | **String** | Input only. Initial root password. |  [optional] |
|**rootPasswordSet** | **Boolean** | Output only. Indicates If this connection profile root password is stored. |  [optional] [readonly] |
|**secondaryZone** | **String** | Optional. The Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available). |  [optional] |
|**sourceId** | **String** | The Database Migration Service source connection profile ID, in the format: &#x60;projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID&#x60; |  [optional] |
|**storageAutoResizeLimit** | **String** | The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit. |  [optional] |
|**tier** | **String** | The tier (or machine type) for this instance, for example: &#x60;db-n1-standard-1&#x60; (MySQL instances) or &#x60;db-custom-1-3840&#x60; (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings). |  [optional] |
|**userLabels** | **Map&lt;String, String&gt;** | The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;18kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. |  [optional] |
|**zone** | **String** | The Google Cloud Platform zone where your Cloud SQL database instance is located. |  [optional] |



## Enum: ActivationPolicyEnum

| Name | Value |
|---- | -----|
| SQL_ACTIVATION_POLICY_UNSPECIFIED | &quot;SQL_ACTIVATION_POLICY_UNSPECIFIED&quot; |
| ALWAYS | &quot;ALWAYS&quot; |
| NEVER | &quot;NEVER&quot; |



## Enum: AvailabilityTypeEnum

| Name | Value |
|---- | -----|
| SQL_AVAILABILITY_TYPE_UNSPECIFIED | &quot;SQL_AVAILABILITY_TYPE_UNSPECIFIED&quot; |
| ZONAL | &quot;ZONAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |



## Enum: DataDiskTypeEnum

| Name | Value |
|---- | -----|
| SQL_DATA_DISK_TYPE_UNSPECIFIED | &quot;SQL_DATA_DISK_TYPE_UNSPECIFIED&quot; |
| PD_SSD | &quot;PD_SSD&quot; |
| PD_HDD | &quot;PD_HDD&quot; |



## Enum: DatabaseVersionEnum

| Name | Value |
|---- | -----|
| SQL_DATABASE_VERSION_UNSPECIFIED | &quot;SQL_DATABASE_VERSION_UNSPECIFIED&quot; |
| MYSQL_5_6 | &quot;MYSQL_5_6&quot; |
| MYSQL_5_7 | &quot;MYSQL_5_7&quot; |
| MYSQL_8_0 | &quot;MYSQL_8_0&quot; |
| MYSQL_8_0_18 | &quot;MYSQL_8_0_18&quot; |
| MYSQL_8_0_26 | &quot;MYSQL_8_0_26&quot; |
| MYSQL_8_0_27 | &quot;MYSQL_8_0_27&quot; |
| MYSQL_8_0_28 | &quot;MYSQL_8_0_28&quot; |
| MYSQL_8_0_30 | &quot;MYSQL_8_0_30&quot; |
| MYSQL_8_0_31 | &quot;MYSQL_8_0_31&quot; |
| MYSQL_8_0_32 | &quot;MYSQL_8_0_32&quot; |
| MYSQL_8_0_33 | &quot;MYSQL_8_0_33&quot; |
| MYSQL_8_0_34 | &quot;MYSQL_8_0_34&quot; |
| MYSQL_8_0_35 | &quot;MYSQL_8_0_35&quot; |
| POSTGRES_9_6 | &quot;POSTGRES_9_6&quot; |
| POSTGRES_11 | &quot;POSTGRES_11&quot; |
| POSTGRES_10 | &quot;POSTGRES_10&quot; |
| POSTGRES_12 | &quot;POSTGRES_12&quot; |
| POSTGRES_13 | &quot;POSTGRES_13&quot; |
| POSTGRES_14 | &quot;POSTGRES_14&quot; |
| POSTGRES_15 | &quot;POSTGRES_15&quot; |



## Enum: EditionEnum

| Name | Value |
|---- | -----|
| EDITION_UNSPECIFIED | &quot;EDITION_UNSPECIFIED&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |
| ENTERPRISE_PLUS | &quot;ENTERPRISE_PLUS&quot; |



