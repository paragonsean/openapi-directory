

# PublicUpdateSubscriptionStatusRequest

A request to change the status of a contact's subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailAddress** | **String** | Contact&#39;s email address. |  |
|**legalBasis** | [**LegalBasisEnum**](#LegalBasisEnum) | Legal basis for updating the contact&#39;s status (required for GDPR enabled portals). |  [optional] |
|**legalBasisExplanation** | **String** | A more detailed explanation to go with the legal basis (required for GDPR enabled portals). |  [optional] |
|**subscriptionId** | **String** | ID of the subscription being updated for the contact. |  |



## Enum: LegalBasisEnum

| Name | Value |
|---- | -----|
| LEGITIMATE_INTEREST_PQL | &quot;LEGITIMATE_INTEREST_PQL&quot; |
| LEGITIMATE_INTEREST_CLIENT | &quot;LEGITIMATE_INTEREST_CLIENT&quot; |
| PERFORMANCE_OF_CONTRACT | &quot;PERFORMANCE_OF_CONTRACT&quot; |
| CONSENT_WITH_NOTICE | &quot;CONSENT_WITH_NOTICE&quot; |
| NON_GDPR | &quot;NON_GDPR&quot; |
| PROCESS_AND_STORE | &quot;PROCESS_AND_STORE&quot; |
| LEGITIMATE_INTEREST_OTHER | &quot;LEGITIMATE_INTEREST_OTHER&quot; |



