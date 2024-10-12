

# DocumentOrder

The order to send.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountingCost** | **String** | The buyer&#39;s accounting cost centre for this document. |  [optional] |
|**allowanceCharges** | [**List&lt;AllowanceCharge&gt;**](AllowanceCharge.md) | An array of allowance charges. |  [optional] |
|**amountIncludingTax** | **BigDecimal** | Total amount including Tax. |  |
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | An array of attachments. You may provide up to 10 attchments, but the total size must not exceed 10MB after Base64 encoding. |  [optional] |
|**delivery** | [**Delivery**](Delivery.md) |  |  [optional] |
|**deliveryTerms** | [**DeliveryTerms**](DeliveryTerms.md) |  |  [optional] |
|**documentCurrencyCode** | **CurrencyCode** |  |  [optional] |
|**documentNumber** | **String** | The number you assigned to the document. |  |
|**issueDate** | **String** | Format: yyyy-mm-dd. |  |
|**issueTime** | **String** | Format: hh:mm:ss±zzzz  |  [optional] |
|**note** | **String** | A note to add to the document |  [optional] |
|**orderLines** | [**List&lt;OrderLine&gt;**](OrderLine.md) | An array of order lines. |  |
|**orderType** | [**OrderTypeEnum**](#OrderTypeEnum) | The type of this order. |  [optional] |
|**paymentTerms** | [**PaymentTerms**](PaymentTerms.md) |  |  [optional] |
|**references** | [**List&lt;Reference&gt;**](Reference.md) | An array of references to other documents. Note that many syntaxes do not support multiple references of the same type in which case they will be concatenated with &#39;,&#39;. Also, not all syntaxes and doucments support all documentTypes. |  [optional] |
|**sellerSupplierParty** | [**SellerSupplierParty**](SellerSupplierParty.md) |  |  |
|**taxSystem** | [**TaxSystemEnum**](#TaxSystemEnum) | The tax system used for the invoice. The system &#39;tax_line_percentages&#39; is the only one currently supported. |  [optional] |
|**timeZone** | **String** | Format: ±zzzz, where ±zzzz is the difference from UTC, e.g. +0100 or -0900 etc. The timezone will also apply to the document issue date if this field is provided. |  [optional] |
|**validityPeriod** | **String** | The period (or specific date) to which the invoice applies. Format: yyyy-mm-dd - yyyy-mm-dd. |  [optional] |



## Enum: OrderTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;regular&quot; |
| CONSIGNMENT | &quot;consignment&quot; |



## Enum: TaxSystemEnum

| Name | Value |
|---- | -----|
| TAX_LINE_PERCENTAGES | &quot;tax_line_percentages&quot; |



