

# InvoiceData


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
|**customerVatNumber** | **String** | Optional customers VAT number |  [optional] |
|**date** | **String** | The date the invoice was issued |  [optional] |
|**discountRate** | **String** | The discount rate per item |  [optional] |
|**items** | [**List&lt;InvoiceItems&gt;**](InvoiceItems.md) | An array of your invoice items |  |
|**notes** | **String** | Add a note to the invoice. |  [optional] |
|**priceType** | **String** | Optional, if the price is including VAT set the type to &#39;incl&#39;. Otherwise the default is assumed as excluding VAT already, &#39;excl&#39; |  [optional] |
|**taxPoint** | **String** | (or &#39;time of supply&#39;) if this is different from the invoice date |  [optional] |
|**type** | **String** | The type of invoice. Either &#39;sale&#39; or &#39;refund&#39; |  |
|**vatNumber** | **String** | Your VAT number |  |
|**zeroRated** | **String** | To Zero-Rate the VAT, set to true. |  [optional] |



