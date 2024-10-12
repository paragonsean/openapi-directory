

# PasswordManagementSettings

The password management settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectTo** | **String** | Connection point of password management. |  [optional] |
|**connectionTimeout** | **Integer** | Connection timeout for password extension. |  [optional] |
|**enabled** | **Boolean** | Indicates if the password extension is enabled. |  [optional] |
|**extensionFilePath** | **String** | The file path of the password management extension. |  [optional] |
|**maximumRetryCount** | **Integer** | The maximum number of retries. |  [optional] |
|**requiresSecureConnection** | **Boolean** | Indicates if a secure connection is required for password management. |  [optional] |
|**retryIntervalInSeconds** | **Integer** | The time between retries. |  [optional] |
|**supportedPasswordOperations** | [**SupportedPasswordOperationsEnum**](#SupportedPasswordOperationsEnum) | The supported password operations. |  [optional] |
|**unlockAccount** | **Boolean** | Indicates if accounts should be unlocked when resetting password. |  [optional] |
|**user** | **String** | User to execute password extension. |  [optional] |



## Enum: SupportedPasswordOperationsEnum

| Name | Value |
|---- | -----|
| UNDEFINED | &quot;Undefined&quot; |
| SET | &quot;Set&quot; |
| CHANGE | &quot;Change&quot; |



