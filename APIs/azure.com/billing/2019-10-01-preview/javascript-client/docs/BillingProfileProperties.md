# BillingManagementClient.BillingProfileProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressDetails**](AddressDetails.md) |  | [optional] 
**currency** | **String** | The currency associated with the billing profile. | [optional] [readonly] 
**displayName** | **String** | The billing profile name. | [optional] 
**enabledAzurePlans** | [**[AzurePlan]**](AzurePlan.md) | Information about the enabled azure plans. | [optional] 
**invoiceDay** | **Number** | Invoice day. | [optional] [readonly] 
**invoiceEmailOptIn** | **Boolean** | If the billing profile is opted in to receive invoices via email. | [optional] 
**invoiceSections** | [**[InvoiceSection]**](InvoiceSection.md) | The invoice sections associated to the billing profile. | [optional] 
**poNumber** | **String** | Purchase order number. | [optional] 


