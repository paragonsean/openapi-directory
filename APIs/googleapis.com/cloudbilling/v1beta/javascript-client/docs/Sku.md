# CloudBillingApi.Sku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The display name for the SKU. Example: A2 Instance Core running in Americas | [optional] 
**prices** | [**[Price]**](Price.md) | A timeline of prices for a SKU in chronological order. Note: The API currently only supports using a constant price for the entire estimation time frame so this list will contain a single value. | [optional] 
**sku** | **String** | The resource name for the SKU. Example: \&quot;services/DA34-426B-A397/skus/AA95-CD31-42FE\&quot; | [optional] 


