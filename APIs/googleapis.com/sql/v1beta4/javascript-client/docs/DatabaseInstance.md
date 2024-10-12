# CloudSqlAdminApi.DatabaseInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableMaintenanceVersions** | **[String]** | Output only. List all maintenance versions applicable on the instance | [optional] [readonly] 
**backendType** | **String** | The backend type. &#x60;SECOND_GEN&#x60;: Cloud SQL database instance. &#x60;EXTERNAL&#x60;: A database server that is not managed by Google. This property is read-only; use the &#x60;tier&#x60; property in the &#x60;settings&#x60; object to determine the database type. | [optional] 
**connectionName** | **String** | Connection name of the Cloud SQL instance used in connection strings. | [optional] 
**createTime** | **String** | Output only. The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example &#x60;2012-11-15T16:19:00.094Z&#x60;. | [optional] [readonly] 
**currentDiskSize** | **String** | The current disk usage of the instance in bytes. This property has been deprecated. Use the \&quot;cloudsql.googleapis.com/database/disk/bytes_used\&quot; metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details. | [optional] 
**databaseInstalledVersion** | **String** | Output only. Stores the current database version running on the instance including minor version such as &#x60;MYSQL_8_0_18&#x60;. | [optional] [readonly] 
**databaseVersion** | **String** | The database engine type and version. The &#x60;databaseVersion&#x60; field cannot be changed after instance creation. | [optional] 
**diskEncryptionConfiguration** | [**DiskEncryptionConfiguration**](DiskEncryptionConfiguration.md) |  | [optional] 
**diskEncryptionStatus** | [**DiskEncryptionStatus**](DiskEncryptionStatus.md) |  | [optional] 
**dnsName** | **String** | Output only. The dns name of the instance. | [optional] [readonly] 
**etag** | **String** | This field is deprecated and will be removed from a future version of the API. Use the &#x60;settings.settingsVersion&#x60; field instead. | [optional] 
**failoverReplica** | [**DatabaseInstanceFailoverReplica**](DatabaseInstanceFailoverReplica.md) |  | [optional] 
**gceZone** | **String** | The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone. WARNING: Changing this might restart the instance. | [optional] 
**instanceType** | **String** | The instance type. | [optional] 
**ipAddresses** | [**[IpMapping]**](IpMapping.md) | The assigned IP addresses for the instance. | [optional] 
**ipv6Address** | **String** | The IPv6 address assigned to the instance. (Deprecated) This property was applicable only to First Generation instances. | [optional] 
**kind** | **String** | This is always &#x60;sql#instance&#x60;. | [optional] 
**maintenanceVersion** | **String** | The current software version on the instance. | [optional] 
**masterInstanceName** | **String** | The name of the instance which will act as primary in the replication setup. | [optional] 
**maxDiskSize** | **String** | The maximum disk size of the instance in bytes. | [optional] 
**name** | **String** | Name of the Cloud SQL instance. This does not include the project ID. | [optional] 
**onPremisesConfiguration** | [**OnPremisesConfiguration**](OnPremisesConfiguration.md) |  | [optional] 
**outOfDiskReport** | [**SqlOutOfDiskReport**](SqlOutOfDiskReport.md) |  | [optional] 
**primaryDnsName** | **String** | Output only. DEPRECATED: please use write_endpoint instead. | [optional] [readonly] 
**project** | **String** | The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable. | [optional] 
**pscServiceAttachmentLink** | **String** | Output only. The link to service attachment of PSC instance. | [optional] [readonly] 
**region** | **String** | The geographical region of the Cloud SQL instance. It can be one of the [regions](https://cloud.google.com/sql/docs/mysql/locations#location-r) where Cloud SQL operates: For example, &#x60;asia-east1&#x60;, &#x60;europe-west1&#x60;, and &#x60;us-central1&#x60;. The default value is &#x60;us-central1&#x60;. | [optional] 
**replicaConfiguration** | [**ReplicaConfiguration**](ReplicaConfiguration.md) |  | [optional] 
**replicaNames** | **[String]** | The replicas of the instance. | [optional] 
**rootPassword** | **String** | Initial root password. Use only on creation. You must set root passwords before you can connect to PostgreSQL instances. | [optional] 
**satisfiesPzs** | **Boolean** | The status indicating if instance satisfiesPzs. Reserved for future use. | [optional] 
**scheduledMaintenance** | [**SqlScheduledMaintenance**](SqlScheduledMaintenance.md) |  | [optional] 
**secondaryGceZone** | **String** | The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone. | [optional] 
**selfLink** | **String** | The URI of this resource. | [optional] 
**serverCaCert** | [**SslCert**](SslCert.md) |  | [optional] 
**serviceAccountEmailAddress** | **String** | The service account email address assigned to the instance. \\This property is read-only. | [optional] 
**settings** | [**Settings**](Settings.md) |  | [optional] 
**sqlNetworkArchitecture** | **String** | The SQL network architecture for the instance. | [optional] 
**state** | **String** | The current serving state of the Cloud SQL instance. | [optional] 
**suspensionReason** | **[String]** | If the instance state is SUSPENDED, the reason for the suspension. | [optional] 
**writeEndpoint** | **String** | Output only. The dns name of the primary instance in a replication group. | [optional] [readonly] 



## Enum: BackendTypeEnum


* `SQL_BACKEND_TYPE_UNSPECIFIED` (value: `"SQL_BACKEND_TYPE_UNSPECIFIED"`)

* `FIRST_GEN` (value: `"FIRST_GEN"`)

* `SECOND_GEN` (value: `"SECOND_GEN"`)

* `EXTERNAL` (value: `"EXTERNAL"`)





## Enum: DatabaseVersionEnum


* `SQL_DATABASE_VERSION_UNSPECIFIED` (value: `"SQL_DATABASE_VERSION_UNSPECIFIED"`)

* `MYSQL_5_1` (value: `"MYSQL_5_1"`)

* `MYSQL_5_5` (value: `"MYSQL_5_5"`)

* `MYSQL_5_6` (value: `"MYSQL_5_6"`)

* `MYSQL_5_7` (value: `"MYSQL_5_7"`)

* `SQLSERVER_2017_STANDARD` (value: `"SQLSERVER_2017_STANDARD"`)

* `SQLSERVER_2017_ENTERPRISE` (value: `"SQLSERVER_2017_ENTERPRISE"`)

* `SQLSERVER_2017_EXPRESS` (value: `"SQLSERVER_2017_EXPRESS"`)

* `SQLSERVER_2017_WEB` (value: `"SQLSERVER_2017_WEB"`)

* `POSTGRES_9_6` (value: `"POSTGRES_9_6"`)

* `POSTGRES_10` (value: `"POSTGRES_10"`)

* `POSTGRES_11` (value: `"POSTGRES_11"`)

* `POSTGRES_12` (value: `"POSTGRES_12"`)

* `POSTGRES_13` (value: `"POSTGRES_13"`)

* `POSTGRES_14` (value: `"POSTGRES_14"`)

* `POSTGRES_15` (value: `"POSTGRES_15"`)

* `MYSQL_8_0` (value: `"MYSQL_8_0"`)

* `MYSQL_8_0_18` (value: `"MYSQL_8_0_18"`)

* `MYSQL_8_0_26` (value: `"MYSQL_8_0_26"`)

* `MYSQL_8_0_27` (value: `"MYSQL_8_0_27"`)

* `MYSQL_8_0_28` (value: `"MYSQL_8_0_28"`)

* `MYSQL_8_0_29` (value: `"MYSQL_8_0_29"`)

* `MYSQL_8_0_30` (value: `"MYSQL_8_0_30"`)

* `MYSQL_8_0_31` (value: `"MYSQL_8_0_31"`)

* `MYSQL_8_0_32` (value: `"MYSQL_8_0_32"`)

* `MYSQL_8_0_33` (value: `"MYSQL_8_0_33"`)

* `MYSQL_8_0_34` (value: `"MYSQL_8_0_34"`)

* `MYSQL_8_0_35` (value: `"MYSQL_8_0_35"`)

* `MYSQL_8_0_36` (value: `"MYSQL_8_0_36"`)

* `SQLSERVER_2019_STANDARD` (value: `"SQLSERVER_2019_STANDARD"`)

* `SQLSERVER_2019_ENTERPRISE` (value: `"SQLSERVER_2019_ENTERPRISE"`)

* `SQLSERVER_2019_EXPRESS` (value: `"SQLSERVER_2019_EXPRESS"`)

* `SQLSERVER_2019_WEB` (value: `"SQLSERVER_2019_WEB"`)

* `SQLSERVER_2022_STANDARD` (value: `"SQLSERVER_2022_STANDARD"`)

* `SQLSERVER_2022_ENTERPRISE` (value: `"SQLSERVER_2022_ENTERPRISE"`)

* `SQLSERVER_2022_EXPRESS` (value: `"SQLSERVER_2022_EXPRESS"`)

* `SQLSERVER_2022_WEB` (value: `"SQLSERVER_2022_WEB"`)





## Enum: InstanceTypeEnum


* `SQL_INSTANCE_TYPE_UNSPECIFIED` (value: `"SQL_INSTANCE_TYPE_UNSPECIFIED"`)

* `CLOUD_SQL_INSTANCE` (value: `"CLOUD_SQL_INSTANCE"`)

* `ON_PREMISES_INSTANCE` (value: `"ON_PREMISES_INSTANCE"`)

* `READ_REPLICA_INSTANCE` (value: `"READ_REPLICA_INSTANCE"`)





## Enum: SqlNetworkArchitectureEnum


* `SQL_NETWORK_ARCHITECTURE_UNSPECIFIED` (value: `"SQL_NETWORK_ARCHITECTURE_UNSPECIFIED"`)

* `NEW_NETWORK_ARCHITECTURE` (value: `"NEW_NETWORK_ARCHITECTURE"`)

* `OLD_NETWORK_ARCHITECTURE` (value: `"OLD_NETWORK_ARCHITECTURE"`)





## Enum: StateEnum


* `SQL_INSTANCE_STATE_UNSPECIFIED` (value: `"SQL_INSTANCE_STATE_UNSPECIFIED"`)

* `RUNNABLE` (value: `"RUNNABLE"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `PENDING_DELETE` (value: `"PENDING_DELETE"`)

* `PENDING_CREATE` (value: `"PENDING_CREATE"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)

* `FAILED` (value: `"FAILED"`)

* `ONLINE_MAINTENANCE` (value: `"ONLINE_MAINTENANCE"`)





## Enum: [SuspensionReasonEnum]


* `SQL_SUSPENSION_REASON_UNSPECIFIED` (value: `"SQL_SUSPENSION_REASON_UNSPECIFIED"`)

* `BILLING_ISSUE` (value: `"BILLING_ISSUE"`)

* `LEGAL_ISSUE` (value: `"LEGAL_ISSUE"`)

* `OPERATIONAL_ISSUE` (value: `"OPERATIONAL_ISSUE"`)

* `KMS_KEY_ISSUE` (value: `"KMS_KEY_ISSUE"`)




