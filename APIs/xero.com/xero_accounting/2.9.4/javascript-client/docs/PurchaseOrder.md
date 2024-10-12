# XeroAccountingApi.PurchaseOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[Attachment]**](Attachment.md) | Displays array of attachments from the API | [optional] 
**attentionTo** | **String** | The person that the delivery is going to | [optional] 
**brandingThemeID** | **String** | See BrandingThemes | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**currencyCode** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**currencyRate** | **Number** | The currency rate for a multicurrency purchase order. If no rate is specified, the XE.com day rate is used. | [optional] 
**date** | **String** | Date purchase order was issued – YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation | [optional] 
**deliveryAddress** | **String** | The address the goods are to be delivered to | [optional] 
**deliveryDate** | **String** | Date the goods are to be delivered – YYYY-MM-DD | [optional] 
**deliveryInstructions** | **String** | A free text feild for instructions (500 characters max) | [optional] 
**expectedArrivalDate** | **String** | The date the goods are expected to arrive. | [optional] 
**hasAttachments** | **Boolean** | boolean to indicate if a purchase order has an attachment | [optional] [readonly] [default to false]
**lineAmountTypes** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | See LineItems | [optional] 
**purchaseOrderID** | **String** | Xero generated unique identifier for purchase order | [optional] 
**purchaseOrderNumber** | **String** | Unique alpha numeric code identifying purchase order (when missing will auto-generate from your Organisation Invoice Settings) | [optional] 
**reference** | **String** | Additional reference number | [optional] 
**sentToContact** | **Boolean** | Boolean to set whether the purchase order should be marked as “sent”. This can be set only on purchase orders that have been approved or billed | [optional] 
**status** | **String** | See Purchase Order Status Codes | [optional] 
**statusAttributeString** | **String** | A string to indicate if a invoice status | [optional] 
**subTotal** | **Number** | Total of purchase order excluding taxes | [optional] [readonly] 
**telephone** | **String** | The phone number for the person accepting the delivery | [optional] 
**total** | **Number** | Total of Purchase Order tax inclusive (i.e. SubTotal + TotalTax) | [optional] [readonly] 
**totalDiscount** | **Number** | Total of discounts applied on the purchase order line items | [optional] [readonly] 
**totalTax** | **Number** | Total tax on purchase order | [optional] [readonly] 
**updatedDateUTC** | **String** | Last modified date UTC format | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**warnings** | [**[ValidationError]**](ValidationError.md) | Displays array of warning messages from the API | [optional] 



## Enum: StatusEnum


* `DRAFT` (value: `"DRAFT"`)

* `SUBMITTED` (value: `"SUBMITTED"`)

* `AUTHORISED` (value: `"AUTHORISED"`)

* `BILLED` (value: `"BILLED"`)

* `DELETED` (value: `"DELETED"`)




