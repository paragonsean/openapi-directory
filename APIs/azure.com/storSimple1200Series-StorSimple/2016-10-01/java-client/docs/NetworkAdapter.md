

# NetworkAdapter

Represents a networkAdapter in a particular node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dhcpStatus** | [**DhcpStatusEnum**](#DhcpStatusEnum) | Represents state of DHCP. |  |
|**iPv4Info** | [**IPConfig**](IPConfig.md) |  |  [optional] |
|**iPv6Info** | [**IPConfig**](IPConfig.md) |  |  [optional] |
|**linkSpeed** | **Long** | The speed of the network adapter. |  [optional] |
|**networkAdapterName** | **String** | The name of the network adapter. |  |



## Enum: DhcpStatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



