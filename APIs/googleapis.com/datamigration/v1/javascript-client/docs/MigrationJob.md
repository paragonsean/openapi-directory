# DatabaseMigrationApi.MigrationJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmekKeyName** | **String** | The CMEK (customer-managed encryption key) fully qualified key name used for the migration job. This field supports all migration jobs types except for: * Mysql to Mysql (use the cmek field in the cloudsql connection profile instead). * PostrgeSQL to PostgreSQL (use the cmek field in the cloudsql connection profile instead). * PostgreSQL to AlloyDB (use the kms_key_name field in the alloydb connection profile instead). Each Cloud CMEK key has the following format: projects/[PROJECT]/locations/[REGION]/keyRings/[RING]/cryptoKeys/[KEY_NAME] | [optional] 
**conversionWorkspace** | [**ConversionWorkspaceInfo**](ConversionWorkspaceInfo.md) |  | [optional] 
**createTime** | **String** | Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. | [optional] [readonly] 
**destination** | **String** | Required. The resource name (URI) of the destination connection profile. | [optional] 
**destinationDatabase** | [**DatabaseType**](DatabaseType.md) |  | [optional] 
**displayName** | **String** | The migration job display name. | [optional] 
**dumpFlags** | [**DumpFlags**](DumpFlags.md) |  | [optional] 
**dumpPath** | **String** | The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]). This field and the \&quot;dump_flags\&quot; field are mutually exclusive. | [optional] 
**duration** | **String** | Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by &#39;s&#39;. Example: \&quot;3.5s\&quot;. | [optional] [readonly] 
**endTime** | **String** | Output only. If the migration job is completed, the time when it was completed. | [optional] [readonly] 
**error** | [**Status**](Status.md) |  | [optional] 
**filter** | **String** | This field can be used to select the entities to migrate as part of the migration job. It uses AIP-160 notation to select a subset of the entities configured on the associated conversion-workspace. This field should not be set on migration-jobs that are not associated with a conversion workspace. | [optional] 
**labels** | **{String: String}** | The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. | [optional] 
**name** | **String** | The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}. | [optional] 
**performanceConfig** | [**PerformanceConfig**](PerformanceConfig.md) |  | [optional] 
**phase** | **String** | Output only. The current migration job phase. | [optional] [readonly] 
**reverseSshConnectivity** | [**ReverseSshConnectivity**](ReverseSshConnectivity.md) |  | [optional] 
**source** | **String** | Required. The resource name (URI) of the source connection profile. | [optional] 
**sourceDatabase** | [**DatabaseType**](DatabaseType.md) |  | [optional] 
**state** | **String** | The current migration job state. | [optional] 
**staticIpConnectivity** | **Object** | The source database will allow incoming connections from the public IP of the destination database. You can retrieve the public IP of the Cloud SQL instance from the Cloud SQL console or using Cloud SQL APIs. No additional configuration is required. | [optional] 
**type** | **String** | Required. The migration job type. | [optional] 
**updateTime** | **String** | Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. | [optional] [readonly] 
**vpcPeeringConnectivity** | [**VpcPeeringConnectivity**](VpcPeeringConnectivity.md) |  | [optional] 



## Enum: PhaseEnum


* `PHASE_UNSPECIFIED` (value: `"PHASE_UNSPECIFIED"`)

* `FULL_DUMP` (value: `"FULL_DUMP"`)

* `CDC` (value: `"CDC"`)

* `PROMOTE_IN_PROGRESS` (value: `"PROMOTE_IN_PROGRESS"`)

* `WAITING_FOR_SOURCE_WRITES_TO_STOP` (value: `"WAITING_FOR_SOURCE_WRITES_TO_STOP"`)

* `PREPARING_THE_DUMP` (value: `"PREPARING_THE_DUMP"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `MAINTENANCE` (value: `"MAINTENANCE"`)

* `DRAFT` (value: `"DRAFT"`)

* `CREATING` (value: `"CREATING"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `RUNNING` (value: `"RUNNING"`)

* `FAILED` (value: `"FAILED"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `DELETING` (value: `"DELETING"`)

* `STOPPING` (value: `"STOPPING"`)

* `STOPPED` (value: `"STOPPED"`)

* `DELETED` (value: `"DELETED"`)

* `UPDATING` (value: `"UPDATING"`)

* `STARTING` (value: `"STARTING"`)

* `RESTARTING` (value: `"RESTARTING"`)

* `RESUMING` (value: `"RESUMING"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `ONE_TIME` (value: `"ONE_TIME"`)

* `CONTINUOUS` (value: `"CONTINUOUS"`)




