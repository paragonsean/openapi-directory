# AlloyDbApi.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseRoles** | **[String]** | Optional. List of database roles this user has. The database role strings are subject to the PostgreSQL naming conventions. | [optional] 
**name** | **String** | Output only. Name of the resource in the form of projects/{project}/locations/{location}/cluster/{cluster}/users/{user}. | [optional] [readonly] 
**password** | **String** | Input only. Password for the user. | [optional] 
**userType** | **String** | Optional. Type of this user. | [optional] 



## Enum: UserTypeEnum


* `USER_TYPE_UNSPECIFIED` (value: `"USER_TYPE_UNSPECIFIED"`)

* `ALLOYDB_BUILT_IN` (value: `"ALLOYDB_BUILT_IN"`)

* `ALLOYDB_IAM_USER` (value: `"ALLOYDB_IAM_USER"`)




