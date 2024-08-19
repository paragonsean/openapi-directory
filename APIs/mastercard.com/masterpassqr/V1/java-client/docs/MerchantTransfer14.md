

# MerchantTransfer14

Response details for a merchant transfer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMessage** | **String** | Message a financial institution will associate to the transfer and may display.\\n\\nType: Alphanumeric Special [a-zA-Z0-9!\\\&quot;#$%&amp;&#39;()*+,-./\\\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~], Maximum Length: 65 |  [optional] |
|**created** | **String** | Date and time the original transfer was created as an ISO 8601 format.   Type: Alphanumerical Special [A-Z 0-9-:], Maximum Length: 25 |  [optional] |
|**digitalAccountReferenceNumber** | **String** | URI to identify the digital account reference number. It will include masked account information but will not include security codes (e.g. CVC or expiration date for a card account).  |  [optional] |
|**fundingSource** | **String** | Funding source must contain one of the following: CREDIT, DEBIT, PREPAID, DEPOSIT_ACCOUNT, MOBILE_MONEY_ACCOUNT or CASH. |  [optional] |
|**id** | **String** | System generated unique merchant transfer identifier.   Type: Alphanumeric Special [a-zA-Z 0-9 _], Maximum Length: 32 |  [optional] |
|**interchangeRateDesignator** | **String** | Indicates the interchange rate and editing rules applied to the transaction. Field is applicable for Europe OIs only.  Type:Alphanumeric [a-zA-Z 0-9], Length: 2 |  [optional] |
|**mastercardAssignedId** | **String** | Mastercard Assigned ID for tiered interchange calculations.   Type: Numeric [0-9], Maximum Length: 6 |  [optional] |
|**originalStatus** | **String** | Original status of the transfer. Values: APPROVED, UNKNOWN.   Type: Alpha [A-Z], Maximum Length: 8 |  [optional] |
|**participant** | [**Participant28**](Participant28.md) |  |  [optional] |
|**participationId** | **String** | Participation identifier of the sender. The receiving financial institution will associate the value to the transfer.\\n\\nType: Alphanumeric Special [a-zA-Z0-9!\\\&quot;#$%&amp;&#39;()*+,-./\\\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~], Maximum Length: 30 |  [optional] |
|**paymentOriginationCountry** | **String** | Country where the payment originated from as an ISO 3166-1 alpha-3 country code.   Type: Alpha [A-Z], Maximum Length: 3 |  [optional] |
|**paymentType** | **String** | Payment type used for transfer. Value - P2M: Person to Merchant.   Type: Alphanumeric [A-Z0-9], Maximum Length: 3 |  [optional] |
|**processorId** | **String** | The processor ID is a ten-digit number of the form: 9000xxxxxx, where the Single Message System-assigned processor ID will be up to the last six digits xxxxxx. If the partner is enrolled in multiple processorId numbers, the processorId number must be specified. If the partner is only enrolled in a single processorId number then system takes the onboarded value. Please contact your MasterCard Representative to enable the usage of fields in this section.  Type: Numeric [0-9], Maximum Length: 10 |  [optional] |
|**recipient** | [**Recipient18**](Recipient18.md) |  |  [optional] |
|**recipientAccountUri** | **String** | URI describing the recipient account. It will include masked account information but will not include security codes (e.g. CVC or expiration date for a card account). Pan, Manula Entry Alias and Alias are valid schemas. |  [optional] |
|**reconciliationData** | [**ReconciliationData26**](ReconciliationData26.md) |  |  [optional] |
|**resourceType** | **String** | Type of the resource that is being returned.   Type: Alpha Special [a-z _], Maximum Length:  17 |  [optional] |
|**routingTransitNumber** | **String** | The nine-digit Federal Reserve Routing and Transit (R &amp; T) number of the acquiring institution or the nine-digit pseudo-number assigned to the acquiring institution by Mastercard. If the partner is enrolled in multiple routing transit numbers, the routing transit number must be specified. If the partner is only enrolled in a single routing transit number then system takes the onboarded value. Please contact your MasterCard Representative to enable the usage of fields in this section.    Type: Numeric [0-9], Maximum Length: 9 |  [optional] |
|**sender** | [**Sender15**](Sender15.md) |  |  [optional] |
|**senderAccountUri** | **String** | URI describing the sending account. It will include masked account information but will not include security codes (e.g. CVC or expiration date for a card account). |  [optional] |
|**status** | **String** | Status of the transfer. Values: APPROVED, UNKNOWN.   Type: Alpha [A-Z], Maximum Length: 8 |  [optional] |
|**statusTimestamp** | **String** | Timestamp of when the status was changed to its current value.    Type: Alphanumerical Special [A-Z 0-9-:], Maximum Length: 25 |  [optional] |
|**transactionHistory** | [**TransactionHistory22**](TransactionHistory22.md) |  |  [optional] |
|**transactionLocalDateTime** | **String** | Local date and time when the transaction is submitted as an ISO 8601 format.   Type: Alphanumerical Special [A-Z 0-9-:], Maximum Length: 25 |  [optional] |
|**transferAmount** | [**TransferAmount21**](TransferAmount21.md) |  |  [optional] |
|**transferReference** | **String** | Unique transaction reference number provided by the partner when the Transfer was created.   Type: Alphanumeric Special [a-zA-Z0-9 * , - . _ ~], Maximum Length: 40 |  [optional] |



