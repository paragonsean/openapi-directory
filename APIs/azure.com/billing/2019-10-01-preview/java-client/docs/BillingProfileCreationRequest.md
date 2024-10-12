

# BillingProfileCreationRequest

The request parameters for creating a new billing profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**AddressDetails**](AddressDetails.md) |  |  [optional] |
|**displayName** | **String** | The billing profile name. |  [optional] |
|**enabledAzurePlans** | [**List&lt;AzurePlan&gt;**](AzurePlan.md) | Enabled azure plans for this billing profile. |  [optional] |
|**invoiceEmailOptIn** | **Boolean** | If the billing profile is opted in to receive invoices via email. |  [optional] |
|**poNumber** | **String** | Purchase order number. |  [optional] |



