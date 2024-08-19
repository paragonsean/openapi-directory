# XeroAccountingApi.LineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCode** | **String** | See Accounts | [optional] 
**description** | **String** | Description needs to be at least 1 char long. A line item with just a description (i.e no unit amount or quantity) can be created by specifying just a &lt;Description&gt; element that contains at least 1 character | [optional] 
**discountAmount** | **Number** | Discount amount being applied to a line item. Only supported on ACCREC invoices - ACCPAY invoices and credit notes in Xero do not support discounts. | [optional] 
**discountRate** | **Number** | Percentage discount being applied to a line item (only supported on  ACCREC invoices – ACC PAY invoices and credit notes in Xero do not support discounts | [optional] 
**itemCode** | **String** | See Items | [optional] 
**lineAmount** | **Number** | If you wish to omit either of the &lt;Quantity&gt; or &lt;UnitAmount&gt; you can provide a LineAmount and Xero will calculate the missing amount for you. The line amount reflects the discounted price if a DiscountRate has been used . i.e LineAmount &#x3D; Quantity * Unit Amount * ((100 – DiscountRate)/100) | [optional] 
**lineItemID** | **String** | LineItem unique ID | [optional] 
**quantity** | **Number** | LineItem Quantity | [optional] 
**repeatingInvoiceID** | **String** | The Xero identifier for a Repeating Invoice | [optional] 
**taxAmount** | **Number** | The tax amount is auto calculated as a percentage of the line amount (see below) based on the tax rate. This value can be overriden if the calculated &lt;TaxAmount&gt; is not correct. | [optional] 
**taxType** | **String** | The tax type from TaxRates | [optional] 
**tracking** | [**[LineItemTracking]**](LineItemTracking.md) | Optional Tracking Category – see Tracking.  Any LineItem can have a  maximum of 2 &lt;TrackingCategory&gt; elements. | [optional] 
**unitAmount** | **Number** | LineItem Unit Amount | [optional] 


