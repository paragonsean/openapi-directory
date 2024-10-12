

# WritableVirtualMachineInterface


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**macAddress** | **String** |  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) |  |  [optional] |
|**mtu** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**taggedVlans** | **Set&lt;Integer&gt;** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**untaggedVlan** | **Integer** |  |  [optional] |
|**virtualMachine** | **Integer** |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| ACCESS | &quot;access&quot; |
| TAGGED | &quot;tagged&quot; |
| TAGGED_ALL | &quot;tagged-all&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VIRTUAL | &quot;virtual&quot; |
| LAG | &quot;lag&quot; |
| _100BASE_TX | &quot;100base-tx&quot; |
| _1000BASE_T | &quot;1000base-t&quot; |
| _2_5GBASE_T | &quot;2.5gbase-t&quot; |
| _5GBASE_T | &quot;5gbase-t&quot; |
| _10GBASE_T | &quot;10gbase-t&quot; |
| _10GBASE_CX4 | &quot;10gbase-cx4&quot; |
| _1000BASE_X_GBIC | &quot;1000base-x-gbic&quot; |
| _1000BASE_X_SFP | &quot;1000base-x-sfp&quot; |
| _10GBASE_X_SFPP | &quot;10gbase-x-sfpp&quot; |
| _10GBASE_X_XFP | &quot;10gbase-x-xfp&quot; |
| _10GBASE_X_XENPAK | &quot;10gbase-x-xenpak&quot; |
| _10GBASE_X_X2 | &quot;10gbase-x-x2&quot; |
| _25GBASE_X_SFP28 | &quot;25gbase-x-sfp28&quot; |
| _40GBASE_X_QSFPP | &quot;40gbase-x-qsfpp&quot; |
| _50GBASE_X_SFP28 | &quot;50gbase-x-sfp28&quot; |
| _100GBASE_X_CFP | &quot;100gbase-x-cfp&quot; |
| _100GBASE_X_CFP2 | &quot;100gbase-x-cfp2&quot; |
| _200GBASE_X_CFP2 | &quot;200gbase-x-cfp2&quot; |
| _100GBASE_X_CFP4 | &quot;100gbase-x-cfp4&quot; |
| _100GBASE_X_CPAK | &quot;100gbase-x-cpak&quot; |
| _100GBASE_X_QSFP28 | &quot;100gbase-x-qsfp28&quot; |
| _200GBASE_X_QSFP56 | &quot;200gbase-x-qsfp56&quot; |
| _400GBASE_X_QSFPDD | &quot;400gbase-x-qsfpdd&quot; |
| _400GBASE_X_OSFP | &quot;400gbase-x-osfp&quot; |
| IEEE802_11A | &quot;ieee802.11a&quot; |
| IEEE802_11G | &quot;ieee802.11g&quot; |
| IEEE802_11N | &quot;ieee802.11n&quot; |
| IEEE802_11AC | &quot;ieee802.11ac&quot; |
| IEEE802_11AD | &quot;ieee802.11ad&quot; |
| IEEE802_11AX | &quot;ieee802.11ax&quot; |
| GSM | &quot;gsm&quot; |
| CDMA | &quot;cdma&quot; |
| LTE | &quot;lte&quot; |
| SONET_OC3 | &quot;sonet-oc3&quot; |
| SONET_OC12 | &quot;sonet-oc12&quot; |
| SONET_OC48 | &quot;sonet-oc48&quot; |
| SONET_OC192 | &quot;sonet-oc192&quot; |
| SONET_OC768 | &quot;sonet-oc768&quot; |
| SONET_OC1920 | &quot;sonet-oc1920&quot; |
| SONET_OC3840 | &quot;sonet-oc3840&quot; |
| _1GFC_SFP | &quot;1gfc-sfp&quot; |
| _2GFC_SFP | &quot;2gfc-sfp&quot; |
| _4GFC_SFP | &quot;4gfc-sfp&quot; |
| _8GFC_SFPP | &quot;8gfc-sfpp&quot; |
| _16GFC_SFPP | &quot;16gfc-sfpp&quot; |
| _32GFC_SFP28 | &quot;32gfc-sfp28&quot; |
| _128GFC_SFP28 | &quot;128gfc-sfp28&quot; |
| INFINIBAND_SDR | &quot;infiniband-sdr&quot; |
| INFINIBAND_DDR | &quot;infiniband-ddr&quot; |
| INFINIBAND_QDR | &quot;infiniband-qdr&quot; |
| INFINIBAND_FDR10 | &quot;infiniband-fdr10&quot; |
| INFINIBAND_FDR | &quot;infiniband-fdr&quot; |
| INFINIBAND_EDR | &quot;infiniband-edr&quot; |
| INFINIBAND_HDR | &quot;infiniband-hdr&quot; |
| INFINIBAND_NDR | &quot;infiniband-ndr&quot; |
| INFINIBAND_XDR | &quot;infiniband-xdr&quot; |
| T1 | &quot;t1&quot; |
| E1 | &quot;e1&quot; |
| T3 | &quot;t3&quot; |
| E3 | &quot;e3&quot; |
| CISCO_STACKWISE | &quot;cisco-stackwise&quot; |
| CISCO_STACKWISE_PLUS | &quot;cisco-stackwise-plus&quot; |
| CISCO_FLEXSTACK | &quot;cisco-flexstack&quot; |
| CISCO_FLEXSTACK_PLUS | &quot;cisco-flexstack-plus&quot; |
| JUNIPER_VCP | &quot;juniper-vcp&quot; |
| EXTREME_SUMMITSTACK | &quot;extreme-summitstack&quot; |
| EXTREME_SUMMITSTACK_128 | &quot;extreme-summitstack-128&quot; |
| EXTREME_SUMMITSTACK_256 | &quot;extreme-summitstack-256&quot; |
| EXTREME_SUMMITSTACK_512 | &quot;extreme-summitstack-512&quot; |
| OTHER | &quot;other&quot; |



