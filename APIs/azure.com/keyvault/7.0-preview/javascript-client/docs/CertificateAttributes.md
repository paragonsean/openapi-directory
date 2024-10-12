# KeyVaultClient.CertificateAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recoveryLevel** | **String** | Reflects the deletion recovery level currently in effect for certificates in the current vault. If it contains &#39;Purgeable&#39;, the certificate can be permanently deleted by a privileged user; otherwise, only the system can purge the certificate, at the end of the retention interval. | [optional] [readonly] 
**created** | **Number** | Creation time in UTC. | [optional] [readonly] 
**enabled** | **Boolean** | Determines whether the object is enabled. | [optional] 
**exp** | **Number** | Expiry date in UTC. | [optional] 
**nbf** | **Number** | Not before date in UTC. | [optional] 
**updated** | **Number** | Last updated time in UTC. | [optional] [readonly] 



## Enum: RecoveryLevelEnum


* `Purgeable` (value: `"Purgeable"`)

* `Recoverable+Purgeable` (value: `"Recoverable+Purgeable"`)

* `Recoverable` (value: `"Recoverable"`)

* `Recoverable+ProtectedSubscription` (value: `"Recoverable+ProtectedSubscription"`)




