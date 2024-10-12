# SendPersonToMerchant.Transaction49

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountUri** | **String** | account uri | [optional] 
**authorizationId** | **String** | Transaction response ID code that the authorizing institution assigns.    Type: Alphanumeric [a-zA-Z 0-9], Length: 6. | [optional] 
**createTimestamp** | **String** | Date and time the transaction was created as an ISO 8601 Timestamp. [YYYY-MM-DDTHH:MM:SSZ] | [optional] 
**fundsAvailability** | **String** | An estimate of when the funds might be available. Actual Deposit Availability is determined by the financial institution.[One of: IMMEDIATE, NEXT_BUSINESS_DAY, or TWO_TO_FIVE_BUSINESS_DAYS.] | [optional] 
**id** | **String** | System generated unique transfer identifier. | [optional] 
**network** | **String** | Proposed network for the transaction. | [optional] 
**networkStatusCode** | **String** | Network Status Code in case of Decline | [optional] 
**networkStatusDescription** | **String** | Network Status Description in case of Decline | [optional] 
**paymentAccountReference** | **String** | A unique value associated with a single PAN and attributed to all tokens associated with that PAN.    Type: Alphanumeric [a-zA-Z 0-9], Length: 29. | [optional] 
**resourceType** | **String** | Type of resource. Valid value:  transaction | [optional] 
**retrievalReference** | **String** | Unique reference number that identifies the transaction at the network. Details- maxlength 24 | [optional] 
**status** | **String** | Status of the disbursement. One of APPROVED, DECLINED, UNKNOWN, ERROR, or PENDING. | [optional] 
**statusReason** | **String** | Reason for status, APPROVED, DECLINED, FRAUD, CARD_EXPIRED, LIMIT_EXCEEDED, UNKNOWN, ERROR, PENDING | [optional] 
**statusTimestamp** | **String** | Date and time of when the status was changed to its current value as an ISO 8601 Timestamp. [YYYY-MM-DDTHH:MM:SSZ | [optional] 
**switchSerialNumber** | **String** | Unique transaction identification number (switch serial number) generated (or assigned) by the Single Message System.Type: Numeric [0-9], Maximum Length: 9 | [optional] 
**systemTraceAuditNumber** | **String** | Unique system trace audit number for the transaction, the STAN ( system trace audit number ). Details- maxlength 6 | [optional] 
**transactionAmount** | [**TransactionAmount50**](TransactionAmount50.md) |  | [optional] 
**type** | **String** | Type of the transaction. One of: FUNDING, PAYMENT, FUNDING_REVERSAL, or PAYMENT_REVERSAL. | [optional] 
**uniqueReferenceNumber** | **String** | Unique reference number for the transaction. Type: Alphanumeric Special [a-zA-Z0-9 * , - . _ ~ ], Length: 19 | [optional] 


