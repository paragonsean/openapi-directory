# NetworkManagementClient.ApplicationGatewayFrontendIPConfigurationPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privateIPAddress** | **String** | PrivateIPAddress of the network interface IP Configuration. | [optional] 
**privateIPAllocationMethod** | **String** | PrivateIP allocation method. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. | [optional] 
**provisioningState** | **String** | Provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIPAddress** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  | [optional] 
**subnet** | [**ApplicationGatewayHttpListenerPropertiesFormatFrontendPort**](ApplicationGatewayHttpListenerPropertiesFormatFrontendPort.md) |  | [optional] 



## Enum: PrivateIPAllocationMethodEnum


* `Static` (value: `"Static"`)

* `Dynamic` (value: `"Dynamic"`)




