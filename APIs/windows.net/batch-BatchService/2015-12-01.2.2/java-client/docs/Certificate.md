

# Certificate

A certificate that can be installed on compute nodes and can be used to authenticate operations on the machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deleteCertificateError** | [**DeleteCertificateError**](DeleteCertificateError.md) |  |  [optional] |
|**previousState** | [**PreviousStateEnum**](#PreviousStateEnum) | Gets or sets the previous state of the certificate. This property is not set if the certificate is in its initial Active state. |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the certificate entered its previous state.  This property is not set if the certificate is in its initial Active state. |  [optional] |
|**publicData** | **String** | Gets or sets the public part of the certificate as a base-64 encoded .cer file. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the current state of the certificate. |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** | Gets or sets the time at which the certificate entered its current state. |  [optional] |
|**thumbprint** | **String** | Get or sets the X.509 thumbprint of the certificate. This is a sequence of up to 40 hex digits (it may include spaces but these are removed). |  [optional] |
|**thumbprintAlgorithm** | **String** | Gets or sets the algorithm used to derive the thumbprint. This must be sha1. |  [optional] |
|**url** | **String** | Gets or sets the URL of the certificate. |  [optional] |



## Enum: PreviousStateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DELETING | &quot;deleting&quot; |
| DELETEFAILED | &quot;deletefailed&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DELETING | &quot;deleting&quot; |
| DELETEFAILED | &quot;deletefailed&quot; |



