

# MerchantTransfer71

An array containing the Transactions in the transfer

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | **String** | Initiation channel of the transfer request. Values: WEB, MOBILE, BANK, KIOSK. |  [optional] |
|**created** | **String** | Date and time the original transfer was created as an ISO 8601 Timestamp. Details- YYYY-MM-DDTHH:MM:SS±hh[:mm] Valid Values- Refer &#39;Date And Time Formats |  [optional] |
|**deviceId** | **String** | The serial number of a device that initiated the transfer. |  [optional] |
|**digitalAccountReferenceNumber** | **String** | Reference number identifying the digital account reference number. Details- Numeric, Length 1-20 |  [optional] |
|**fundingSource** | **String** | Funding source must contain one of the following: CREDIT, DEBIT, PREPAID, DEPOSIT_ACCOUNT, MOBILE_MONEY_ACCOUNT, CASH.  |  [optional] |
|**id** | **String** | System generated unique merchant transfer identifier. |  [optional] |
|**interchangeRateDesignator** | **String** | Indicates the interchange rate and editing rules applied to the transaction. Field is applicable for Europe OIs only.  Type:Alphanumeric [a-zA-Z 0-9], Length: 2 |  [optional] |
|**location** | **String** | Location where the transaction is initiated. Valid Values- Refer &#39;Location URIs&#39;. |  [optional] |
|**originalStatus** | **String** | Original status of the transfer. One of APPROVED, DECLINED, ERROR, PENDING, UNKNOWN. |  [optional] |
|**participant** | [**Participant85**](Participant85.md) |  |  [optional] |
|**paymentOriginationCountry** | **String** | Country where the payment originated from as an ISO 3166-1 alpha-3 country code, in uppercase. Details- Alpha, Length: 3 |  [optional] |
|**paymentType** | **String** | P2M: Person to Merchant |  [optional] |
|**processorId** | **String** | The processor ID is a ten-digit number of the form: 9000xxxxxx, where the Single Message System-assigned processor ID will be up to the last six digits xxxxxx. If the partner is enrolled in multiple processorId numbers, the processorId number must be specified. If the partner is only enrolled in a single processorId number then system takes the onboarded value. Please contact your MasterCard Representative to enable the usage of fields in this section. Details- Numeric, 10 |  [optional] |
|**recipient** | [**Recipient75**](Recipient75.md) |  |  [optional] |
|**recipientAccountUri** | **String** | URI describing the recipient/merchant account. It will include masked account information (e.g. \&quot;************1234\&quot; for a card account) but will not include security codes (e.g. CVC or expiration date for a card account). |  [optional] |
|**reconciliationData** | [**ReconciliationData83**](ReconciliationData83.md) |  |  [optional] |
|**resourceType** | **String** | Type of the resource that is being returned. Valid value: merchant_transfer |  [optional] |
|**routingTransitNumber** | **String** | The nine-digit Federal Reserve Routing and Transit (R &amp; T) number of the acquiring institution or the nine-digit pseudo-number assigned to the acquiring institution by Mastercard. If the partner is enrolled in multiple routing transit numbers, the routing transit number must be specified. If the partner is only enrolled in a single routing transit number then system takes the onboarded value. Please contact your MasterCard Representative to enable the usage of fields in this section. Details- Numeric, 9 |  [optional] |
|**sender** | [**Sender72**](Sender72.md) |  |  [optional] |
|**senderAccountUri** | **String** | URI describing the sending account. It will include masked account information (e.g. \&quot;************1234\&quot; for a card account) but will not include security codes (e.g. CVC or expiration date for a card account). |  [optional] |
|**status** | **String** | Status of the transfer. Values: APPROVED, DECLINED, ERROR, PENDING, REVERSED, CANCELLED. |  [optional] |
|**statusTimestamp** | **String** | Timestamp of when the status was changed to its current value. Details-YYYY-MM-DDTHH:MM:SS±hh[:mm] Valid Values- Refer &#39;Date And Time Formats |  [optional] |
|**transactionHistory** | [**TransactionHistory79**](TransactionHistory79.md) |  |  [optional] |
|**transactionLocalDateTime** | **String** | Local date and time when the transaction is submitted. Details-YYYY-MM-DDTHH:MM:SS±hh[:mm]  |  [optional] |
|**transferAmount** | [**TransferAmount78**](TransferAmount78.md) |  |  [optional] |
|**transferReference** | **String** | Unique transaction reference number provided when the Transfer was created. |  [optional] |



