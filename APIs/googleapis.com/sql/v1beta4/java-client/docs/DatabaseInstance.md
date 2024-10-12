

# DatabaseInstance

A Cloud SQL instance resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableMaintenanceVersions** | **List&lt;String&gt;** | Output only. List all maintenance versions applicable on the instance |  [optional] [readonly] |
|**backendType** | [**BackendTypeEnum**](#BackendTypeEnum) | The backend type. &#x60;SECOND_GEN&#x60;: Cloud SQL database instance. &#x60;EXTERNAL&#x60;: A database server that is not managed by Google. This property is read-only; use the &#x60;tier&#x60; property in the &#x60;settings&#x60; object to determine the database type. |  [optional] |
|**connectionName** | **String** | Connection name of the Cloud SQL instance used in connection strings. |  [optional] |
|**createTime** | **String** | Output only. The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. |  [optional] [readonly] |
|**currentDiskSize** | **String** | The current disk usage of the instance in bytes. This property has been deprecated. Use the \&quot;cloudsql.googleapis.com/database/disk/bytes_used\&quot; metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details. |  [optional] |
|**databaseInstalledVersion** | **String** | Output only. Stores the current database version running on the instance including minor version such as &#x60;MYSQL_8_0_18&#x60;. |  [optional] [readonly] |
|**databaseVersion** | [**DatabaseVersionEnum**](#DatabaseVersionEnum) | The database engine type and version. The &#x60;databaseVersion&#x60; field cannot be changed after instance creation. |  [optional] |
|**diskEncryptionConfiguration** | [**DiskEncryptionConfiguration**](DiskEncryptionConfiguration.md) |  |  [optional] |
|**diskEncryptionStatus** | [**DiskEncryptionStatus**](DiskEncryptionStatus.md) |  |  [optional] |
|**dnsName** | **String** | Output only. The dns name of the instance. |  [optional] [readonly] |
|**etag** | **String** | This field is deprecated and will be removed from a future version of the API. Use the &#x60;settings.settingsVersion&#x60; field instead. |  [optional] |
|**failoverReplica** | [**DatabaseInstanceFailoverReplica**](DatabaseInstanceFailoverReplica.md) |  |  [optional] |
|**gceZone** | **String** | The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone. WARNING: Changing this might restart the instance. |  [optional] |
|**instanceType** | [**InstanceTypeEnum**](#InstanceTypeEnum) | The instance type. |  [optional] |
|**ipAddresses** | [**List&lt;IpMapping&gt;**](IpMapping.md) | The assigned IP addresses for the instance. |  [optional] |
|**ipv6Address** | **String** | The IPv6 address assigned to the instance. (Deprecated) This property was applicable only to First Generation instances. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#instance&#x60;. |  [optional] |
|**maintenanceVersion** | **String** | The current software version on the instance. |  [optional] |
|**masterInstanceName** | **String** | The name of the instance which will act as primary in the replication setup. |  [optional] |
|**maxDiskSize** | **String** | The maximum disk size of the instance in bytes. |  [optional] |
|**name** | **String** | Name of the Cloud SQL instance. This does not include the project ID. |  [optional] |
|**onPremisesConfiguration** | [**OnPremisesConfiguration**](OnPremisesConfiguration.md) |  |  [optional] |
|**outOfDiskReport** | [**SqlOutOfDiskReport**](SqlOutOfDiskReport.md) |  |  [optional] |
|**primaryDnsName** | **String** | Output only. DEPRECATED: please use write_endpoint instead. |  [optional] [readonly] |
|**project** | **String** | The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable. |  [optional] |
|**pscServiceAttachmentLink** | **String** | Output only. The link to service attachment of PSC instance. |  [optional] [readonly] |
|**region** | **String** | The geographical region of the Cloud SQL instance. It can be one of the [regions](https://cloud.google.com/sql/docs/mysql/locations#location-r) where Cloud SQL operates: For example, &#x60;asia-east1&#x60;, &#x60;europe-west1&#x60;, and &#x60;us-central1&#x60;. The default value is &#x60;us-central1&#x60;. |  [optional] |
|**replicaConfiguration** | [**ReplicaConfiguration**](ReplicaConfiguration.md) |  |  [optional] |
|**replicaNames** | **List&lt;String&gt;** | The replicas of the instance. |  [optional] |
|**rootPassword** | **String** | Initial root password. Use only on creation. You must set root passwords before you can connect to PostgreSQL instances. |  [optional] |
|**satisfiesPzs** | **Boolean** | The status indicating if instance satisfiesPzs. Reserved for future use. |  [optional] |
|**scheduledMaintenance** | [**SqlScheduledMaintenance**](SqlScheduledMaintenance.md) |  |  [optional] |
|**secondaryGceZone** | **String** | The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone. |  [optional] |
|**selfLink** | **String** | The URI of this resource. |  [optional] |
|**serverCaCert** | [**SslCert**](SslCert.md) |  |  [optional] |
|**serviceAccountEmailAddress** | **String** | The service account email address assigned to the instance. \\This property is read-only. |  [optional] |
|**settings** | [**Settings**](Settings.md) |  |  [optional] |
|**sqlNetworkArchitecture** | [**SqlNetworkArchitectureEnum**](#SqlNetworkArchitectureEnum) | The SQL network architecture for the instance. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current serving state of the Cloud SQL instance. |  [optional] |
|**suspensionReason** | [**List&lt;SuspensionReasonEnum&gt;**](#List&lt;SuspensionReasonEnum&gt;) | If the instance state is SUSPENDED, the reason for the suspension. |  [optional] |
|**writeEndpoint** | **String** | Output only. The dns name of the primary instance in a replication group. |  [optional] [readonly] |



## Enum: BackendTypeEnum

| Name | Value |
|---- | -----|
| SQL_BACKEND_TYPE_UNSPECIFIED | &quot;SQL_BACKEND_TYPE_UNSPECIFIED&quot; |
| FIRST_GEN | &quot;FIRST_GEN&quot; |
| SECOND_GEN | &quot;SECOND_GEN&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |



## Enum: DatabaseVersionEnum

| Name | Value |
|---- | -----|
| SQL_DATABASE_VERSION_UNSPECIFIED | &quot;SQL_DATABASE_VERSION_UNSPECIFIED&quot; |
| MYSQL_5_1 | &quot;MYSQL_5_1&quot; |
| MYSQL_5_5 | &quot;MYSQL_5_5&quot; |
| MYSQL_5_6 | &quot;MYSQL_5_6&quot; |
| MYSQL_5_7 | &quot;MYSQL_5_7&quot; |
| SQLSERVER_2017_STANDARD | &quot;SQLSERVER_2017_STANDARD&quot; |
| SQLSERVER_2017_ENTERPRISE | &quot;SQLSERVER_2017_ENTERPRISE&quot; |
| SQLSERVER_2017_EXPRESS | &quot;SQLSERVER_2017_EXPRESS&quot; |
| SQLSERVER_2017_WEB | &quot;SQLSERVER_2017_WEB&quot; |
| POSTGRES_9_6 | &quot;POSTGRES_9_6&quot; |
| POSTGRES_10 | &quot;POSTGRES_10&quot; |
| POSTGRES_11 | &quot;POSTGRES_11&quot; |
| POSTGRES_12 | &quot;POSTGRES_12&quot; |
| POSTGRES_13 | &quot;POSTGRES_13&quot; |
| POSTGRES_14 | &quot;POSTGRES_14&quot; |
| POSTGRES_15 | &quot;POSTGRES_15&quot; |
| MYSQL_8_0 | &quot;MYSQL_8_0&quot; |
| MYSQL_8_0_18 | &quot;MYSQL_8_0_18&quot; |
| MYSQL_8_0_26 | &quot;MYSQL_8_0_26&quot; |
| MYSQL_8_0_27 | &quot;MYSQL_8_0_27&quot; |
| MYSQL_8_0_28 | &quot;MYSQL_8_0_28&quot; |
| MYSQL_8_0_29 | &quot;MYSQL_8_0_29&quot; |
| MYSQL_8_0_30 | &quot;MYSQL_8_0_30&quot; |
| MYSQL_8_0_31 | &quot;MYSQL_8_0_31&quot; |
| MYSQL_8_0_32 | &quot;MYSQL_8_0_32&quot; |
| MYSQL_8_0_33 | &quot;MYSQL_8_0_33&quot; |
| MYSQL_8_0_34 | &quot;MYSQL_8_0_34&quot; |
| MYSQL_8_0_35 | &quot;MYSQL_8_0_35&quot; |
| MYSQL_8_0_36 | &quot;MYSQL_8_0_36&quot; |
| SQLSERVER_2019_STANDARD | &quot;SQLSERVER_2019_STANDARD&quot; |
| SQLSERVER_2019_ENTERPRISE | &quot;SQLSERVER_2019_ENTERPRISE&quot; |
| SQLSERVER_2019_EXPRESS | &quot;SQLSERVER_2019_EXPRESS&quot; |
| SQLSERVER_2019_WEB | &quot;SQLSERVER_2019_WEB&quot; |
| SQLSERVER_2022_STANDARD | &quot;SQLSERVER_2022_STANDARD&quot; |
| SQLSERVER_2022_ENTERPRISE | &quot;SQLSERVER_2022_ENTERPRISE&quot; |
| SQLSERVER_2022_EXPRESS | &quot;SQLSERVER_2022_EXPRESS&quot; |
| SQLSERVER_2022_WEB | &quot;SQLSERVER_2022_WEB&quot; |



## Enum: InstanceTypeEnum

| Name | Value |
|---- | -----|
| SQL_INSTANCE_TYPE_UNSPECIFIED | &quot;SQL_INSTANCE_TYPE_UNSPECIFIED&quot; |
| CLOUD_SQL_INSTANCE | &quot;CLOUD_SQL_INSTANCE&quot; |
| ON_PREMISES_INSTANCE | &quot;ON_PREMISES_INSTANCE&quot; |
| READ_REPLICA_INSTANCE | &quot;READ_REPLICA_INSTANCE&quot; |



## Enum: SqlNetworkArchitectureEnum

| Name | Value |
|---- | -----|
| SQL_NETWORK_ARCHITECTURE_UNSPECIFIED | &quot;SQL_NETWORK_ARCHITECTURE_UNSPECIFIED&quot; |
| NEW_NETWORK_ARCHITECTURE | &quot;NEW_NETWORK_ARCHITECTURE&quot; |
| OLD_NETWORK_ARCHITECTURE | &quot;OLD_NETWORK_ARCHITECTURE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SQL_INSTANCE_STATE_UNSPECIFIED | &quot;SQL_INSTANCE_STATE_UNSPECIFIED&quot; |
| RUNNABLE | &quot;RUNNABLE&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| PENDING_DELETE | &quot;PENDING_DELETE&quot; |
| PENDING_CREATE | &quot;PENDING_CREATE&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| FAILED | &quot;FAILED&quot; |
| ONLINE_MAINTENANCE | &quot;ONLINE_MAINTENANCE&quot; |



## Enum: List&lt;SuspensionReasonEnum&gt;

| Name | Value |
|---- | -----|
| SQL_SUSPENSION_REASON_UNSPECIFIED | &quot;SQL_SUSPENSION_REASON_UNSPECIFIED&quot; |
| BILLING_ISSUE | &quot;BILLING_ISSUE&quot; |
| LEGAL_ISSUE | &quot;LEGAL_ISSUE&quot; |
| OPERATIONAL_ISSUE | &quot;OPERATIONAL_ISSUE&quot; |
| KMS_KEY_ISSUE | &quot;KMS_KEY_ISSUE&quot; |



