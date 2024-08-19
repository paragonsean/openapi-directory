# RocketServices.AccountUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**defaultPaymentInstrumentId** | **String** | The id of the payment instrument to use by default for account transactions.  **DEPRECATED** The property &#x60;defaultPaymentMethodId&#x60; is now preferred.  | [optional] 
**defaultPaymentMethodId** | **String** | The id of the payment method to use by default for account transactions. | [optional] 
**firstName** | **String** | The first name of the account holder. | [optional] 
**lastName** | **String** | The last name of the account holder. | [optional] 
**minRatingPlaybackGuard** | **String** | The classification rating defining the minimum rating level a user should be forced to enter the account pin code for playback. Anything at this rating level or above will require the pin for playback.  e.g. AUOFLC-MA15+  If you want to disable this guard pass an empty string or &#x60;null&#x60;.  | [optional] 
**segments** | **[String]** | The segments an account should be placed under | [optional] 
**trackingEnabled** | **Boolean** | Whether usage tracking is associated with an account or anonymous. | [optional] 


