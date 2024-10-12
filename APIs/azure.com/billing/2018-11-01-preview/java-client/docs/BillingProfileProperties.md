

# BillingProfileProperties

The properties of the billing profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**currency** | **String** | The currency associated with the billing profile. |  [optional] [readonly] |
|**displayName** | **String** | The billing profile name. |  [optional] |
|**enabledAzureSKUs** | [**List&lt;EnabledAzureSKUs&gt;**](EnabledAzureSKUs.md) | Information about the product. |  [optional] |
|**invoiceDay** | **Integer** | Invoice day. |  [optional] [readonly] |
|**invoiceEmailOptIn** | **Boolean** | If the billing profile is opted in to receive invoices via email. |  [optional] [readonly] |
|**invoiceSections** | [**List&lt;InvoiceSection&gt;**](InvoiceSection.md) | The invoice sections associated to the billing profile. |  [optional] |
|**isClassic** | **Boolean** | Is OMS bootstrapped billing profile. |  [optional] [readonly] |
|**poNumber** | **String** | Purchase order number. |  [optional] |



