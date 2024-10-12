

# MigrationJob

Represents a Database Migration Service migration job object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. |  [optional] [readonly] |
|**destination** | **String** | Required. The resource name (URI) of the destination connection profile. |  [optional] |
|**destinationDatabase** | [**DatabaseType**](DatabaseType.md) |  |  [optional] |
|**displayName** | **String** | The migration job display name. |  [optional] |
|**dumpPath** | **String** | The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]). |  [optional] |
|**duration** | **String** | Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by &#39;s&#39;. Example: \&quot;3.5s\&quot;. |  [optional] [readonly] |
|**endTime** | **String** | Output only. If the migration job is completed, the time when it was completed. |  [optional] [readonly] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of \&quot;key\&quot;: \&quot;value\&quot; pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. |  [optional] |
|**name** | **String** | The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}. |  [optional] |
|**phase** | [**PhaseEnum**](#PhaseEnum) | Output only. The current migration job phase. |  [optional] [readonly] |
|**reverseSshConnectivity** | [**ReverseSshConnectivity**](ReverseSshConnectivity.md) |  |  [optional] |
|**source** | **String** | Required. The resource name (URI) of the source connection profile. |  [optional] |
|**sourceDatabase** | [**DatabaseType**](DatabaseType.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current migration job state. |  [optional] |
|**staticIpConnectivity** | **Object** | The source database will allow incoming connections from the destination database&#39;s public IP. You can retrieve the Cloud SQL instance&#39;s public IP from the Cloud SQL console or using Cloud SQL APIs. No additional configuration is required. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The migration job type. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC \&quot;Zulu\&quot; format, accurate to nanoseconds. Example: \&quot;2014-10-02T15:01:23.045123456Z\&quot;. |  [optional] [readonly] |
|**vpcPeeringConnectivity** | [**VpcPeeringConnectivity**](VpcPeeringConnectivity.md) |  |  [optional] |



## Enum: PhaseEnum

| Name | Value |
|---- | -----|
| PHASE_UNSPECIFIED | &quot;PHASE_UNSPECIFIED&quot; |
| FULL_DUMP | &quot;FULL_DUMP&quot; |
| CDC | &quot;CDC&quot; |
| PROMOTE_IN_PROGRESS | &quot;PROMOTE_IN_PROGRESS&quot; |
| WAITING_FOR_SOURCE_WRITES_TO_STOP | &quot;WAITING_FOR_SOURCE_WRITES_TO_STOP&quot; |
| PREPARING_THE_DUMP | &quot;PREPARING_THE_DUMP&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| MAINTENANCE | &quot;MAINTENANCE&quot; |
| DRAFT | &quot;DRAFT&quot; |
| CREATING | &quot;CREATING&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FAILED | &quot;FAILED&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| DELETING | &quot;DELETING&quot; |
| STOPPING | &quot;STOPPING&quot; |
| STOPPED | &quot;STOPPED&quot; |
| DELETED | &quot;DELETED&quot; |
| UPDATING | &quot;UPDATING&quot; |
| STARTING | &quot;STARTING&quot; |
| RESTARTING | &quot;RESTARTING&quot; |
| RESUMING | &quot;RESUMING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| ONE_TIME | &quot;ONE_TIME&quot; |
| CONTINUOUS | &quot;CONTINUOUS&quot; |



