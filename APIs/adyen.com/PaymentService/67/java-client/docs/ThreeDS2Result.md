

# ThreeDS2Result


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationValue** | **String** | The &#x60;authenticationValue&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |
|**cavvAlgorithm** | **String** | The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations. |  [optional] |
|**challengeCancel** | [**ChallengeCancelEnum**](#ChallengeCancelEnum) | Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. For possible values, refer to [3D Secure API reference](https://docs.adyen.com/online-payments/3d-secure/api-reference#mpidata). |  [optional] |
|**dsTransID** | **String** | The &#x60;dsTransID&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |
|**eci** | **String** | The &#x60;eci&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |
|**exemptionIndicator** | [**ExemptionIndicatorEnum**](#ExemptionIndicatorEnum) | Indicates the exemption type that was applied by the issuer to the authentication, if exemption applied. Allowed values: * &#x60;lowValue&#x60; * &#x60;secureCorporate&#x60; * &#x60;trustedBeneficiary&#x60; * &#x60;transactionRiskAnalysis&#x60;  |  [optional] |
|**messageVersion** | **String** | The &#x60;messageVersion&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |
|**riskScore** | **String** | Risk score calculated by Cartes Bancaires Directory Server (DS). |  [optional] |
|**threeDSServerTransID** | **String** | The &#x60;threeDSServerTransID&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |
|**timestamp** | **String** | The &#x60;timestamp&#x60; value of the 3D Secure 2 authentication. |  [optional] |
|**transStatus** | **String** | The &#x60;transStatus&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |
|**transStatusReason** | **String** | Provides information on why the &#x60;transStatus&#x60; field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). |  [optional] |
|**whiteListStatus** | **String** | The &#x60;whiteListStatus&#x60; value as defined in the 3D Secure 2 specification. |  [optional] |



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



## Enum: ExemptionIndicatorEnum

| Name | Value |
|---- | -----|
| LOW_VALUE | &quot;lowValue&quot; |
| SECURE_CORPORATE | &quot;secureCorporate&quot; |
| TRUSTED_BENEFICIARY | &quot;trustedBeneficiary&quot; |
| TRANSACTION_RISK_ANALYSIS | &quot;transactionRiskAnalysis&quot; |



