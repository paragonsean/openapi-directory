

# ExternalAccountIdentifiers

User account identifier in the third-party service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalAccountId** | **String** | User account identifier in the third-party service. Only present if account linking happened as part of the subscription purchase flow. |  [optional] |
|**obfuscatedExternalAccountId** | **String** | An obfuscated version of the id that is uniquely associated with the user&#39;s account in your app. Present for the following purchases: * If account linking happened as part of the subscription purchase flow. * It was specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedaccountid when the purchase was made. |  [optional] |
|**obfuscatedExternalProfileId** | **String** | An obfuscated version of the id that is uniquely associated with the user&#39;s profile in your app. Only present if specified using https://developer.android.com/reference/com/android/billingclient/api/BillingFlowParams.Builder#setobfuscatedprofileid when the purchase was made. |  [optional] |



