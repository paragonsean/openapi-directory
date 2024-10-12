

# TransactionLines


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalCurrencies** | [**AdditionalCurrencies**](AdditionalCurrencies.md) |  |  [optional] |
|**amount** | **BigDecimal** | Amount. Required if total amount or both unit price and quantity are not provided. |  [optional] |
|**customFields** | [**List&lt;CustomFields&gt;**](CustomFields.md) | Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers. |  [optional] |
|**customId** | **String** | Custom id, provided by ecommerce software. |  |
|**deductedTaxAmount** | **BigDecimal** | Deducted tax amount, calculated by taxmo. |  [optional] |
|**deductedTaxRate** | **BigDecimal** | Deducted tax rate, calculated by taxamo. |  [optional] |
|**description** | **String** | Line contents description. |  [optional] |
|**id** | **BigDecimal** | Generated id. |  [optional] |
|**informative** | **Boolean** | If the line is provided for informative purposes. Such line must have :tax-rate and optionally :tax-name - if not, API validation will fail for this line. |  [optional] |
|**lineKey** | **String** | Generated line key. |  [optional] |
|**productCode** | **String** | Internal product code, used for invoicing for example. |  [optional] |
|**productTaxCode** | **String** | External product tax code for a line, for example TIC in US Sales tax. |  [optional] |
|**productType** | **String** | Product type, according to dictionary /dictionaries/product_types.  |  [optional] |
|**quantity** | **BigDecimal** | Quantity Defaults to 1. |  [optional] |
|**refundedTaxAmount** | **BigDecimal** | Refunded tax amount, calculated by taxmo. |  [optional] |
|**refundedTotalAmount** | **BigDecimal** | Refunded total amount, calculated by taxmo. |  [optional] |
|**supplyDate** | **String** | Date of supply in yyyy-MM-dd format. |  [optional] |
|**taxAmount** | **BigDecimal** | Tax amount, calculated by taxamo. |  [optional] |
|**taxName** | **String** | Tax name, calculated by taxamo.  Can be overwritten when informative field is true. |  [optional] |
|**taxRate** | **BigDecimal** | Tax rate, calculated by taxamo. Must be provided when informative field is true. |  [optional] |
|**totalAmount** | **BigDecimal** | Total amount. Required if amount or both unit price and quantity are not provided. |  [optional] |
|**unitOfMeasure** | **String** | Unit of measure. |  [optional] |
|**unitPrice** | **BigDecimal** | Unit price. |  [optional] |



