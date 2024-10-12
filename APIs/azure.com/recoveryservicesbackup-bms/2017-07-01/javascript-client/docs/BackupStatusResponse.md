# RecoveryServicesBackupClient.BackupStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerName** | **String** | Specifies the product specific container name. E.g. iaasvmcontainer;iaasvmcontainer;csname;vmname. | [optional] 
**errorCode** | **String** | ErrorCode in case of intent failed | [optional] 
**errorMessage** | **String** | ErrorMessage in case of intent failed. | [optional] 
**fabricName** | **String** | Specifies the fabric name - Azure or AD | [optional] 
**policyName** | **String** | Specifies the policy name which is used for protection | [optional] 
**protectedItemName** | **String** | Specifies the product specific ds name. E.g. vm;iaasvmcontainer;csname;vmname. | [optional] 
**protectionStatus** | **String** | Specifies whether the container is registered or not | [optional] 
**registrationStatus** | **String** | Container registration status | [optional] 
**vaultId** | **String** | Specifies the arm resource id of the vault | [optional] 



## Enum: FabricNameEnum


* `Invalid` (value: `"Invalid"`)

* `Azure` (value: `"Azure"`)





## Enum: ProtectionStatusEnum


* `Invalid` (value: `"Invalid"`)

* `NotProtected` (value: `"NotProtected"`)

* `Protecting` (value: `"Protecting"`)

* `Protected` (value: `"Protected"`)

* `ProtectionFailed` (value: `"ProtectionFailed"`)




