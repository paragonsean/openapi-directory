

# User

Message describing User object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseRoles** | **List&lt;String&gt;** | Optional. List of database roles this user has. The database role strings are subject to the PostgreSQL naming conventions. |  [optional] |
|**name** | **String** | Output only. Name of the resource in the form of projects/{project}/locations/{location}/cluster/{cluster}/users/{user}. |  [optional] [readonly] |
|**password** | **String** | Input only. Password for the user. |  [optional] |
|**userType** | [**UserTypeEnum**](#UserTypeEnum) | Optional. Type of this user. |  [optional] |



## Enum: UserTypeEnum

| Name | Value |
|---- | -----|
| USER_TYPE_UNSPECIFIED | &quot;USER_TYPE_UNSPECIFIED&quot; |
| ALLOYDB_BUILT_IN | &quot;ALLOYDB_BUILT_IN&quot; |
| ALLOYDB_IAM_USER | &quot;ALLOYDB_IAM_USER&quot; |



