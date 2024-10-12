

# RecoveryPlanHyperVReplicaAzureFailoverInput

Recovery plan HVR Azure failover input.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primaryKekCertificatePfx** | **String** | The primary KEK certificate PFX. |  [optional] |
|**recoveryPointType** | [**RecoveryPointTypeEnum**](#RecoveryPointTypeEnum) | The recovery point type. |  [optional] |
|**secondaryKekCertificatePfx** | **String** | The secondary KEK certificate PFX. |  [optional] |
|**vaultLocation** | **String** | The vault location. |  |



## Enum: RecoveryPointTypeEnum

| Name | Value |
|---- | -----|
| LATEST | &quot;Latest&quot; |
| LATEST_APPLICATION_CONSISTENT | &quot;LatestApplicationConsistent&quot; |
| LATEST_PROCESSED | &quot;LatestProcessed&quot; |



