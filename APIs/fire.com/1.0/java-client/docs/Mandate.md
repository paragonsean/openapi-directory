

# Mandate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | The name of the alias |  [optional] |
|**currency** | [**Currency**](Currency.md) |  |  [optional] |
|**dateCancelled** | **OffsetDateTime** | Date the direct debit was canceled. Milliseconds since the epoch (1970). |  [optional] |
|**dateCompleted** | **OffsetDateTime** | Date the direct debit was completed. Milliseconds since the epoch (1970). |  [optional] |
|**dateCreated** | **OffsetDateTime** | Date the direct debit was created. Milliseconds since the epoch (1970). |  [optional] |
|**fireRejectionReason** | [**FireRejectionReasonEnum**](#FireRejectionReasonEnum) | Rejection reason if transaction is rejected |  [optional] |
|**lastUpdated** | **OffsetDateTime** | Date the direct debit was last updated. Milliseconds since the epoch (1970). |  [optional] |
|**latestDirectDebitAmount** | **Long** | The value of largest direct debit collected |  [optional] |
|**latestDirectDebitDate** | **OffsetDateTime** | The date of latest direct debit collected |  [optional] |
|**mandateReference** | **String** | the reference of the mandate |  [optional] |
|**mandateUuid** | **String** | The UUID for the mandate |  [optional] |
|**numberOfDirectDebitCollected** | **Long** | The number of direct debits collected |  [optional] |
|**originatorAlias** | **String** | The name of the alias |  [optional] |
|**originatorLogoUrlLarge** | **String** | Logo url from party who sets up the direct debit. |  [optional] |
|**originatorLogoUrlSmall** | **String** | Logo url from party who sets up the direct debit. |  [optional] |
|**originatorName** | **String** | The creator of the party who sets up the direct debit. |  [optional] |
|**originatorReference** | **String** | Set by party who sets up the direct debit. |  [optional] |
|**schemeCancelReason** | **String** | Reason for cancelation |  [optional] |
|**schemeCancelReasonCode** | **String** | The cancelation code returned by the bank indicating an issue with the direct debit. Each ARRUD code represents a rejection reason. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the mandate. * &#39;CREATED&#39; * &#39;LIVE&#39; * &#39;REJECT_REQUESTED&#39; * &#39;REJECT_RECORD_IN_PROGRESS&#39; * &#39;REJECT_RECORDED&#39; * &#39;REJECT_FILE_CREATED&#39; * &#39;REJECT_FILE_SENT&#39; * &#39;CANCEL_REQUESTED&#39; * &#39;CANCEL_RECORD_IN_PROGRESS&#39; * &#39;CANCEL_RECORDED&#39; * &#39;CANCEL_FILE_CREATED&#39; * &#39;CANCEL_FILE_SENT&#39; * &#39;COMPLETE&#39; * &#39;DORMANT&#39;  |  [optional] |
|**targetIcan** | **Long** | Identifier for the fire.com account (assigned by fire.com) |  [optional] |
|**valueOfDirectDebitCollected** | **Long** | The value of direct debits collected |  [optional] |



## Enum: FireRejectionReasonEnum

| Name | Value |
|---- | -----|
| ACCOUNT_DOES_NOT_ACCEPT_DIRECT_DEBITS | &quot;ACCOUNT_DOES_NOT_ACCEPT_DIRECT_DEBITS&quot; |
| DDIC | &quot;DDIC&quot; |
| ACCOUNT_NOT_FOUND | &quot;ACCOUNT_NOT_FOUND&quot; |
| ACCOUNT_NOT_LIVE | &quot;ACCOUNT_NOT_LIVE&quot; |
| CUSTOMER_NOT_FOUND | &quot;CUSTOMER_NOT_FOUND&quot; |
| BUSINESS_NOT_LIVE | &quot;BUSINESS_NOT_LIVE&quot; |
| BUSINESS_NOT_FULL | &quot;BUSINESS_NOT_FULL&quot; |
| PERSONAL_USER_NOT_LIVE | &quot;PERSONAL_USER_NOT_LIVE&quot; |
| PERSONAL_USER_NOT_FULL | &quot;PERSONAL_USER_NOT_FULL&quot; |
| MANDATE_ALREADY_EXISTS | &quot;MANDATE_ALREADY_EXISTS&quot; |
| MANDATE_WITH_DIFERENT_ACCOUNT | &quot;MANDATE_WITH_DIFERENT_ACCOUNT&quot; |
| NULL_MANDATE_REFERENCE | &quot;NULL_MANDATE_REFERENCE&quot; |
| INVALID_ACCOUNT_CURRENCY | &quot;INVALID_ACCOUNT_CURRENCY&quot; |
| INVALID_MANDATE_REFERENCE | &quot;INVALID_MANDATE_REFERENCE&quot; |
| REQUESTED_BY_CUSTOMER_VIA_SUPPORT | &quot;REQUESTED_BY_CUSTOMER_VIA_SUPPORT&quot; |
| CUSTOMER_ACCOUNT_CLOSED | &quot;CUSTOMER_ACCOUNT_CLOSED&quot; |
| CUSTOMER_DECEASED | &quot;CUSTOMER_DECEASED&quot; |
| ACCOUNT_TRANSFERRED | &quot;ACCOUNT_TRANSFERRED&quot; |
| MANDATE_NOT_FOUND | &quot;MANDATE_NOT_FOUND&quot; |
| ACCOUNT_TRANSFERRED_TO_DIFFERENT_ACCOUNT | &quot;ACCOUNT_TRANSFERRED_TO_DIFFERENT_ACCOUNT&quot; |
| INVALID_ACCOUNT_TYPE | &quot;INVALID_ACCOUNT_TYPE&quot; |
| MANDATE_EXPIRED | &quot;MANDATE_EXPIRED&quot; |
| MANDATE_CANCELLED | &quot;MANDATE_CANCELLED&quot; |
| REQUESTED_BY_CUSTOMER | &quot;REQUESTED_BY_CUSTOMER&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;CREATED&quot; |
| LIVE | &quot;LIVE&quot; |
| REJECT_REQUESTED | &quot;REJECT_REQUESTED&quot; |
| REJECT_RECORD_IN_PROGRESS | &quot;REJECT_RECORD_IN_PROGRESS&quot; |
| REJECT_RECORDED | &quot;REJECT_RECORDED&quot; |
| REJECT_FILE_CREATED | &quot;REJECT_FILE_CREATED&quot; |
| REJECT_FILE_SENT | &quot;REJECT_FILE_SENT&quot; |
| CANCEL_REQUESTED | &quot;CANCEL_REQUESTED&quot; |
| CANCEL_RECORD_IN_PROGRESS | &quot;CANCEL_RECORD_IN_PROGRESS&quot; |
| CANCEL_RECORDED | &quot;CANCEL_RECORDED&quot; |
| CANCEL_FILE_CREATED | &quot;CANCEL_FILE_CREATED&quot; |
| CANCEL_FILE_SENT | &quot;CANCEL_FILE_SENT&quot; |
| COMPLETE | &quot;COMPLETE&quot; |
| DORMANT | &quot;DORMANT&quot; |



