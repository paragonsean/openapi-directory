

# GoogleFirestoreAdminV1Database

A Cloud Firestore Database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appEngineIntegrationMode** | [**AppEngineIntegrationModeEnum**](#AppEngineIntegrationModeEnum) | The App Engine integration mode to use for this database. |  [optional] |
|**concurrencyMode** | [**ConcurrencyModeEnum**](#ConcurrencyModeEnum) | The concurrency control mode to use for this database. |  [optional] |
|**createTime** | **String** | Output only. The timestamp at which this database was created. Databases created before 2016 do not populate create_time. |  [optional] [readonly] |
|**deleteProtectionState** | [**DeleteProtectionStateEnum**](#DeleteProtectionStateEnum) | State of delete protection for the database. |  [optional] |
|**earliestVersionTime** | **String** | Output only. The earliest timestamp at which older versions of the data can be read from the database. See [version_retention_period] above; this field is populated with &#x60;now - version_retention_period&#x60;. This value is continuously updated, and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery. |  [optional] [readonly] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**keyPrefix** | **String** | Output only. The key_prefix for this database. This key_prefix is used, in combination with the project id (\&quot;~\&quot;) to construct the application id that is returned from the Cloud Datastore APIs in Google App Engine first generation runtimes. This value may be empty in which case the appid to use for URL-encoded keys is the project_id (eg: foo instead of v~foo). |  [optional] [readonly] |
|**locationId** | **String** | The location of the database. Available locations are listed at https://cloud.google.com/firestore/docs/locations. |  [optional] |
|**name** | **String** | The resource name of the Database. Format: &#x60;projects/{project}/databases/{database}&#x60; |  [optional] |
|**pointInTimeRecoveryEnablement** | [**PointInTimeRecoveryEnablementEnum**](#PointInTimeRecoveryEnablementEnum) | Whether to enable the PITR feature on this database. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the database. See https://cloud.google.com/datastore/docs/firestore-or-datastore for information about how to choose. |  [optional] |
|**uid** | **String** | Output only. The system-generated UUID4 for this Database. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp at which this database was most recently updated. Note this only includes updates to the database resource and not data contained by the database. |  [optional] [readonly] |
|**versionRetentionPeriod** | **String** | Output only. The period during which past versions of data are retained in the database. Any read or query can specify a &#x60;read_time&#x60; within this window, and will read the state of the database at that time. If the PITR feature is enabled, the retention period is 7 days. Otherwise, the retention period is 1 hour. |  [optional] [readonly] |



## Enum: AppEngineIntegrationModeEnum

| Name | Value |
|---- | -----|
| APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED | &quot;APP_ENGINE_INTEGRATION_MODE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |



## Enum: ConcurrencyModeEnum

| Name | Value |
|---- | -----|
| CONCURRENCY_MODE_UNSPECIFIED | &quot;CONCURRENCY_MODE_UNSPECIFIED&quot; |
| OPTIMISTIC | &quot;OPTIMISTIC&quot; |
| PESSIMISTIC | &quot;PESSIMISTIC&quot; |
| OPTIMISTIC_WITH_ENTITY_GROUPS | &quot;OPTIMISTIC_WITH_ENTITY_GROUPS&quot; |



## Enum: DeleteProtectionStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;DELETE_PROTECTION_STATE_UNSPECIFIED&quot; |
| DISABLED | &quot;DELETE_PROTECTION_DISABLED&quot; |
| ENABLED | &quot;DELETE_PROTECTION_ENABLED&quot; |



## Enum: PointInTimeRecoveryEnablementEnum

| Name | Value |
|---- | -----|
| ENABLEMENT_UNSPECIFIED | &quot;POINT_IN_TIME_RECOVERY_ENABLEMENT_UNSPECIFIED&quot; |
| ENABLED | &quot;POINT_IN_TIME_RECOVERY_ENABLED&quot; |
| DISABLED | &quot;POINT_IN_TIME_RECOVERY_DISABLED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATABASE_TYPE_UNSPECIFIED | &quot;DATABASE_TYPE_UNSPECIFIED&quot; |
| FIRESTORE_NATIVE | &quot;FIRESTORE_NATIVE&quot; |
| DATASTORE_MODE | &quot;DATASTORE_MODE&quot; |



