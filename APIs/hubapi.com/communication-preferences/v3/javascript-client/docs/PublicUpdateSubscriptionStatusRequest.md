# Subscriptions.PublicUpdateSubscriptionStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailAddress** | **String** | Contact&#39;s email address. | 
**legalBasis** | **String** | Legal basis for updating the contact&#39;s status (required for GDPR enabled portals). | [optional] 
**legalBasisExplanation** | **String** | A more detailed explanation to go with the legal basis (required for GDPR enabled portals). | [optional] 
**subscriptionId** | **String** | ID of the subscription being updated for the contact. | 



## Enum: LegalBasisEnum


* `LEGITIMATE_INTEREST_PQL` (value: `"LEGITIMATE_INTEREST_PQL"`)

* `LEGITIMATE_INTEREST_CLIENT` (value: `"LEGITIMATE_INTEREST_CLIENT"`)

* `PERFORMANCE_OF_CONTRACT` (value: `"PERFORMANCE_OF_CONTRACT"`)

* `CONSENT_WITH_NOTICE` (value: `"CONSENT_WITH_NOTICE"`)

* `NON_GDPR` (value: `"NON_GDPR"`)

* `PROCESS_AND_STORE` (value: `"PROCESS_AND_STORE"`)

* `LEGITIMATE_INTEREST_OTHER` (value: `"LEGITIMATE_INTEREST_OTHER"`)




