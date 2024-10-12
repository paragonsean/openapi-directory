# RecoveryServicesBackupClient.GenericProtectedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fabricName** | **String** | Name of this backup item&#39;s fabric. | [optional] 
**friendlyName** | **String** | Friendly name of the container. | [optional] 
**policyState** | **String** | Indicates consistency of policy object and policy applied to this backup item. | [optional] 
**protectedItemId** | **Number** | Data Plane Service ID of the protected item. | [optional] 
**protectionState** | **String** | Backup state of this backup item. | [optional] 
**sourceAssociations** | **{String: String}** | Loosely coupled (type, value) associations (example - parent of a protected item) | [optional] 



## Enum: ProtectionStateEnum


* `Invalid` (value: `"Invalid"`)

* `IRPending` (value: `"IRPending"`)

* `Protected` (value: `"Protected"`)

* `ProtectionError` (value: `"ProtectionError"`)

* `ProtectionStopped` (value: `"ProtectionStopped"`)

* `ProtectionPaused` (value: `"ProtectionPaused"`)




