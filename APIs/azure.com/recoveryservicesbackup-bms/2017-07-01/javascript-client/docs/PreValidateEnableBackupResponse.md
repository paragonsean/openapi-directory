# RecoveryServicesBackupClient.PreValidateEnableBackupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerName** | **String** | Specifies the product specific container name. E.g. iaasvmcontainer;iaasvmcontainer;rgname;vmname. This is required  for portal | [optional] 
**errorCode** | **String** | Response error code | [optional] 
**errorMessage** | **String** | Response error message | [optional] 
**protectedItemName** | **String** | Specifies the product specific ds name. E.g. vm;iaasvmcontainer;rgname;vmname. This is required for portal | [optional] 
**recommendation** | **String** | Recommended action for user | [optional] 
**status** | **String** | Validation Status | [optional] 



## Enum: StatusEnum


* `Invalid` (value: `"Invalid"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)




