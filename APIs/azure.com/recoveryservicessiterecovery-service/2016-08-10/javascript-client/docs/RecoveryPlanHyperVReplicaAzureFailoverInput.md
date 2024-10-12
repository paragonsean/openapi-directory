# SiteRecoveryManagementClient.RecoveryPlanHyperVReplicaAzureFailoverInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primaryKekCertificatePfx** | **String** | The primary KEK certificate PFX. | [optional] 
**recoveryPointType** | **String** | The recovery point type. | [optional] 
**secondaryKekCertificatePfx** | **String** | The secondary KEK certificate PFX. | [optional] 
**vaultLocation** | **String** | The vault location. | 



## Enum: RecoveryPointTypeEnum


* `Latest` (value: `"Latest"`)

* `LatestApplicationConsistent` (value: `"LatestApplicationConsistent"`)

* `LatestProcessed` (value: `"LatestProcessed"`)




