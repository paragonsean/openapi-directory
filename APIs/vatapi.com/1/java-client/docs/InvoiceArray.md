

# InvoiceArray


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**businessAddress** | **String** | Your business address |  |
|**businessName** | **String** | Your business name |  |
|**conversionRate** | **Integer** | The rate of conversion at time of supply |  [optional] |
|**currencyCode** | **String** | 3 character currency code for invoice |  |
|**currencyCodeConversion** | **String** | 3 character currency code to be converted from original transaction currency |  [optional] |
|**customerAddress** | **String** | Your customers address |  [optional] |
|**customerName** | **String** | Your customers name or trading name |  [optional] |
|**customerVatNumber** | **String** | Customers VAT number |  [optional] |
|**date** | **String** | The date the invoice was issued |  |
|**discountRate** | **Integer** | The discount rate per item |  [optional] |
|**discountTotal** | **Integer** | Total amount of discount |  |
|**invoiceNumber** | **Integer** | A sequential invoice number |  |
|**invoiceUrl** | **String** | A perminant URL to your VAT invoice |  |
|**items** | [**List&lt;InvoiceItems&gt;**](InvoiceItems.md) | An array of your invoice items |  |
|**logoUrl** | **String** | A URL to your logo image. Must be SSL hosted. https://sslimagehost.com is recommended |  [optional] |
|**notes** | **String** | Any notes attached to the invoice |  [optional] |
|**subtotal** | **Integer** | Total amount excluding VAT |  |
|**taxPoint** | **String** | (or &#39;time of supply&#39;) if this is different from the invoice date |  |
|**total** | **Integer** | Total amount of including VAT |  |
|**type** | **String** | The type of invoice. Either &#39;sale&#39; or &#39;refund&#39; |  |
|**vatNumber** | **String** | Your VAT number |  |
|**vatTotal** | **Integer** | Total amount of VAT |  |



