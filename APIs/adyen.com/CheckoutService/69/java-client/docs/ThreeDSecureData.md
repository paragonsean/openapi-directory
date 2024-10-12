

# ThreeDSecureData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationResponse** | [**AuthenticationResponseEnum**](#AuthenticationResponseEnum) | In 3D Secure 1, the authentication response if the shopper was redirected.  In 3D Secure 2, this is the &#x60;transStatus&#x60; from the challenge result. If the transaction was frictionless, omit this parameter. |  [optional] |
|**cavv** | **String** | The cardholder authentication value (base64 encoded, 20 bytes in a decoded form). |  [optional] |
|**cavvAlgorithm** | **String** | The CAVV algorithm used. Include this only for 3D Secure 1. |  [optional] |
|**challengeCancel** | [**ChallengeCancelEnum**](#ChallengeCancelEnum) | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). |  [optional] |
|**directoryResponse** | [**DirectoryResponseEnum**](#DirectoryResponseEnum) | In 3D Secure 1, this is the enrollment response from the 3D directory server.  In 3D Secure 2, this is the &#x60;transStatus&#x60; from the &#x60;ARes&#x60;. |  [optional] |
|**dsTransID** | **String** | Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction. |  [optional] |
|**eci** | **String** | The electronic commerce indicator. |  [optional] |
|**riskScore** | **String** | Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations. |  [optional] |
|**threeDSVersion** | **String** | The version of the 3D Secure protocol. |  [optional] |
|**tokenAuthenticationVerificationValue** | **String** | Network token authentication verification value (TAVV). The network token cryptogram. |  [optional] |
|**transStatusReason** | **String** | Provides information on why the &#x60;transStatus&#x60; field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |  [optional] |
|**xid** | **String** | Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form). |  [optional] |



## Enum: AuthenticationResponseEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |
| U | &quot;U&quot; |
| A | &quot;A&quot; |



## Enum: ChallengeCancelEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |
| _06 | &quot;06&quot; |
| _07 | &quot;07&quot; |



## Enum: DirectoryResponseEnum

| Name | Value |
|---- | -----|
| A | &quot;A&quot; |
| C | &quot;C&quot; |
| D | &quot;D&quot; |
| I | &quot;I&quot; |
| N | &quot;N&quot; |
| R | &quot;R&quot; |
| U | &quot;U&quot; |
| Y | &quot;Y&quot; |



