# MerakiDashboardApi.UpdateDeviceManagementInterfaceRequestWan2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**staticDns** | **[String]** | Up to two DNS IPs. | [optional] 
**staticGatewayIp** | **String** | The IP of the gateway on the WAN. | [optional] 
**staticIp** | **String** | The IP the device should use on the WAN. | [optional] 
**staticSubnetMask** | **String** | The subnet mask for the WAN. | [optional] 
**usingStaticIp** | **Boolean** | Configure the interface to have static IP settings or use DHCP. | [optional] 
**vlan** | **Number** | The VLAN that management traffic should be tagged with. Applies whether usingStaticIp is true or false. | [optional] 
**wanEnabled** | **String** | Enable or disable the interface (only for MX devices). Valid values are &#39;enabled&#39;, &#39;disabled&#39;, and &#39;not configured&#39;. | [optional] 



## Enum: WanEnabledEnum


* `disabled` (value: `"disabled"`)

* `enabled` (value: `"enabled"`)

* `not configured` (value: `"not configured"`)




