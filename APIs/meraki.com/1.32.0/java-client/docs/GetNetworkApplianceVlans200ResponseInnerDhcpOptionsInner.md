

# GetNetworkApplianceVlans200ResponseInnerDhcpOptionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The code for the DHCP option. This should be an integer between 2 and 254. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type for the DHCP option. One of: &#39;text&#39;, &#39;ip&#39;, &#39;hex&#39; or &#39;integer&#39; |  |
|**value** | **String** | The value for the DHCP option |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEX | &quot;hex&quot; |
| INTEGER | &quot;integer&quot; |
| IP | &quot;ip&quot; |
| TEXT | &quot;text&quot; |



