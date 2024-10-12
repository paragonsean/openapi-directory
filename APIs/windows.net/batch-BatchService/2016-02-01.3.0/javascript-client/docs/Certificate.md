# BatchService.Certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleteCertificateError** | [**DeleteCertificateError**](DeleteCertificateError.md) |  | [optional] 
**previousState** | **String** | The previous state of the certificate. This property is not set if the certificate is in its initial Active state. | [optional] 
**previousStateTransitionTime** | **Date** | The time at which the certificate entered its previous state. This property is not set if the certificate is in its initial Active state. | [optional] 
**publicData** | **String** | The public part of the certificate as a base-64 encoded .cer file. | [optional] 
**state** | **String** | The current state of the certificate. | [optional] 
**stateTransitionTime** | **Date** | The time at which the certificate entered its current state. | [optional] 
**thumbprint** | **String** | The X.509 thumbprint of the certificate. This is a sequence of up to 40 hex digits (it may include spaces but these are removed). | [optional] 
**thumbprintAlgorithm** | **String** | The algorithm used to derive the thumbprint. This must be sha1. | [optional] 
**url** | **String** | The URL of the certificate. | [optional] 



## Enum: PreviousStateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `deletefailed` (value: `"deletefailed"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `deletefailed` (value: `"deletefailed"`)




