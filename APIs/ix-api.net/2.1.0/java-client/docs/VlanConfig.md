

# VlanConfig

The vlan configuration defines how the service is made available on the connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vlan** | **Integer** | A VLAN tag  |  |
|**vlanEthertype** | [**VlanEthertypeEnum**](#VlanEthertypeEnum) | The ethertype of the vlan in hexadecimal notation. |  [optional] |
|**vlanType** | **String** |  |  |
|**innerVlan** | **Integer** | The inner VLAN id.  |  |
|**outerVlan** | **Integer** | The outer VLAN id.  |  |
|**outerVlanEthertype** | [**OuterVlanEthertypeEnum**](#OuterVlanEthertypeEnum) | The ethertype of the outer tag in hexadecimal notation. |  [optional] |



## Enum: VlanEthertypeEnum

| Name | Value |
|---- | -----|
| _0X8100 | &quot;0x8100&quot; |
| _0X88A8 | &quot;0x88a8&quot; |
| _0X9100 | &quot;0x9100&quot; |



## Enum: OuterVlanEthertypeEnum

| Name | Value |
|---- | -----|
| _0X8100 | &quot;0x8100&quot; |
| _0X88A8 | &quot;0x88a8&quot; |
| _0X9100 | &quot;0x9100&quot; |



