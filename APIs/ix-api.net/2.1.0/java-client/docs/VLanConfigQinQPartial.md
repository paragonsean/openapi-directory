

# VLanConfigQinQPartial

A QinQ vlan configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**innerVlan** | **Integer** | The inner VLAN id.  |  [optional] |
|**outerVlan** | **Integer** | The outer VLAN id.  |  [optional] |
|**outerVlanEthertype** | [**OuterVlanEthertypeEnum**](#OuterVlanEthertypeEnum) | The ethertype of the outer tag in hexadecimal notation. |  [optional] |
|**vlanType** | **String** |  |  |



## Enum: OuterVlanEthertypeEnum

| Name | Value |
|---- | -----|
| _0X8100 | &quot;0x8100&quot; |
| _0X88A8 | &quot;0x88a8&quot; |
| _0X9100 | &quot;0x9100&quot; |



