# RocketServices.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**defaultPaymentInstrumentId** | **String** | The id of the payment instrument to use by default for account transactions.   **DEPRECATED** The property &#x60;defaultPaymentMethodId&#x60; is now preferred.  | [optional] 
**defaultPaymentMethodId** | **String** | The id of the payment method to use by default for account transactions. | [optional] 
**emailVerified** | **Boolean** | Whether the email address has been verified.  Users who receive an emailed verification url click the link to verify their email address.  | [optional] 
**entitlements** | [**[Entitlement]**](Entitlement.md) | The list of entitlements to playback specific items. | [optional] 
**firstName** | **String** | The first name of the account holder. | [optional] 
**id** | **String** | The id of the account. | 
**isFirstTimeSubscriber** | **Boolean** | Whether the account has the very first subscription. | [optional] 
**lastName** | **String** | The last name of the account holder. | [optional] 
**marketingEnabled** | **Boolean** | Whether the account has opted in or out of marketing material. | 
**minRatingPlaybackGuard** | **String** | The classification rating defining the minimum rating level a user should be forced to enter the account pin code for playback. Anything at this rating level or above will require the pin for playback.  e.g. AUOFLC-MA15+  If you want to disable this guard pass an empty string or &#x60;null&#x60;.  | [optional] 
**pinEnabled** | **Boolean** | When an account level pin is defined this will be true. | 
**primaryProfileId** | **String** | The id of the primary profile. | 
**profiles** | [**[ProfileSummary]**](ProfileSummary.md) | The list of profiles under this account. | 
**segments** | **[String]** | The segments an account has been placed under | [optional] 
**subscriptionCode** | **String** | The active subscription code for an account.  The value of this should be passed to any endpoints accepting a &#x60;sub&#x60; query parameter.  | 
**subscriptions** | [**[Subscription]**](Subscription.md) | The list of subscriptions, if any, the account has signed up to. | [optional] 
**trackingEnabled** | **Boolean** | Whether usage tracking is associated with the account or anonymous. | 
**usedFreeTrial** | **Boolean** | Whether the account has used up their free trial period of a plan. | [optional] 


