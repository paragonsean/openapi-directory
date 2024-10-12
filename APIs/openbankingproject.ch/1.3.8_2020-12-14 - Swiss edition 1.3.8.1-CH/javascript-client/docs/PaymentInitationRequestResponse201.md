# SwissNextGenBankingApiFramework.PaymentInitationRequestResponse201

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksPaymentInitiation**](LinksPaymentInitiation.md) |  | 
**challengeData** | [**ChallengeData**](ChallengeData.md) |  | [optional] 
**chosenScaMethod** | [**AuthenticationObject**](AuthenticationObject.md) |  | [optional] 
**currencyConversionFee** | [**Amount**](Amount.md) |  | [optional] 
**estimatedInterbankSettlementAmount** | [**Amount**](Amount.md) |  | [optional] 
**estimatedTotalAmount** | [**Amount**](Amount.md) |  | [optional] 
**paymentId** | **String** | Resource identification of the generated payment initiation resource. | 
**psuMessage** | **String** | Text to be displayed to the PSU. | [optional] 
**scaMethods** | [**[AuthenticationObject]**](AuthenticationObject.md) | This data element might be contained, if SCA is required and if the PSU has a choice between different authentication methods.  Depending on the risk management of the ASPSP this choice might be offered before or after the PSU has been identified with the first relevant factor, or if an access token is transported.  If this data element is contained, then there is also a hyperlink of type &#39;startAuthorisationWithAuthenticationMethodSelection&#39; contained in the response body.  These methods shall be presented towards the PSU for selection by the TPP.  | [optional] 
**tppMessages** | [**[TppMessage2XX]**](TppMessage2XX.md) |  | [optional] 
**transactionFeeIndicator** | **Boolean** | If equals &#39;true&#39;, the transaction will involve specific transaction cost as shown by the ASPSP in their public price list or as agreed between ASPSP and PSU. If equals &#39;false&#39;, the transaction will not involve additional specific transaction costs to the PSU unless the fee amount is given specifically in the data elements transactionFees and/or currencyConversionFees. If this data element is not used, there is no information about transaction fees unless the fee amount is given explicitly in the data element transactionFees and/or currencyConversionFees.  | [optional] 
**transactionFees** | [**Amount**](Amount.md) |  | [optional] 
**transactionStatus** | [**TransactionStatus**](TransactionStatus.md) |  | 


