# DataLakeStoreAccountManagementClient.DataLakeStoreAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **Date** | the account creation time. | [optional] [readonly] 
**defaultGroup** | **String** | the default owner group for all new folders and files created in the Data Lake Store account. | [optional] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**encryptionProvisioningState** | **String** | The current state of encryption provisioning for this Data Lake store account. | [optional] [readonly] 
**encryptionState** | **String** | The current state of encryption for this Data Lake store account. | [optional] 
**endpoint** | **String** | the gateway host. | [optional] 
**lastModifiedTime** | **Date** | the account last modified time. | [optional] [readonly] 
**provisioningState** | **String** | the status of the Data Lake Store account while being provisioned. | [optional] [readonly] 
**state** | **String** | the status of the Data Lake Store account after provisioning has completed. | [optional] [readonly] 



## Enum: EncryptionProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Succeeded` (value: `"Succeeded"`)





## Enum: EncryptionStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: ProvisioningStateEnum


* `Failed` (value: `"Failed"`)

* `Creating` (value: `"Creating"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Patching` (value: `"Patching"`)

* `Suspending` (value: `"Suspending"`)

* `Resuming` (value: `"Resuming"`)

* `Deleting` (value: `"Deleting"`)

* `Deleted` (value: `"Deleted"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `suspended` (value: `"suspended"`)




