

# CreateAnAchTransferParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The Increase identifier for the account that will send the transfer. |  |
|**accountNumber** | **String** | The account number for the destination account. |  [optional] |
|**addendum** | **String** | Additional information that will be sent to the recipient. This is included in the transfer data sent to the receiving bank. |  [optional] |
|**amount** | **Integer** | The transfer amount in cents. A positive amount originates a credit transfer pushing funds to the receiving account. A negative amount originates a debit transfer pulling funds from the receiving account. |  |
|**companyDescriptiveDate** | **String** | The description of the date of the transfer, usually in the format &#x60;YYMMDD&#x60;. This is included in the transfer data sent to the receiving bank. |  [optional] |
|**companyDiscretionaryData** | **String** | The data you choose to associate with the transfer. This is included in the transfer data sent to the receiving bank. |  [optional] |
|**companyEntryDescription** | **String** | A description of the transfer. This is included in the transfer data sent to the receiving bank. |  [optional] |
|**companyName** | **String** | The name by which the recipient knows you. This is included in the transfer data sent to the receiving bank. |  [optional] |
|**effectiveDate** | **LocalDate** | The transfer effective date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**externalAccountId** | **String** | The ID of an External Account to initiate a transfer to. If this parameter is provided, &#x60;account_number&#x60;, &#x60;routing_number&#x60;, and &#x60;funding&#x60; must be absent. |  [optional] |
|**funding** | [**FundingEnum**](#FundingEnum) | The type of the account to which the transfer will be sent. |  [optional] |
|**individualId** | **String** | Your identifer for the transfer recipient. |  [optional] |
|**individualName** | **String** | The name of the transfer recipient. This value is informational and not verified by the recipient&#39;s bank. |  [optional] |
|**requireApproval** | **Boolean** | Whether the transfer requires explicit approval via the dashboard or API. |  [optional] |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN) for the destination account. |  [optional] |
|**standardEntryClassCode** | [**StandardEntryClassCodeEnum**](#StandardEntryClassCodeEnum) | The Standard Entry Class (SEC) code to use for the transfer. |  [optional] |
|**statementDescriptor** | **String** | A description you choose to give the transfer. This will be saved with the transfer details, displayed in the dashboard, and returned by the API. If &#x60;individual_name&#x60; and &#x60;company_name&#x60; are not explicitly set by this API, the &#x60;statement_descriptor&#x60; will be sent in those fields to the receiving bank to help the customer recognize the transfer. You are highly encouraged to pass &#x60;individual_name&#x60; and &#x60;company_name&#x60; instead of relying on this fallback. |  |



## Enum: FundingEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |



## Enum: StandardEntryClassCodeEnum

| Name | Value |
|---- | -----|
| CORPORATE_CREDIT_OR_DEBIT | &quot;corporate_credit_or_debit&quot; |
| PREARRANGED_PAYMENTS_AND_DEPOSIT | &quot;prearranged_payments_and_deposit&quot; |
| INTERNET_INITIATED | &quot;internet_initiated&quot; |



