# AdyenPaymentApi.ThreeDS2Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationValue** | **String** | The &#x60;authenticationValue&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**cavvAlgorithm** | **String** | The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations. | [optional] 
**challengeCancel** | **String** | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). | [optional] 
**dsTransID** | **String** | The &#x60;dsTransID&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**eci** | **String** | The &#x60;eci&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**exemptionIndicator** | **String** | Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied. Allowed values: * &#x60;lowValue&#x60; * &#x60;secureCorporate&#x60; * &#x60;trustedBeneficiary&#x60; * &#x60;transactionRiskAnalysis&#x60;  | [optional] 
**messageVersion** | **String** | The &#x60;messageVersion&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**riskScore** | **String** | Risk score calculated by Cartes Bancaires Directory Server (DS). | [optional] 
**threeDSRequestorChallengeInd** | **String** | Indicates whether a challenge is requested for this transaction. Possible values: * **01** — No preference * **02** — No challenge requested * **03** — Challenge requested (3DS Requestor preference) * **04** — Challenge requested (Mandate) * **05** — No challenge (transactional risk analysis is already performed) * **06** — Data Only | [optional] 
**threeDSServerTransID** | **String** | The &#x60;threeDSServerTransID&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**timestamp** | **String** | The &#x60;timestamp&#x60; value of the 3D Secure 2 authentication. | [optional] 
**transStatus** | **String** | The &#x60;transStatus&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**transStatusReason** | **String** | Provides information on why the &#x60;transStatus&#x60; field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). | [optional] 
**whiteListStatus** | **String** | The &#x60;whiteListStatus&#x60; value as defined in the 3D Secure 2 specification. | [optional] 



## Enum: ChallengeCancelEnum


* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)

* `06` (value: `"06"`)

* `07` (value: `"07"`)





## Enum: ExemptionIndicatorEnum


* `lowValue` (value: `"lowValue"`)

* `secureCorporate` (value: `"secureCorporate"`)

* `trustedBeneficiary` (value: `"trustedBeneficiary"`)

* `transactionRiskAnalysis` (value: `"transactionRiskAnalysis"`)





## Enum: ThreeDSRequestorChallengeIndEnum


* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)

* `06` (value: `"06"`)




