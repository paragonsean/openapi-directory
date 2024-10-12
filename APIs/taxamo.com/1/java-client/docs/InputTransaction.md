

# InputTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalCurrencies** | [**AdditionalCurrencies**](AdditionalCurrencies.md) |  |  [optional] |
|**billingCountryCode** | **String** | Billing two letter ISO country code. |  [optional] |
|**buyerCreditCardPrefix** | **String** | First 6 digits of buyer&#39;s credit card prefix. |  [optional] |
|**buyerEmail** | **String** | Buyer&#39;s declared email address. |  [optional] |
|**buyerIp** | **String** | IP address of the buyer in dotted decimal (IPv4) or text format (IPv6). |  [optional] |
|**buyerName** | **String** | Buyer&#39;s name - first name and last name or company name. |  [optional] |
|**buyerTaxNumber** | **String** |  Buyer&#39;s tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly. |  [optional] |
|**comments** | **String** | Additional information about the transaction - for example if the evidence has been amended. |  [optional] |
|**currencyCode** | **String** | Currency code for transaction - e.g. EUR. |  |
|**customData** | **String** | Custom data related to transaction. |  [optional] |
|**customFields** | [**List&lt;CustomFields&gt;**](CustomFields.md) | Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers. |  [optional] |
|**customId** | **String** | Custom identifier provided upon transaction creation. |  [optional] |
|**customerId** | **String** | Free-form field for storing customer id. |  [optional] |
|**description** | **String** | Transaction description. |  [optional] |
|**evidence** | [**Evidence**](Evidence.md) |  |  [optional] |
|**forceCountryCode** | **String** | Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation. |  [optional] |
|**invoiceAddress** | [**InvoiceAddress**](InvoiceAddress.md) |  |  [optional] |
|**invoiceDate** | **String** | Invoice date of issue. |  [optional] |
|**invoiceNumber** | **String** | Invoice number. |  [optional] |
|**invoicePlace** | **String** | Invoice place of issue. |  [optional] |
|**note** | **String** | Additional note related to transaction state - for example if the transaction was created in a &#39;catch-all&#39; mode or the VAT number re-check for subscriptions has failed. |  [optional] |
|**orderDate** | **String** | Order date in yyyy-MM-dd format, in merchant&#39;s timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used. |  [optional] |
|**originalTransactionKey** | **String** | Use data and evidence from original transaction. Tax will be re-calculated, but evidence won&#39;t be re-checked. This parameter is taken into account only when &#39;manual&#39; flag is raised. |  [optional] |
|**status** | **String** | Transaction status: &#39;N&#39; - new, &#39;C&#39; - confirmed. Can use &#39;C&#39; in store-transaction! with private-token to create confirmed transaction, otherwise &#39;N&#39; is default status. Not applicable for update-transaction!. |  [optional] |
|**subAccountId** | **String** | Sub account identifier. |  [optional] |
|**supplyDate** | **String** | Supply date in yyyy-MM-dd format. |  [optional] |
|**taxCountryCode** | **String** | Two-letter ISO country code, e.g. FR. This code applies to detected/set country for transaction, but can be set using manual mode. |  [optional] |
|**taxData** | [**TaxDataSchema**](TaxDataSchema.md) |  |  [optional] |
|**taxDeducted** | **Boolean** | True if the transaction is deducted from tax and no tax is applied (it is untaxed). Either set automatically when VAT number validates with VIES correctly, but can also be provided in manual mode. |  [optional] |
|**transactionLines** | [**List&lt;InputTransactionLine&gt;**](InputTransactionLine.md) | Transaction lines. |  |
|**verificationToken** | **String** | Verification token |  [optional] |



