# BillingManagementClient.BillingProfileProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**currency** | **String** | The currency associated with the billing profile. | [optional] [readonly] 
**displayName** | **String** | The billing profile name. | [optional] 
**enabledAzureSKUs** | [**[EnabledAzureSKUs]**](EnabledAzureSKUs.md) | Information about the product. | [optional] 
**invoiceDay** | **Number** | Invoice day. | [optional] [readonly] 
**invoiceEmailOptIn** | **Boolean** | If the billing profile is opted in to receive invoices via email. | [optional] [readonly] 
**invoiceSections** | [**[InvoiceSection]**](InvoiceSection.md) | The invoice sections associated to the billing profile. | [optional] 
**isClassic** | **Boolean** | Is OMS bootstrapped billing profile. | [optional] [readonly] 
**poNumber** | **String** | Purchase order number. | [optional] 


