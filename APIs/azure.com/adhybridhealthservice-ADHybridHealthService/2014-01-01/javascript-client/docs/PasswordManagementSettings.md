# AdHybridHealthService.PasswordManagementSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectTo** | **String** | Connection point of password management. | [optional] 
**connectionTimeout** | **Number** | Connection timeout for password extension. | [optional] 
**enabled** | **Boolean** | Indicates if the password extension is enabled. | [optional] 
**extensionFilePath** | **String** | The file path of the password management extension. | [optional] 
**maximumRetryCount** | **Number** | The maximum number of retries. | [optional] 
**requiresSecureConnection** | **Boolean** | Indicates if a secure connection is required for password management. | [optional] 
**retryIntervalInSeconds** | **Number** | The time between retries. | [optional] 
**supportedPasswordOperations** | **String** | The supported password operations. | [optional] 
**unlockAccount** | **Boolean** | Indicates if accounts should be unlocked when resetting password. | [optional] 
**user** | **String** | User to execute password extension. | [optional] 



## Enum: SupportedPasswordOperationsEnum


* `Undefined` (value: `"Undefined"`)

* `Set` (value: `"Set"`)

* `Change` (value: `"Change"`)




