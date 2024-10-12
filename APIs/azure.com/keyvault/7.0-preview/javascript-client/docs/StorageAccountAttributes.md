# KeyVaultClient.StorageAccountAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Number** | Creation time in UTC. | [optional] [readonly] 
**enabled** | **Boolean** | the enabled state of the object. | [optional] 
**recoveryLevel** | **String** | Reflects the deletion recovery level currently in effect for storage accounts in the current vault. If it contains &#39;Purgeable&#39; the storage account can be permanently deleted by a privileged user; otherwise, only the system can purge the storage account, at the end of the retention interval. | [optional] [readonly] 
**updated** | **Number** | Last updated time in UTC. | [optional] [readonly] 



## Enum: RecoveryLevelEnum


* `Purgeable` (value: `"Purgeable"`)

* `Recoverable+Purgeable` (value: `"Recoverable+Purgeable"`)

* `Recoverable` (value: `"Recoverable"`)

* `Recoverable+ProtectedSubscription` (value: `"Recoverable+ProtectedSubscription"`)




