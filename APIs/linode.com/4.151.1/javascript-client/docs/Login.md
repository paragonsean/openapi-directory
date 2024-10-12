# LinodeApi.Login

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **Date** | When the login was initiated.  | [optional] [readonly] 
**id** | **Number** | The unique ID of this login object.  | [optional] [readonly] 
**ip** | **String** | The remote IP address that requested the login.  | [optional] [readonly] 
**restricted** | **Boolean** | True if the User that attempted the login was a restricted User, false otherwise.  | [optional] [readonly] 
**status** | **String** | Whether the login attempt succeeded or failed.  | [optional] [readonly] 
**username** | **String** | The username of the User that attempted the login.  | [optional] [readonly] 



## Enum: StatusEnum


* `successful` (value: `"successful"`)

* `failed` (value: `"failed"`)




