# FirebaseRealtimeDatabaseApi.DatabaseInstance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseUrl** | **String** | Output only. Output Only. The globally unique hostname of the database. | [optional] [readonly] 
**name** | **String** | The fully qualified resource name of the database instance, in the form: &#x60;projects/{project-number}/locations/{location-id}/instances/{database-id}&#x60;. | [optional] 
**project** | **String** | Output only. The resource name of the project this instance belongs to. For example: &#x60;projects/{project-number}&#x60;. | [optional] [readonly] 
**state** | **String** | Output only. The database&#39;s lifecycle state. Read-only. | [optional] [readonly] 
**type** | **String** | Immutable. The database instance type. On creation only USER_DATABASE is allowed, which is also the default when omitted. | [optional] 



## Enum: StateEnum


* `LIFECYCLE_STATE_UNSPECIFIED` (value: `"LIFECYCLE_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DISABLED` (value: `"DISABLED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: TypeEnum


* `DATABASE_INSTANCE_TYPE_UNSPECIFIED` (value: `"DATABASE_INSTANCE_TYPE_UNSPECIFIED"`)

* `DEFAULT_DATABASE` (value: `"DEFAULT_DATABASE"`)

* `USER_DATABASE` (value: `"USER_DATABASE"`)




