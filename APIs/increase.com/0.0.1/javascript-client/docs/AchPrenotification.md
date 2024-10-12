# IncreaseApi.AchPrenotification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The destination account number. | 
**addendum** | **String** | Additional information for the recipient. | 
**companyDescriptiveDate** | **String** | The description of the date of the notification. | 
**companyDiscretionaryData** | **String** | Optional data associated with the notification. | 
**companyEntryDescription** | **String** | The description of the notification. | 
**companyName** | **String** | The name by which you know the company. | 
**createdAt** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the prenotification was created. | 
**creditDebitIndicator** | **String** | If the notification is for a future credit or debit. | 
**effectiveDate** | **Date** | The effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | 
**id** | **String** | The ACH Prenotification&#39;s identifier. | 
**prenotificationReturn** | [**ACHPrenotificationReturn**](ACHPrenotificationReturn.md) |  | 
**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). | 
**status** | **String** | The lifecycle status of the ACH Prenotification. | 
**type** | **String** | A constant representing the object&#39;s type. For this resource it will always be &#x60;ach_prenotification&#x60;. | 



## Enum: CreditDebitIndicatorEnum


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)





## Enum: StatusEnum


* `pending_submitting` (value: `"pending_submitting"`)

* `requires_attention` (value: `"requires_attention"`)

* `returned` (value: `"returned"`)

* `submitted` (value: `"submitted"`)





## Enum: TypeEnum


* `ach_prenotification` (value: `"ach_prenotification"`)




