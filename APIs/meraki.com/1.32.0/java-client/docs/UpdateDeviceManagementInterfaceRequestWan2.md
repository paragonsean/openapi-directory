

# UpdateDeviceManagementInterfaceRequestWan2

WAN 2 settings (only for MX devices)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**staticDns** | **List&lt;String&gt;** | Up to two DNS IPs. |  [optional] |
|**staticGatewayIp** | **String** | The IP of the gateway on the WAN. |  [optional] |
|**staticIp** | **String** | The IP the device should use on the WAN. |  [optional] |
|**staticSubnetMask** | **String** | The subnet mask for the WAN. |  [optional] |
|**usingStaticIp** | **Boolean** | Configure the interface to have static IP settings or use DHCP. |  [optional] |
|**vlan** | **Integer** | The VLAN that management traffic should be tagged with. Applies whether usingStaticIp is true or false. |  [optional] |
|**wanEnabled** | [**WanEnabledEnum**](#WanEnabledEnum) | Enable or disable the interface (only for MX devices). Valid values are &#39;enabled&#39;, &#39;disabled&#39;, and &#39;not configured&#39;. |  [optional] |



## Enum: WanEnabledEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;disabled&quot; |
| ENABLED | &quot;enabled&quot; |
| NOT_CONFIGURED | &quot;not configured&quot; |



