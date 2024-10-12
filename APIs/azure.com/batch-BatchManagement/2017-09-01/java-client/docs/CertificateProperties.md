

# CertificateProperties

Certificate properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deleteCertificateError** | [**DeleteCertificateError**](DeleteCertificateError.md) |  |  [optional] |
|**previousProvisioningState** | [**PreviousProvisioningStateEnum**](#PreviousProvisioningStateEnum) | The previous provisioned state of the resource |  [optional] [readonly] |
|**previousProvisioningStateTransitionTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Values are:   Succeeded - The certificate is available for use in pools.  Deleting - The user has requested that the certificate be deleted, but the delete operation has not yet completed. You may not reference the certificate when creating or updating pools.  Failed - The user requested that the certificate be deleted, but there are pools that still have references to the certificate, or it is still installed on one or more compute nodes. (The latter can occur if the certificate has been removed from the pool, but the node has not yet restarted. Nodes refresh their certificates only when they restart.) You may use the cancel certificate delete operation to cancel the delete, or the delete certificate operation to retry the delete. |  [optional] [readonly] |
|**provisioningStateTransitionTime** | **OffsetDateTime** |  |  [optional] [readonly] |
|**publicData** | **String** | The public key of the certificate. |  [optional] [readonly] |
|**format** | [**FormatEnum**](#FormatEnum) | The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx. |  [optional] |
|**thumbprint** | **String** | This must match the thumbprint from the name. |  [optional] |
|**thumbprintAlgorithm** | **String** | This must match the first portion of the certificate name. Currently required to be &#39;SHA1&#39;. |  [optional] |



## Enum: PreviousProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| PFX | &quot;Pfx&quot; |
| CER | &quot;Cer&quot; |



