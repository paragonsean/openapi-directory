# AdyenPaymentApi.ThreeDSecureData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationResponse** | **String** | In 3D Secure 1, the authentication response if the shopper was redirected.  In 3D Secure 2, this is the &#x60;transStatus&#x60; from the challenge result. If the transaction was frictionless, omit this parameter. | [optional] 
**cavv** | **String** | The cardholder authentication value (base64 encoded, 20 bytes in a decoded form). | [optional] 
**cavvAlgorithm** | **String** | The CAVV algorithm used. Include this only for 3D Secure 1. | [optional] 
**challengeCancel** | **String** | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). | [optional] 
**directoryResponse** | **String** | In 3D Secure 1, this is the enrollment response from the 3D directory server.  In 3D Secure 2, this is the &#x60;transStatus&#x60; from the &#x60;ARes&#x60;. | [optional] 
**dsTransID** | **String** | Supported for 3D Secure 2. The unique transaction identifier assigned by the Directory Server (DS) to identify a single transaction. | [optional] 
**eci** | **String** | The electronic commerce indicator. | [optional] 
**riskScore** | **String** | Risk score calculated by Directory Server (DS). Required for Cartes Bancaires integrations. | [optional] 
**threeDSVersion** | **String** | The version of the 3D Secure protocol. | [optional] 
**tokenAuthenticationVerificationValue** | **String** | Network token authentication verification value (TAVV). The network token cryptogram. | [optional] 
**transStatusReason** | **String** | Provides information on why the &#x60;transStatus&#x60; field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). | [optional] 
**xid** | **String** | Supported for 3D Secure 1. The transaction identifier (Base64-encoded, 20 bytes in a decoded form). | [optional] 



## Enum: AuthenticationResponseEnum


* `Y` (value: `"Y"`)

* `N` (value: `"N"`)

* `U` (value: `"U"`)

* `A` (value: `"A"`)





## Enum: ChallengeCancelEnum


* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)

* `06` (value: `"06"`)

* `07` (value: `"07"`)





## Enum: DirectoryResponseEnum


* `A` (value: `"A"`)

* `C` (value: `"C"`)

* `D` (value: `"D"`)

* `I` (value: `"I"`)

* `N` (value: `"N"`)

* `R` (value: `"R"`)

* `U` (value: `"U"`)

* `Y` (value: `"Y"`)




