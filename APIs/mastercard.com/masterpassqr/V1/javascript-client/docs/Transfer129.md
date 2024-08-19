# SendPersonToMerchant.Transfer129

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel** | **String** | Initiation channel of the transfer request. Values: WEB, MOBILE, BANK, KIOSK. | [optional] 
**created** | **String** | Date and time the original transfer was created as an ISO 8601 Timestamp. Details- YYYY-MM-DDTHH:MM:SSZ Valid Values- Refer &#39;Date And Time Formats&#39; | [optional] 
**deviceId** | **String** | The serial number of a device that initiated the transfer. | [optional] 
**id** | **String** | System generated unique transfer identifier. | [optional] 
**interchangeRateDesignator** | **String** | Indicates the interchange rate and editing rules applied to the transaction.  Type:Alphanumeric [a-zA-Z 0-9], Length: 2 | [optional] 
**location** | **String** | Location where the transaction is initiated. | [optional] 
**originalStatus** | **String** | Original status of the transfer. One of APPROVED, DECLINED, ERROR, PENDING, UNKNOWN. | [optional] 
**paymentType** | **String** | Payment type used for transfer. Value - P2M: Person to Merchant. \\n\\nType: Alphanumeric [A-Z0-9], Maximum Length: 3 | [optional] 
**recipient** | [**Recipient134**](Recipient134.md) |  | [optional] 
**recipientAccountUri** | **String** | URI describing the recipient account. It will include masked account information (e.g. \&quot;************1234\&quot; for a card account) but will not include security codes (e.g. CVC or expiration date for a card account). | [optional] 
**reconciliationData** | [**ReconciliationData142**](ReconciliationData142.md) |  | [optional] 
**resourceType** | **String** | Type of resource | [optional] 
**sanctionScreeningOverride** | **Boolean** | Sanction Screening validation override if enabled for partner. | [optional] 
**sender** | [**Sender130**](Sender130.md) |  | [optional] 
**senderAccountUri** | **String** | URI describing the sending account. It will include masked account information (e.g. \&quot;************1234\&quot; for a card account) but will not include security codes (e.g. CVC or expiration date for a card account). | [optional] 
**statementDescriptor** | **String** | The statement descriptor is the value that will be displayed on the recipient&#39;s bank or card statement. It consists of two parts: the prefix and the content. The prefix is a short string typically used to identify the partner. The appended &amp;lt;prefix&amp;gt;*&amp;lt;content&amp;gt; will be displayed on the recipient&#39;s statement. Note: While most financial institutions display this information consistently, some may display it incorrectly or not at all. | [optional] 
**status** | **String** | Status of the transfer. Values: APPROVED, DECLINED, ERROR, PENDING, REVERSED, CANCELLED. | [optional] 
**statusTimestamp** | **String** | Timestamp of when the status was changed to its current value. Details- YYYY-MM-DDTHH:MM:SSZ Valid Values- Refer &#39;Date And Time Formats&#39; | [optional] 
**transactionHistory** | [**TransactionHistory138**](TransactionHistory138.md) |  | [optional] 
**transferAmount** | [**TransferAmount137**](TransferAmount137.md) |  | [optional] 
**transferReference** | **String** | Unique transaction reference number provided when the Transfer was created. | [optional] 


