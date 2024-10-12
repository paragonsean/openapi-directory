

# Transaction81

Array of transactions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountUri** | **String** | Scrubbed URI describing the account. It will include masked account information (e.g. \&quot;************1234\&quot; for a card account) but will not include security codes (e.g. CVC or expiration date for a card account).  |  [optional] |
|**authorizationId** | **String** | Transaction response ID code that the authorizing institution assigns.    Type: Alphanumeric [a-zA-Z 0-9], Length: 6. |  [optional] |
|**convenienceAmount** | **String** | Amount of the convenience fee. The decimal point is implied based on the transaction_amount.currency. \&quot;[0-9]*\&quot;. Max Length: 12. Value must be less than payment_transfer.amount. |  [optional] |
|**convenienceIndicator** | **String** | Convenience fee type code. Min length: 2. Max Length: 2. Valid values  (01: Indicates Consumer should be prompted to enter tip 02: Indicates that merchant would mandatorily charge a flat convenience fee 03: Indicates that merchant would charge a percentage convenience fee) |  [optional] |
|**createTimestamp** | **String** | Date and time the transaction was created as an ISO 8601 Timestamp. [YYYY-MM-DDTHH:MM:SS±hh[:mm]] |  [optional] |
|**id** | **String** | System generated unique transfer identifier. |  [optional] |
|**network** | **String** | Name of the network that processed this transaction. |  [optional] |
|**networkStatusCode** | **String** | Network Status Code in case of Decline |  [optional] |
|**networkStatusDescription** | **String** | Network Status Description in case of Decline |  [optional] |
|**paymentAccountReference** | **String** | A unique value associated with a single PAN and attributed to all tokens associated with that PAN.    Type: Alphanumeric [a-zA-Z 0-9], Length: 29. |  [optional] |
|**qrData** | **String** | Encoded QR (Quick Response) code data. Type: Alphanumeric and special characters [a-zA-Z0-9!\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~], Maximum Length: 237 |  [optional] |
|**resourceType** | **String** | Type of resource. Valid value:  transaction |  [optional] |
|**retrievalReference** | **String** | Unique reference number that identifies the transaction at the network. Details- maxlength 24 |  [optional] |
|**status** | **String** | Status of this transaction. One of APPROVED, DECLINED, UNKNOWN, ERROR, or PENDING. |  [optional] |
|**statusReason** | **String** | Reason for status One of [APPROVED, DECLINED, FRAUD, CARD_EXPIRED, LIMIT_EXCEEDED,UNKNOWN, ERROR or PENDING] The following status reason will be provided based on the status APPROVED: APPROVED; UNKNOWN:UNKNOWN, ERROR:ERROR, PENDING: PENDING;DECLINED: DECLINED, FRAUD, CARD_EXPIRED, LIMIT_EXCEEDED; |  [optional] |
|**statusTimestamp** | **String** | Date and time of the status as an ISO 8601 Timestamp. [YYYY-MM-DDTHH:MM:SS±hh[:mm]] |  [optional] |
|**switchSerialNumber** | **String** | Unique transaction identification number (switch serial number) generated (or assigned) by the Single Message System.Type: Numeric [0-9], Maximum Length: 9 |  [optional] |
|**systemTraceAuditNumber** | **String** | Unique system trace audit number for the transaction, the STAN ( system trace audit number ). Details- maxlength 6 |  [optional] |
|**transactionAmount** | [**TransactionAmount82**](TransactionAmount82.md) |  |  [optional] |
|**type** | **String** | Type of the transaction. One of: FUNDING, PAYMENT, FUNDING_REVERSAL, or PAYMENT_REVERSAL. |  [optional] |
|**uniqueReferenceNumber** | **String** | Unique reference number for the transaction. Type: Alphanumeric Special [a-zA-Z0-9 * , - . _ ~ ], Length: 19 |  [optional] |



