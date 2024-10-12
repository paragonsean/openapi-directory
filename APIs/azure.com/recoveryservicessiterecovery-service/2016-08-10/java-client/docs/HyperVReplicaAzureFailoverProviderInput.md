

# HyperVReplicaAzureFailoverProviderInput

HvrA provider specific input for failover.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primaryKekCertificatePfx** | **String** | Primary kek certificate pfx. |  [optional] |
|**recoveryPointId** | **String** | The recovery point id to be passed to failover to a particular recovery point. In case of latest recovery point, null should be passed. |  [optional] |
|**secondaryKekCertificatePfx** | **String** | Secondary kek certificate pfx. |  [optional] |
|**vaultLocation** | **String** | Location of the vault. |  [optional] |



