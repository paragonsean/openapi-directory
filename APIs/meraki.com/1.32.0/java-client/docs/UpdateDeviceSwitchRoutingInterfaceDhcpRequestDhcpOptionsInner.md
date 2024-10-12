

# UpdateDeviceSwitchRoutingInterfaceDhcpRequestDhcpOptionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The code for DHCP option which should be from 2 to 254 |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the DHCP option which should be one of (&#39;text&#39;, &#39;ip&#39;, &#39;integer&#39; or &#39;hex&#39;) |  |
|**value** | **String** | The value of the DHCP option |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEX | &quot;hex&quot; |
| INTEGER | &quot;integer&quot; |
| IP | &quot;ip&quot; |
| TEXT | &quot;text&quot; |



