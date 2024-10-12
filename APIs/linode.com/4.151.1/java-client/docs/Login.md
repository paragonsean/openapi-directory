

# Login

An object representing a previous successful login for a User. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datetime** | **OffsetDateTime** | When the login was initiated.  |  [optional] [readonly] |
|**id** | **Integer** | The unique ID of this login object.  |  [optional] [readonly] |
|**ip** | **String** | The remote IP address that requested the login.  |  [optional] [readonly] |
|**restricted** | **Boolean** | True if the User that attempted the login was a restricted User, false otherwise.  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the login attempt succeeded or failed.  |  [optional] [readonly] |
|**username** | **String** | The username of the User that attempted the login.  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESSFUL | &quot;successful&quot; |
| FAILED | &quot;failed&quot; |



