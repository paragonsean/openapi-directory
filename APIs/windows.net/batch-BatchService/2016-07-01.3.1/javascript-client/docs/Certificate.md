# BatchService.Certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleteCertificateError** | [**DeleteCertificateError**](DeleteCertificateError.md) |  | [optional] 
**previousState** | **String** | This property is not set if the certificate is in its initial Active state. | [optional] 
**previousStateTransitionTime** | **Date** | This property is not set if the certificate is in its initial Active state. | [optional] 
**publicData** | **String** |  | [optional] 
**state** | **String** |  | [optional] 
**stateTransitionTime** | **Date** |  | [optional] 
**thumbprint** | **String** |  | [optional] 
**thumbprintAlgorithm** | **String** |  | [optional] 
**url** | **String** |  | [optional] 



## Enum: PreviousStateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `deletefailed` (value: `"deletefailed"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `deleting` (value: `"deleting"`)

* `deletefailed` (value: `"deletefailed"`)




