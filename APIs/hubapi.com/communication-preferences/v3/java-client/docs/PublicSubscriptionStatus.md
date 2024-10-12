

# PublicSubscriptionStatus

The status of a subscription for a contact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brandId** | **Long** | The ID of the brand that the subscription is associated with, if there is one. |  [optional] |
|**description** | **String** | A description of the subscription. |  |
|**id** | **String** | The ID for the subscription. |  |
|**legalBasis** | [**LegalBasisEnum**](#LegalBasisEnum) | The legal reason for the current status of the subscription. |  [optional] |
|**legalBasisExplanation** | **String** | A more detailed explanation to go with the legal basis. |  [optional] |
|**name** | **String** | The name of the subscription. |  |
|**preferenceGroupName** | **String** | The name of the preferences group that the subscription is associated with. |  [optional] |
|**sourceOfStatus** | [**SourceOfStatusEnum**](#SourceOfStatusEnum) | Where the status is determined from e.g. PORTAL_WIDE_STATUS if the contact opted out from the portal. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the contact is subscribed. |  |



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



## Enum: SourceOfStatusEnum

| Name | Value |
|---- | -----|
| PORTAL_WIDE_STATUS | &quot;PORTAL_WIDE_STATUS&quot; |
| BRAND_WIDE_STATUS | &quot;BRAND_WIDE_STATUS&quot; |
| SUBSCRIPTION_STATUS | &quot;SUBSCRIPTION_STATUS&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBSCRIBED | &quot;SUBSCRIBED&quot; |
| NOT_SUBSCRIBED | &quot;NOT_SUBSCRIBED&quot; |



