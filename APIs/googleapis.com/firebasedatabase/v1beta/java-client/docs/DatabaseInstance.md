

# DatabaseInstance

Representation of a Realtime Database instance. Details on interacting with contents of a DatabaseInstance can be found at: https://firebase.google.com/docs/database/rest/start.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseUrl** | **String** | Output only. Output Only. The globally unique hostname of the database. |  [optional] [readonly] |
|**name** | **String** | The fully qualified resource name of the database instance, in the form: &#x60;projects/{project-number}/locations/{location-id}/instances/{database-id}&#x60;. |  [optional] |
|**project** | **String** | Output only. The resource name of the project this instance belongs to. For example: &#x60;projects/{project-number}&#x60;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The database&#39;s lifecycle state. Read-only. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. The database instance type. On creation only USER_DATABASE is allowed, which is also the default when omitted. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DISABLED | &quot;DISABLED&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATABASE_INSTANCE_TYPE_UNSPECIFIED | &quot;DATABASE_INSTANCE_TYPE_UNSPECIFIED&quot; |
| DEFAULT_DATABASE | &quot;DEFAULT_DATABASE&quot; |
| USER_DATABASE | &quot;USER_DATABASE&quot; |



