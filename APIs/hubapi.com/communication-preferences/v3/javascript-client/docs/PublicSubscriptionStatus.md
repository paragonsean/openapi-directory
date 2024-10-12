# Subscriptions.PublicSubscriptionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brandId** | **Number** | The ID of the brand that the subscription is associated with, if there is one. | [optional] 
**description** | **String** | A description of the subscription. | 
**id** | **String** | The ID for the subscription. | 
**legalBasis** | **String** | The legal reason for the current status of the subscription. | [optional] 
**legalBasisExplanation** | **String** | A more detailed explanation to go with the legal basis. | [optional] 
**name** | **String** | The name of the subscription. | 
**preferenceGroupName** | **String** | The name of the preferences group that the subscription is associated with. | [optional] 
**sourceOfStatus** | **String** | Where the status is determined from e.g. PORTAL_WIDE_STATUS if the contact opted out from the portal. | 
**status** | **String** | Whether the contact is subscribed. | 



## Enum: LegalBasisEnum


* `LEGITIMATE_INTEREST_PQL` (value: `"LEGITIMATE_INTEREST_PQL"`)

* `LEGITIMATE_INTEREST_CLIENT` (value: `"LEGITIMATE_INTEREST_CLIENT"`)

* `PERFORMANCE_OF_CONTRACT` (value: `"PERFORMANCE_OF_CONTRACT"`)

* `CONSENT_WITH_NOTICE` (value: `"CONSENT_WITH_NOTICE"`)

* `NON_GDPR` (value: `"NON_GDPR"`)

* `PROCESS_AND_STORE` (value: `"PROCESS_AND_STORE"`)

* `LEGITIMATE_INTEREST_OTHER` (value: `"LEGITIMATE_INTEREST_OTHER"`)





## Enum: SourceOfStatusEnum


* `PORTAL_WIDE_STATUS` (value: `"PORTAL_WIDE_STATUS"`)

* `BRAND_WIDE_STATUS` (value: `"BRAND_WIDE_STATUS"`)

* `SUBSCRIPTION_STATUS` (value: `"SUBSCRIPTION_STATUS"`)





## Enum: StatusEnum


* `SUBSCRIBED` (value: `"SUBSCRIBED"`)

* `NOT_SUBSCRIBED` (value: `"NOT_SUBSCRIBED"`)




