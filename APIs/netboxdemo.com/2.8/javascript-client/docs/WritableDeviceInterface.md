# NetBoxApi.WritableDeviceInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**connectedEndpoint** | **{String: String}** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointType** | **String** |  | [optional] [readonly] 
**connectionStatus** | **Boolean** |  | [optional] 
**countIpaddresses** | **Number** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**device** | **Number** |  | 
**enabled** | **Boolean** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lag** | **Number** |  | [optional] 
**macAddress** | **String** |  | [optional] 
**mgmtOnly** | **Boolean** | This interface is used only for out-of-band management | [optional] 
**mode** | **String** |  | [optional] 
**mtu** | **Number** |  | [optional] 
**name** | **String** |  | 
**taggedVlans** | **[Number]** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**type** | **String** |  | 
**untaggedVlan** | **Number** |  | [optional] 



## Enum: ModeEnum


* `access` (value: `"access"`)

* `tagged` (value: `"tagged"`)

* `tagged-all` (value: `"tagged-all"`)





## Enum: TypeEnum


* `virtual` (value: `"virtual"`)

* `lag` (value: `"lag"`)

* `100base-tx` (value: `"100base-tx"`)

* `1000base-t` (value: `"1000base-t"`)

* `2.5gbase-t` (value: `"2.5gbase-t"`)

* `5gbase-t` (value: `"5gbase-t"`)

* `10gbase-t` (value: `"10gbase-t"`)

* `10gbase-cx4` (value: `"10gbase-cx4"`)

* `1000base-x-gbic` (value: `"1000base-x-gbic"`)

* `1000base-x-sfp` (value: `"1000base-x-sfp"`)

* `10gbase-x-sfpp` (value: `"10gbase-x-sfpp"`)

* `10gbase-x-xfp` (value: `"10gbase-x-xfp"`)

* `10gbase-x-xenpak` (value: `"10gbase-x-xenpak"`)

* `10gbase-x-x2` (value: `"10gbase-x-x2"`)

* `25gbase-x-sfp28` (value: `"25gbase-x-sfp28"`)

* `40gbase-x-qsfpp` (value: `"40gbase-x-qsfpp"`)

* `50gbase-x-sfp28` (value: `"50gbase-x-sfp28"`)

* `100gbase-x-cfp` (value: `"100gbase-x-cfp"`)

* `100gbase-x-cfp2` (value: `"100gbase-x-cfp2"`)

* `200gbase-x-cfp2` (value: `"200gbase-x-cfp2"`)

* `100gbase-x-cfp4` (value: `"100gbase-x-cfp4"`)

* `100gbase-x-cpak` (value: `"100gbase-x-cpak"`)

* `100gbase-x-qsfp28` (value: `"100gbase-x-qsfp28"`)

* `200gbase-x-qsfp56` (value: `"200gbase-x-qsfp56"`)

* `400gbase-x-qsfpdd` (value: `"400gbase-x-qsfpdd"`)

* `400gbase-x-osfp` (value: `"400gbase-x-osfp"`)

* `ieee802.11a` (value: `"ieee802.11a"`)

* `ieee802.11g` (value: `"ieee802.11g"`)

* `ieee802.11n` (value: `"ieee802.11n"`)

* `ieee802.11ac` (value: `"ieee802.11ac"`)

* `ieee802.11ad` (value: `"ieee802.11ad"`)

* `ieee802.11ax` (value: `"ieee802.11ax"`)

* `gsm` (value: `"gsm"`)

* `cdma` (value: `"cdma"`)

* `lte` (value: `"lte"`)

* `sonet-oc3` (value: `"sonet-oc3"`)

* `sonet-oc12` (value: `"sonet-oc12"`)

* `sonet-oc48` (value: `"sonet-oc48"`)

* `sonet-oc192` (value: `"sonet-oc192"`)

* `sonet-oc768` (value: `"sonet-oc768"`)

* `sonet-oc1920` (value: `"sonet-oc1920"`)

* `sonet-oc3840` (value: `"sonet-oc3840"`)

* `1gfc-sfp` (value: `"1gfc-sfp"`)

* `2gfc-sfp` (value: `"2gfc-sfp"`)

* `4gfc-sfp` (value: `"4gfc-sfp"`)

* `8gfc-sfpp` (value: `"8gfc-sfpp"`)

* `16gfc-sfpp` (value: `"16gfc-sfpp"`)

* `32gfc-sfp28` (value: `"32gfc-sfp28"`)

* `128gfc-sfp28` (value: `"128gfc-sfp28"`)

* `infiniband-sdr` (value: `"infiniband-sdr"`)

* `infiniband-ddr` (value: `"infiniband-ddr"`)

* `infiniband-qdr` (value: `"infiniband-qdr"`)

* `infiniband-fdr10` (value: `"infiniband-fdr10"`)

* `infiniband-fdr` (value: `"infiniband-fdr"`)

* `infiniband-edr` (value: `"infiniband-edr"`)

* `infiniband-hdr` (value: `"infiniband-hdr"`)

* `infiniband-ndr` (value: `"infiniband-ndr"`)

* `infiniband-xdr` (value: `"infiniband-xdr"`)

* `t1` (value: `"t1"`)

* `e1` (value: `"e1"`)

* `t3` (value: `"t3"`)

* `e3` (value: `"e3"`)

* `cisco-stackwise` (value: `"cisco-stackwise"`)

* `cisco-stackwise-plus` (value: `"cisco-stackwise-plus"`)

* `cisco-flexstack` (value: `"cisco-flexstack"`)

* `cisco-flexstack-plus` (value: `"cisco-flexstack-plus"`)

* `juniper-vcp` (value: `"juniper-vcp"`)

* `extreme-summitstack` (value: `"extreme-summitstack"`)

* `extreme-summitstack-128` (value: `"extreme-summitstack-128"`)

* `extreme-summitstack-256` (value: `"extreme-summitstack-256"`)

* `extreme-summitstack-512` (value: `"extreme-summitstack-512"`)

* `other` (value: `"other"`)




