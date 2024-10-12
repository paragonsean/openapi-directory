# CustomerInsightsManagementClient.HubPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiEndpoint** | **String** | API endpoint URL of the hub. | [optional] [readonly] 
**hubBillingInfo** | [**HubBillingInfoFormat**](HubBillingInfoFormat.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state of the hub. | [optional] [readonly] 
**tenantFeatures** | **Number** | The bit flags for enabled hub features. Bit 0 is set to 1 indicates graph is enabled, or disabled if set to 0. Bit 1 is set to 1 indicates the hub is disabled, or enabled if set to 0. | [optional] 
**webEndpoint** | **String** | Web endpoint URL of the hub. | [optional] [readonly] 


