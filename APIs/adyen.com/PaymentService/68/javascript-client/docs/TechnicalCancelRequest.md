# AdyenPaymentApi.TechnicalCancelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | [**AdjustAuthorisationRequestAdditionalData**](AdjustAuthorisationRequestAdditionalData.md) |  | [optional] 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**modificationAmount** | [**Amount**](Amount.md) | The amount that needs to be captured/refunded. Required for &#x60;/capture&#x60; and &#x60;/refund&#x60;, not allowed for &#x60;/cancel&#x60;. The &#x60;currency&#x60; must match the currency used in authorisation, the &#x60;value&#x60; must be smaller than or equal to the authorised amount. | [optional] 
**mpiData** | [**ThreeDSecureData**](ThreeDSecureData.md) | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). | [optional] 
**originalMerchantReference** | **String** | The original merchant reference to cancel. | 
**platformChargebackLogic** | [**PlatformChargebackLogic**](PlatformChargebackLogic.md) | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#chargebacks-and-disputes). | [optional] 
**reference** | **String** | Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters. | [optional] 
**splits** | [**[Split]**](Split.md) | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For details, refer to [Providing split information](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#providing-split-information). | [optional] 
**tenderReference** | **String** | The transaction reference provided by the PED. For point-of-sale integrations only. | [optional] 
**uniqueTerminalId** | **String** | Unique terminal ID for the PED that originally processed the request. For point-of-sale integrations only. | [optional] 


