# BatchManagement.CertificateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleteCertificateError** | [**DeleteCertificateError**](DeleteCertificateError.md) |  | [optional] 
**previousProvisioningState** | **String** | The previous provisioned state of the resource | [optional] [readonly] 
**previousProvisioningStateTransitionTime** | **Date** |  | [optional] [readonly] 
**provisioningState** | **String** |  | [optional] [readonly] 
**provisioningStateTransitionTime** | **Date** |  | [optional] [readonly] 
**publicData** | **String** | The public key of the certificate. | [optional] [readonly] 
**format** | **String** | The format of the certificate - either Pfx or Cer. If omitted, the default is Pfx. | [optional] 
**thumbprint** | **String** | This must match the thumbprint from the name. | [optional] 
**thumbprintAlgorithm** | **String** | This must match the first portion of the certificate name. Currently required to be &#39;SHA1&#39;. | [optional] 



## Enum: PreviousProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)





## Enum: FormatEnum


* `Pfx` (value: `"Pfx"`)

* `Cer` (value: `"Cer"`)




