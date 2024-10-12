# XeroAccountingApi.RepeatingInvoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**brandingThemeID** | **String** | See BrandingThemes | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if an invoice has an attachment | [optional] [readonly] [default to false]
**ID** | **String** | Xero generated unique identifier for repeating invoice template | [optional] 
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See LineItems | [optional] 
**reference** | **String** | ACCREC only – additional reference number | [optional] 
**repeatingInvoiceID** | **String** | Xero generated unique identifier for repeating invoice template | [optional] 
**schedule** | [**Schedule**](Schedule.md) |  | [optional] 
**status** | **String** | One of the following - DRAFT or AUTHORISED – See Invoice Status Codes | [optional] 
**subTotal** | **Number** | Total of invoice excluding taxes | [optional] 
**total** | **Number** | Total of Invoice tax inclusive (i.e. SubTotal + TotalTax) | [optional] 
**totalTax** | **Number** | Total tax on invoice | [optional] 
**type** | **String** | See Invoice Types | [optional] 



## Enum: StatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `AUTHORISED` (value: `"AUTHORISED"`)

* `DELETED` (value: `"DELETED"`)





## Enum: TypeEnum


* `ACCPAY` (value: `"ACCPAY"`)

* `ACCREC` (value: `"ACCREC"`)




