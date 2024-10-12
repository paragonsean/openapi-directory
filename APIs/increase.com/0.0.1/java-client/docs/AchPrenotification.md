

# AchPrenotification

ACH Prenotifications are one way you can verify account and routing numbers by Automated Clearing House (ACH).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The destination account number. |  |
|**addendum** | **String** | Additional information for the recipient. |  |
|**companyDescriptiveDate** | **String** | The description of the date of the notification. |  |
|**companyDiscretionaryData** | **String** | Optional data associated with the notification. |  |
|**companyEntryDescription** | **String** | The description of the notification. |  |
|**companyName** | **String** | The name by which you know the company. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the prenotification was created. |  |
|**creditDebitIndicator** | [**CreditDebitIndicatorEnum**](#CreditDebitIndicatorEnum) | If the notification is for a future credit or debit. |  |
|**effectiveDate** | **OffsetDateTime** | The effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  |
|**id** | **String** | The ACH Prenotification&#39;s identifier. |  |
|**prenotificationReturn** | [**ACHPrenotificationReturn**](ACHPrenotificationReturn.md) |  |  |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**status** | [**StatusEnum**](#StatusEnum) | The lifecycle status of the ACH Prenotification. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;ach_prenotification&#x60;. |  |



## Enum: CreditDebitIndicatorEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_SUBMITTING | &quot;pending_submitting&quot; |
| REQUIRES_ATTENTION | &quot;requires_attention&quot; |
| RETURNED | &quot;returned&quot; |
| SUBMITTED | &quot;submitted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACH_PRENOTIFICATION | &quot;ach_prenotification&quot; |



