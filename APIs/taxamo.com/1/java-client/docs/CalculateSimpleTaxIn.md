

# CalculateSimpleTaxIn


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | Amount. Required if total amount or both unit price and quantity are not provided. |  [optional] |
|**billingCountryCode** | **String** | Billing two letter ISO country code. |  [optional] |
|**buyerCreditCardPrefix** | **String** | First 6 digits of buyer&#39;s credit card prefix. |  [optional] |
|**buyerTaxNumber** | **String** |  Buyer&#39;s tax number - EU VAT number for example. If using EU VAT number, it is possible to provide country code in it (e.g. IE1234567X) or simply use billing_country_code field for that. In the first case, if billing_country_code value was provided, it will be overwritten with country code value extracted from VAT number - but only if the VAT has been verified properly. |  [optional] |
|**currencyCode** | **String** | Currency code for transaction - e.g. EUR. |  |
|**forceCountryCode** | **String** | Two-letter ISO country code, e.g. FR. Use it to force country code for tax calculation. |  [optional] |
|**invoiceAddressCity** | **String** | Invoice address/postal_code |  [optional] |
|**invoiceAddressPostalCode** | **String** | Invoice address/postal_code |  [optional] |
|**invoiceAddressRegion** | **String** | Invoice address/region |  [optional] |
|**orderDate** | **String** | Order date in yyyy-MM-dd format, in merchant&#39;s timezone. If provided by the API caller, no timezone conversion is performed. Default value is current date and time. When using public token, the default value is used. |  [optional] |
|**productType** | **String** | Product type, according to dictionary /dictionaries/product_types.  |  [optional] |
|**quantity** | **BigDecimal** | Quantity Defaults to 1. |  [optional] |
|**taxDeducted** | **Boolean** | If the transaction is in a country supported by Taxamo, but the tax is not calculated due to merchant settings or EU B2B transaction for example. |  [optional] |
|**totalAmount** | **BigDecimal** | Total amount. Required if amount or both unit price and quantity are not provided. |  [optional] |
|**unitPrice** | **BigDecimal** | Unit price. |  [optional] |



