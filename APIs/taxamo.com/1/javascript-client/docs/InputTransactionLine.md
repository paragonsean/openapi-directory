# Taxamo.InputTransactionLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Amount. Required if total amount or both unit price and quantity are not provided. | [optional] 
**customFields** | [**[CustomFields]**](CustomFields.md) | Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers. | [optional] 
**customId** | **String** | Custom id, provided by ecommerce software. | 
**deductedTaxRate** | **Number** | Deducted tax rate, calculated by taxamo. | [optional] 
**description** | **String** | Line contents description. | [optional] 
**informative** | **Boolean** | If the line is provided for informative purposes. Such line must have :tax-rate and optionally :tax-name - if not, API validation will fail for this line. | [optional] 
**lineKey** | **String** | Generated line key. | [optional] 
**productCode** | **String** | Internal product code, used for invoicing for example. | [optional] 
**productTaxCode** | **String** | External product tax code for a line, for example TIC in US Sales tax. | [optional] 
**productType** | **String** | Product type, according to dictionary /dictionaries/product_types.  | [optional] 
**quantity** | **Number** | Quantity Defaults to 1. | [optional] 
**supplyDate** | **String** | Date of supply in yyyy-MM-dd format. | [optional] 
**taxName** | **String** | Tax name, calculated by taxamo.  Can be overwritten when informative field is true. | [optional] 
**taxRate** | **Number** | Tax rate, calculated by taxamo. Must be provided when informative field is true. | [optional] 
**totalAmount** | **Number** | Total amount. Required if amount or both unit price and quantity are not provided. | [optional] 
**unitOfMeasure** | **String** | Unit of measure. | [optional] 
**unitPrice** | **Number** | Unit price. | [optional] 


