# SwissNextGenBankingApiFramework.PaymentInitiationCancelResponse202

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksPaymentInitiationCancel**](LinksPaymentInitiationCancel.md) |  | [optional] 
**challengeData** | [**ChallengeData**](ChallengeData.md) |  | [optional] 
**chosenScaMethod** | [**AuthenticationObject**](AuthenticationObject.md) |  | [optional] 
**scaMethods** | [**[AuthenticationObject]**](AuthenticationObject.md) | This data element might be contained, if SCA is required and if the PSU has a choice between different authentication methods.  Depending on the risk management of the ASPSP this choice might be offered before or after the PSU has been identified with the first relevant factor, or if an access token is transported.  If this data element is contained, then there is also a hyperlink of type &#39;startAuthorisationWithAuthenticationMethodSelection&#39; contained in the response body.  These methods shall be presented towards the PSU for selection by the TPP.  | [optional] 
**transactionStatus** | [**TransactionStatus**](TransactionStatus.md) |  | 


