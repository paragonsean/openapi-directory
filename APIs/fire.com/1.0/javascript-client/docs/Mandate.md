# FireFinancialServicesBusinessApi.Mandate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | The name of the alias | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**dateCancelled** | **Date** | Date the direct debit was canceled. Milliseconds since the epoch (1970). | [optional] 
**dateCompleted** | **Date** | Date the direct debit was completed. Milliseconds since the epoch (1970). | [optional] 
**dateCreated** | **Date** | Date the direct debit was created. Milliseconds since the epoch (1970). | [optional] 
**fireRejectionReason** | **String** | Rejection reason if transaction is rejected | [optional] 
**lastUpdated** | **Date** | Date the direct debit was last updated. Milliseconds since the epoch (1970). | [optional] 
**latestDirectDebitAmount** | **Number** | The value of largest direct debit collected | [optional] 
**latestDirectDebitDate** | **Date** | The date of latest direct debit collected | [optional] 
**mandateReference** | **String** | the reference of the mandate | [optional] 
**mandateUuid** | **String** | The UUID for the mandate | [optional] 
**numberOfDirectDebitCollected** | **Number** | The number of direct debits collected | [optional] 
**originatorAlias** | **String** | The name of the alias | [optional] 
**originatorLogoUrlLarge** | **String** | Logo url from party who sets up the direct debit. | [optional] 
**originatorLogoUrlSmall** | **String** | Logo url from party who sets up the direct debit. | [optional] 
**originatorName** | **String** | The creator of the party who sets up the direct debit. | [optional] 
**originatorReference** | **String** | Set by party who sets up the direct debit. | [optional] 
**schemeCancelReason** | **String** | Reason for cancelation | [optional] 
**schemeCancelReasonCode** | **String** | The cancelation code returned by the bank indicating an issue with the direct debit. Each ARRUD code represents a rejection reason. | [optional] 
**status** | **String** | The status of the mandate. * &#39;CREATED&#39; * &#39;LIVE&#39; * &#39;REJECT_REQUESTED&#39; * &#39;REJECT_RECORD_IN_PROGRESS&#39; * &#39;REJECT_RECORDED&#39; * &#39;REJECT_FILE_CREATED&#39; * &#39;REJECT_FILE_SENT&#39; * &#39;CANCEL_REQUESTED&#39; * &#39;CANCEL_RECORD_IN_PROGRESS&#39; * &#39;CANCEL_RECORDED&#39; * &#39;CANCEL_FILE_CREATED&#39; * &#39;CANCEL_FILE_SENT&#39; * &#39;COMPLETE&#39; * &#39;DORMANT&#39;  | [optional] 
**targetIcan** | **Number** | Identifier for the fire.com account (assigned by fire.com) | [optional] 
**valueOfDirectDebitCollected** | **Number** | The value of direct debits collected | [optional] 



## Enum: FireRejectionReasonEnum


* `ACCOUNT_DOES_NOT_ACCEPT_DIRECT_DEBITS` (value: `"ACCOUNT_DOES_NOT_ACCEPT_DIRECT_DEBITS"`)

* `DDIC` (value: `"DDIC"`)

* `ACCOUNT_NOT_FOUND` (value: `"ACCOUNT_NOT_FOUND"`)

* `ACCOUNT_NOT_LIVE` (value: `"ACCOUNT_NOT_LIVE"`)

* `CUSTOMER_NOT_FOUND` (value: `"CUSTOMER_NOT_FOUND"`)

* `BUSINESS_NOT_LIVE` (value: `"BUSINESS_NOT_LIVE"`)

* `BUSINESS_NOT_FULL` (value: `"BUSINESS_NOT_FULL"`)

* `PERSONAL_USER_NOT_LIVE` (value: `"PERSONAL_USER_NOT_LIVE"`)

* `PERSONAL_USER_NOT_FULL` (value: `"PERSONAL_USER_NOT_FULL"`)

* `MANDATE_ALREADY_EXISTS` (value: `"MANDATE_ALREADY_EXISTS"`)

* `MANDATE_WITH_DIFERENT_ACCOUNT` (value: `"MANDATE_WITH_DIFERENT_ACCOUNT"`)

* `NULL_MANDATE_REFERENCE` (value: `"NULL_MANDATE_REFERENCE"`)

* `INVALID_ACCOUNT_CURRENCY` (value: `"INVALID_ACCOUNT_CURRENCY"`)

* `INVALID_MANDATE_REFERENCE` (value: `"INVALID_MANDATE_REFERENCE"`)

* `REQUESTED_BY_CUSTOMER_VIA_SUPPORT` (value: `"REQUESTED_BY_CUSTOMER_VIA_SUPPORT"`)

* `CUSTOMER_ACCOUNT_CLOSED` (value: `"CUSTOMER_ACCOUNT_CLOSED"`)

* `CUSTOMER_DECEASED` (value: `"CUSTOMER_DECEASED"`)

* `ACCOUNT_TRANSFERRED` (value: `"ACCOUNT_TRANSFERRED"`)

* `MANDATE_NOT_FOUND` (value: `"MANDATE_NOT_FOUND"`)

* `ACCOUNT_TRANSFERRED_TO_DIFFERENT_ACCOUNT` (value: `"ACCOUNT_TRANSFERRED_TO_DIFFERENT_ACCOUNT"`)

* `INVALID_ACCOUNT_TYPE` (value: `"INVALID_ACCOUNT_TYPE"`)

* `MANDATE_EXPIRED` (value: `"MANDATE_EXPIRED"`)

* `MANDATE_CANCELLED` (value: `"MANDATE_CANCELLED"`)

* `REQUESTED_BY_CUSTOMER` (value: `"REQUESTED_BY_CUSTOMER"`)





## Enum: StatusEnum


* `CREATED` (value: `"CREATED"`)

* `LIVE` (value: `"LIVE"`)

* `REJECT_REQUESTED` (value: `"REJECT_REQUESTED"`)

* `REJECT_RECORD_IN_PROGRESS` (value: `"REJECT_RECORD_IN_PROGRESS"`)

* `REJECT_RECORDED` (value: `"REJECT_RECORDED"`)

* `REJECT_FILE_CREATED` (value: `"REJECT_FILE_CREATED"`)

* `REJECT_FILE_SENT` (value: `"REJECT_FILE_SENT"`)

* `CANCEL_REQUESTED` (value: `"CANCEL_REQUESTED"`)

* `CANCEL_RECORD_IN_PROGRESS` (value: `"CANCEL_RECORD_IN_PROGRESS"`)

* `CANCEL_RECORDED` (value: `"CANCEL_RECORDED"`)

* `CANCEL_FILE_CREATED` (value: `"CANCEL_FILE_CREATED"`)

* `CANCEL_FILE_SENT` (value: `"CANCEL_FILE_SENT"`)

* `COMPLETE` (value: `"COMPLETE"`)

* `DORMANT` (value: `"DORMANT"`)




