

# Invoice

The invoice to send. Provide either invoice, or invoiceData, but not both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountingCost** | **String** | The buyer&#39;s accounting cost centre for this invoice, expressed as text. |  [optional] |
|**accountingCurrencyTaxAmount** | **BigDecimal** | The total amount of tax in the accounting currency. If included, must be non-zero. |  [optional] |
|**accountingCurrencyTaxAmountCurrency** | **CurrencyCode** |  |  [optional] |
|**accountingCustomerParty** | [**AccountingCustomerParty**](AccountingCustomerParty.md) |  |  |
|**accountingSupplierParty** | [**AccountingSupplierParty**](AccountingSupplierParty.md) |  |  [optional] |
|**allowanceCharges** | [**List&lt;AllowanceCharge&gt;**](AllowanceCharge.md) | An array of allowance charges. |  [optional] |
|**amountIncludingVat** | **BigDecimal** | amountIncludingVat is important because of rounding differences. In many invoices, the sum of the line item amounts excluding VAT and the VAT amounts is not equal to first summing the line items without VAT, and then applying VAT. The difference is automatically calculated and included in the electronic invoice, so the receiving accounting package can process the electronic invoice without problems. |  |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | An array of attachments. You may provide up to 10 attchments, but the total size must not exceed 10MB after Base64 encoding. |  [optional] |
|**billingReference** | **String** | DEPRECATED. Use a reference object with a documentType &#39;billing&#39;. A reference to a commercial invoice or corrective invoice of which the current invoice is a correction. This field is mandatory when sending invoiceType 384. |  [optional] |
|**buyerReference** | **String** | DEPRECATED. Use a reference object with a documentType &#39;buyer_reference&#39;. A reference provided by the buyer used for internal routing of the document. |  [optional] |
|**consumerTaxMode** | **Boolean** | Whether or not to process the invoice in consumer tax mode. In this mode, the VAT identifier of the sender will not be the default VAT identifier, but the one that matches with the country of the receiving consumer, if that additional VAT identifier for that country is available. These additional VAT identifiers need to be added to the sending LegalEntity by Storecove, so if you need to send invoices in this mode, please contact us. |  [optional] |
|**contractDocumentReference** | **String** | DEPRECATED. Use a reference object with a documentType &#39;contract&#39;. A reference to a contract or framework agreement that this invoice relates to. |  [optional] |
|**delivery** | [**Delivery**](Delivery.md) |  |  [optional] |
|**documentCurrencyCode** | **CurrencyCode** |  |  [optional] |
|**dueDate** | **String** | Format: yyyy-mm-dd. |  [optional] |
|**invoiceLines** | [**List&lt;InvoiceLine&gt;**](InvoiceLine.md) | An array of invoice lines. |  |
|**invoiceNumber** | **String** | The invoice number you assigned to the invoice. The invoiceNumber should be unique for the legalEntityId and year of the issueDate. This means invoice numbers can be reused in different years, as is customary in some countries. |  |
|**invoicePeriod** | **String** | The period (or specific date) to which the invoice applies. Format: yyyy-mm-dd - yyyy-mm-dd. |  [optional] |
|**invoiceType** | [**InvoiceTypeEnum**](#InvoiceTypeEnum) | DEPRECATED. Do not use. This field is available for legacy reasons only. If you want to send a regular invoice (aka UBL type &#39;380&#39;), make sure you have a positive invoice amount. For a credit note (aka UBL type &#39;381&#39;), simply provide a negative invoice amount. If you, in addition to a negative invoice amount, also specify a billingReferences, your invoice will become a corrective invoice (aka UBL type &#39;384&#39;). If your invoice is not sent in the UBL syntax, Storecove will provide the appropriate type for the syntax the invoice is sent in. |  [optional] |
|**issueDate** | **String** | Format: yyyy-mm-dd. |  |
|**issueReasons** | **List&lt;String&gt;** | An array reasons for issuing the invoice. |  [optional] |
|**note** | **String** | A note to add to the invoice |  [optional] |
|**orderReference** | **String** | DEPRECATED. Use a reference object with a documentType &#39;purchase_order&#39;. A reference to an order for this invoice, assigned by the buyer. Note that this often is a key field, since many receivers of invoices will use this field to automatically match the invoice to an order they placed. Many receivers refuse invoices that cannot be automatically matched, in particular government agencies. So it is highly recommended to fill this field whenever possible. |  [optional] |
|**paymentMeansArray** | [**List&lt;PaymentMeans&gt;**](PaymentMeans.md) | An array of payment means (ways to pay the invoice). |  [optional] |
|**paymentMeansBic** | **String** | DEPRECATED. Use paymentMeansArray. The BIC (Swift) of the bank where the amount payable should be transferred to |  [optional] |
|**paymentMeansCode** | [**PaymentMeansCodeEnum**](#PaymentMeansCodeEnum) | DEPRECATED. Use paymentMeansArray. How the invoice has been / will be paid. Use only online_payment_service (payment will be made or has been made by an online payment service), bank_card (e.g. debit card, credit card), direct_debit (the amount has been / will be taken out of the client&#39;s bank account), standing_agreement (an unspecified payment means known to both buyer and seller) or credit_transfer (the buyer will do / has done a bank transfer). The numeric codes are for legacy purposes, they should not be used. |  [optional] |
|**paymentMeansIban** | **String** | DEPRECATED. Use paymentMeansArray. The IBAN the amount payable should be transferred to |  [optional] |
|**paymentMeansPaymentId** | **String** | DEPRECATED. Use the paymentId in the individual PaymentMeans object. The payment id that you will use to match the payment against the invoice. |  [optional] |
|**paymentTerms** | [**PaymentTerms**](PaymentTerms.md) |  |  [optional] |
|**preferredInvoiceType** | [**PreferredInvoiceTypeEnum**](#PreferredInvoiceTypeEnum) | In auto mode, the choice between invoice or creditnote is made by Storecove based on what is appropriate for the receiver and the receiver country, in combination with the invoice amount sign. If you wish to state a preference, use this field. It is not guaranteed that the preference will be used, since it depends also on the receiver&#39;s document capabilities. |  [optional] |
|**prepaidAmount** | **BigDecimal** | The amount already paid. |  [optional] |
|**priceMode** | [**PriceModeEnum**](#PriceModeEnum) | The price mode. This is used to determine whether the prices are net or gross. Price Mode &#39;price_mode_gross&#39; can only be used for \&quot;x2y\&quot;: \&quot;b2c\&quot;, sender countries ES, IT and PT, \&quot;clearWithoutSending\&quot;: true and \&quot;taxSystem\&quot;: \&quot;tax_line_percentages\&quot; |  [optional] |
|**projectReference** | **String** | DEPRECATED. Information about the project this invoice relates to. |  [optional] |
|**references** | [**List&lt;Reference&gt;**](Reference.md) | An array of references to other documents. Note that many syntaxes do not support multiple references of the same type in which case they will be concatenated with &#39;,&#39;. Also, not all syntaxes support all documentTypes. |  [optional] |
|**salesOrderId** | **String** | DEPRECATED. Use a reference object with a documentType &#39;sales_order&#39;. A reference to an order for this invoice, assigned by the seller. |  [optional] |
|**selfBillingMode** | **Boolean** | In self billing mode, the AccountingCustomerParty and the AccountingSupplierParty are be switched. Such an invoice can only be sent via email. Also, your account will need to allow the use of this mode, so before trying to use this please first contact Storecove. |  [optional] |
|**taxExemptReason** | [**TaxExemptReasonEnum**](#TaxExemptReasonEnum) | DEPRECATED. Use Tax/category and specify this per invoice line. If you do specify this field, it will be applied to all invoice lines and it is an error to specify a Tax/category at the invoice line level. This field holds the reason no tax is present in the invoice. Note that this is an invoice level field and you cannot specify it per invoice line. This field is mandatory unless tax is present in the invoice. |  [optional] |
|**taxPointDate** | **String** | The tax date is the date on which the supply of goods or of services was made or completed or the date on which the payment on account was made insofar as that date can be determined and differs from the date of the issue of the invoice. EU 2006-112 Article 226 Point 7. Note: For the Dutch TAX authorities the tac date should be the same as the issue date. |  [optional] |
|**taxSubtotals** | [**List&lt;TaxSubtotal&gt;**](TaxSubtotal.md) | An array of tax subtotals. This element is mandatory for taxSystem &#39;tax_line_percentages&#39;. |  [optional] |
|**taxSystem** | [**TaxSystemEnum**](#TaxSystemEnum) | The tax system used for the invoice. The system &#39;tax_line_percentages&#39; is preferred, but for historic purposes &#39;tax_line_amounts&#39; is supported and the default. Since not all invoice formats that we are required to send support &#39;tax_line_amounts&#39; we will need to convert the invoice to the &#39;tax_line_percentags&#39; system if we are forced to send the invoice in that tax system. Note that an invoice must always contain tax information, even if that is 0% or an item or sender is exempt or tax is completely outside scope. In that case, use the correct tax categories (see &lt;&lt;_openapi_tax&gt;&gt;) |  [optional] |
|**taxesDutiesFees** | [**List&lt;Tax&gt;**](Tax.md) | An array of taxes, duties and fees for this invoice. At this moment, the only invoice level tax allowed is the Italian &#39;€2 bollo virtuale&#39; |  [optional] |
|**transactionType** | [**TransactionTypeEnum**](#TransactionTypeEnum) | The type of transaction. Currently used only for India. |  [optional] |
|**ublExtensions** | **List&lt;String&gt;** | An array of ubl extensions. |  [optional] |
|**vatReverseCharge** | **Boolean** | DEPRECATED. Use taxExemptReason. |  [optional] |
|**x2y** | [**X2yEnum**](#X2yEnum) | The type of entities the document is sent from/to: b2b (business-to-business), b2g (business-to-government) or b2c (business-to-consumer). This field does not have a default, but it in mose cases it will be treated as b2b. Only when you explicitly specify b2g or b2c OR when it is clear from the context will a different value be used. For instance, when we see the document is being routed to DE:LWID or NL:OINO number, this tells us it is b2g. But in many cases we are unable to determine this and so it is best to always specify this field. Note that b2b_sez is for use inside India only. |  [optional] |



## Enum: InvoiceTypeEnum

| Name | Value |
|---- | -----|
| _380 | &quot;380&quot; |
| _381 | &quot;381&quot; |
| _384 | &quot;384&quot; |



## Enum: PaymentMeansCodeEnum

| Name | Value |
|---- | -----|
| ONLINE_PAYMENT_SERVICE | &quot;online_payment_service&quot; |
| BANK_CARD | &quot;bank_card&quot; |
| DIRECT_DEBIT | &quot;direct_debit&quot; |
| STANDING_AGREEMENT | &quot;standing_agreement&quot; |
| CREDIT_TRANSFER | &quot;credit_transfer&quot; |
| SE_BANKGIRO | &quot;se_bankgiro&quot; |
| SE_PLUSGIRO | &quot;se_plusgiro&quot; |
| AUNZ_NPP | &quot;aunz_npp&quot; |
| EMPTY | &quot;&quot; |
| _1 | &quot;1&quot; |
| _30 | &quot;30&quot; |
| _31 | &quot;31&quot; |
| _42 | &quot;42&quot; |
| _48 | &quot;48&quot; |
| _49 | &quot;49&quot; |
| _57 | &quot;57&quot; |
| _58 | &quot;58&quot; |



## Enum: PreferredInvoiceTypeEnum

| Name | Value |
|---- | -----|
| AUTODETECT | &quot;prefer_autodetect&quot; |
| INVOICE | &quot;prefer_invoice&quot; |
| CREDITNOTE | &quot;prefer_creditnote&quot; |



## Enum: PriceModeEnum

| Name | Value |
|---- | -----|
| NET | &quot;price_mode_net&quot; |
| GROSS | &quot;price_mode_gross&quot; |



## Enum: TaxExemptReasonEnum

| Name | Value |
|---- | -----|
| EXPORT | &quot;export&quot; |
| REVERSE_CHARGE | &quot;reverse_charge&quot; |
| ZERO_RATED | &quot;zero_rated&quot; |
| EXEMPT | &quot;exempt&quot; |
| OUTSIDE_SCOPE | &quot;outside_scope&quot; |
| INTRA_COMMUNITY | &quot;intra_community&quot; |



## Enum: TaxSystemEnum

| Name | Value |
|---- | -----|
| AMOUNTS | &quot;tax_line_amounts&quot; |
| PERCENTAGES | &quot;tax_line_percentages&quot; |



## Enum: TransactionTypeEnum

| Name | Value |
|---- | -----|
| B2B | &quot;b2b&quot; |
| SEZWP | &quot;sezwp&quot; |
| SEZWOP | &quot;sezwop&quot; |
| EXPWP | &quot;expwp&quot; |
| EXPWOP | &quot;expwop&quot; |
| DEXP | &quot;dexp&quot; |



## Enum: X2yEnum

| Name | Value |
|---- | -----|
| B2B | &quot;b2b&quot; |
| B2G | &quot;b2g&quot; |
| B2C | &quot;b2c&quot; |
| B2B_SEZ | &quot;b2b_sez&quot; |



