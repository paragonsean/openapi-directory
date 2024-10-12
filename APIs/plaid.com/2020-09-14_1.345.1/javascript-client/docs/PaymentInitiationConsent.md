# ThePlaidApi.PaymentInitiationConsent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentId** | **String** | The consent ID. | 
**constraints** | [**PaymentInitiationConsentConstraints**](PaymentInitiationConsentConstraints.md) |  | 
**createdAt** | **Date** | Consent creation timestamp, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. | 
**recipientId** | **String** | The ID of the recipient the payment consent is for. | 
**reference** | **String** | A reference for the payment consent. | 
**scopes** | [**[PaymentInitiationConsentScope]**](PaymentInitiationConsentScope.md) | An array of payment consent scopes. | 
**status** | [**PaymentInitiationConsentStatus**](PaymentInitiationConsentStatus.md) |  | 


