

# UpdateInvoiceArray


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
|**customervatNumber** | **String** | Customers VAT number |  |
|**date** | **String** | The date the invoice was issued |  [optional] |
|**discountRate** | **String** | The discount rate per item |  [optional] |
|**items** | [**List&lt;InvoiceItems&gt;**](InvoiceItems.md) | An array of your invoice items |  |
|**logoUrl** | **String** | A URL to your logo image. Must be SSL hosted. https://sslimagehost.com is recommended |  [optional] |
|**notes** | **String** | Add a note to the invoice. |  [optional] |
|**taxPoint** | **String** | (or &#39;time of supply&#39;) if this is different from the invoice date |  [optional] |
|**type** | **String** | The type of invoice. Either &#39;sale&#39; or &#39;refund&#39; |  |
|**vatNumber** | **String** | Your VAT number |  [optional] |



