# AdyenPayoutApi.ResponseAdditionalData3DSecure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardHolderInfo** | **String** | Information provided by the issuer to the cardholder. If this field is present, you need to display this information to the cardholder.  | [optional] 
**cavv** | **String** | The Cardholder Authentication Verification Value (CAVV) for the 3D Secure authentication session, as a Base64-encoded 20-byte array. | [optional] 
**cavvAlgorithm** | **String** | The CAVV algorithm used. | [optional] 
**scaExemptionRequested** | **String** | Shows the [exemption type](https://docs.adyen.com/payments-fundamentals/psd2-sca-compliance-and-implementation-guide#specifypreferenceinyourapirequest) that Adyen requested for the payment.   Possible values: * **lowValue**  * **secureCorporate**  * **trustedBeneficiary**  * **transactionRiskAnalysis**  | [optional] 
**threeds2CardEnrolled** | **Boolean** | Indicates whether a card is enrolled for 3D Secure 2. | [optional] 


