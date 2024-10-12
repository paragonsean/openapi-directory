# SendPersonToMerchant.MerchantPaymentTransfer29

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalMessage** | **String** | Message a financial institution will associate to the transfer and may display. \\n\\nType: Alphanumeric Special [a-zA-Z0-9!\\\&quot;#$%&amp;&#39;()*+,-./\\\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~], Length: 1-65 | [optional] 
**amount** | **String** | Amount of the transfer. The decimal point is implied based on the payment transfer currency. Details- 1-999999999999 | 
**authenticationValue** | **String** | List of name/value pairs containing authentication  values. Refer &#39;Authentication Value URIs&#39; | [optional] 
**channel** | **String** | Initiation channel of the transfer request. This value can be defined in the onboarding process instead of passing in every call. Values: WEB, MOBILE, BANK, KIOSK. Details- Conditional | [optional] 
**convenienceAmount** | **String** | Tip or convenience amount in transaction currency. Length:1-12 numeric. If present, then convenience_indicator is also required. | [optional] 
**convenienceIndicator** | **String** | Convenience fee type code. Min length: 2. Max Length: 2. Valid values are 01,02 or 03. 01:Indicates consumer should be prompted to enter tip. 02:Indicates the merchant would mandatorily charge a flat convenience fee. 03:Indicates that merchant would charge a percentage convenience fee. Required if convenience_amount is provided. | [optional] 
**currency** | **String** | Currency of the transfer amount as an ISO alpha currency code. Details- Alpha, Length: 3 | 
**deviceId** | **String** | The serial number of a device initiating the transfer. Details- 1-40 | [optional] 
**digitalAccountReferenceNumber** | **String** | URI to identify the digital account reference number. URI scheme must be pan. Valid Values- Refer &#39;Account URIs&#39;. | [optional] 
**fundingSource** | **String** | Funding source must contain one of the following: CREDIT, DEBIT, PREPAID, DEPOSIT_ACCOUNT, MOBILE_MONEY_ACCOUNT, CASH. In the Asia/Pacific region, funding sources are limited to Mastercard cards. In Subfield 1 values 04, 05, 06, and 07 are not applicable. | 
**fundingTransactionReference** | [**FundingTransactionReference38**](FundingTransactionReference38.md) |  | [optional] 
**interchangeRateDesignator** | **String** | Indicates the interchange rate and editing rules applied to the transaction.  Type:Alphanumeric [a-zA-Z 0-9], Length: 2 | [optional] 
**location** | **String** | Location where the transaction is initiated. Valid Values- Refer &#39;Location URIs&#39;. | [optional] 
**mastercardAssignedId** | **String** | Mastercard Assigned ID for tiered interchange calculations. \\n\\nType: Numeric [0-9], Length: 6 | [optional] 
**participant** | [**Participant37**](Participant37.md) |  | [optional] 
**participationId** | **String** | Participation identifier of the sender. The receiving financial institution will associate the value to the transfer. Details- 1-30 | [optional] 
**paymentOriginationCountry** | **String** | The country where the payment originates from as an ISO 3166-1 alpha-3 country code, in uppercase. Details - Conditional. If provided, this should match a valid country configured for the partner during onboarding. If the partner is configured for multiple origination countries this field is required and must be provided. Alpha, length: 3 | [optional] 
**paymentType** | **String** | P2M: Person to Merchant | 
**processorId** | **String** | The processor ID is a ten-digit number of the form: 9000xxxxxx, where the Single Message System-assigned processor ID will be up to the last six digits xxxxxx. If the partner is enrolled in multiple processorId numbers, the processorId number must be specified. If the partner is only enrolled in a single processorId number then system takes the onboarded value. Please contact your MasterCard Representative to enable the usage of fields in this section. Details- Numeric, 10 | [optional] 
**qrData** | **String** | Contains QR data. For future use. Details- alpha numeric special characters 1-237. | [optional] 
**recipient** | [**Recipient32**](Recipient32.md) |  | 
**recipientAccountUri** | **String** | URI to identify the account of the recipient/merchant. When PAN is the URI then recipient/merchant information is required. Pan, Manual Entry Alias and Alias are valid schemas. Valid Values- Refer &#39;Account URIs&#39; | 
**reconciliationData** | [**ReconciliationData35**](ReconciliationData35.md) |  | [optional] 
**routingTransitNumber** | **String** | The nine-digit Federal Reserve Routing and Transit (R &amp; T) number of the acquiring institution or the nine-digit pseudo-number assigned to the acquiring institution by Mastercard. If the partner is enrolled in multiple routing transit numbers, the routing transit number must be specified. If the partner is only enrolled in a single routing transit number then system takes the onboarded value. Please contact your MasterCard Representative to enable the usage of fields in this section. Details- Numeric, 9 | [optional] 
**sender** | [**Sender30**](Sender30.md) |  | [optional] 
**senderAccountUri** | **String** | URI to identify the account information of the sender. When PAN is the URI then sender information is required. If scheme chosen is raw, then funding_source must be other than CREDIT, DEBIT or PREPAID. Valid Values- Refer &#39;Account URIs&#39; | 
**tokenCryptogram** | [**TokenCryptogram39**](TokenCryptogram39.md) |  | [optional] 
**transactionLocalDateTime** | **String** | Local date and time when the transaction is submitted. Details-YYYY-MM-DDTHH:MM:SS±hh[:mm]  | 
**transferReference** | **String** | Provide a unique transaction reference number. It must be a unique value for the partner. Details- 6-40, Allowable characters are alphanumeric and * , - . _ ~ | 


