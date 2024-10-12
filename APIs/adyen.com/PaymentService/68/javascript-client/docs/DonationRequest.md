# AdyenPaymentApi.DonationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donationAccount** | **String** | The Adyen account name of the charity. | 
**merchantAccount** | **String** | The merchant account that is used to process the payment. | 
**modificationAmount** | [**Amount**](Amount.md) | The amount to be donated.The &#x60;currency&#x60; must match the currency used in authorisation, the &#x60;value&#x60; must be smaller than or equal to the authorised amount. | 
**originalReference** | **String** | The original pspReference of the payment to modify. This reference is returned in: * authorisation response * authorisation notification   | [optional] 
**platformChargebackLogic** | [**PlatformChargebackLogic**](PlatformChargebackLogic.md) | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/marketplaces-and-platforms/processing-payments#chargebacks-and-disputes). | [optional] 
**reference** | **String** | Your reference for the payment modification. This reference is visible in Customer Area and in reports. Maximum length: 80 characters. | [optional] 


