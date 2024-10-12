

# DataLakeStoreAccountProperties

Data Lake Store account properties information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | the account creation time. |  [optional] [readonly] |
|**defaultGroup** | **String** | the default owner group for all new folders and files created in the Data Lake Store account. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**encryptionProvisioningState** | [**EncryptionProvisioningStateEnum**](#EncryptionProvisioningStateEnum) | The current state of encryption provisioning for this Data Lake store account. |  [optional] [readonly] |
|**encryptionState** | [**EncryptionStateEnum**](#EncryptionStateEnum) | The current state of encryption for this Data Lake store account. |  [optional] |
|**endpoint** | **String** | the gateway host. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | the account last modified time. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | the status of the Data Lake Store account while being provisioned. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | the status of the Data Lake Store account after provisioning has completed. |  [optional] [readonly] |



## Enum: EncryptionProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: EncryptionStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;Failed&quot; |
| CREATING | &quot;Creating&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| PATCHING | &quot;Patching&quot; |
| SUSPENDING | &quot;Suspending&quot; |
| RESUMING | &quot;Resuming&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| SUSPENDED | &quot;suspended&quot; |



