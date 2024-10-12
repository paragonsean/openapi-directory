# NetBoxApi.WritableInterfaceTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**deviceType** | **Number** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**mgmtOnly** | **Boolean** |  | [optional] 
**moduleType** | **Number** |  | [optional] 
**name** | **String** |  {module} is accepted as a substitution for the module bay position when attached to a module type.  | 
**poeMode** | **String** |  | [optional] 
**poeType** | **String** |  | [optional] 
**type** | **String** |  | 
**url** | **String** |  | [optional] [readonly] 



## Enum: PoeModeEnum


* `pd` (value: `"pd"`)

* `pse` (value: `"pse"`)





## Enum: PoeTypeEnum


* `type1-ieee802.3af` (value: `"type1-ieee802.3af"`)

* `type2-ieee802.3at` (value: `"type2-ieee802.3at"`)

* `type2-ieee802.3az` (value: `"type2-ieee802.3az"`)

* `type3-ieee802.3bt` (value: `"type3-ieee802.3bt"`)

* `type4-ieee802.3bt` (value: `"type4-ieee802.3bt"`)

* `passive-24v-2pair` (value: `"passive-24v-2pair"`)

* `passive-24v-4pair` (value: `"passive-24v-4pair"`)

* `passive-48v-2pair` (value: `"passive-48v-2pair"`)

* `passive-48v-4pair` (value: `"passive-48v-4pair"`)





## Enum: TypeEnum


* `virtual` (value: `"virtual"`)

* `bridge` (value: `"bridge"`)

* `lag` (value: `"lag"`)

* `100base-fx` (value: `"100base-fx"`)

* `100base-lfx` (value: `"100base-lfx"`)

* `100base-tx` (value: `"100base-tx"`)

* `100base-t1` (value: `"100base-t1"`)

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

* `50gbase-x-sfp56` (value: `"50gbase-x-sfp56"`)

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

* `800gbase-x-qsfpdd` (value: `"800gbase-x-qsfpdd"`)

* `800gbase-x-osfp` (value: `"800gbase-x-osfp"`)

* `1000base-kx` (value: `"1000base-kx"`)

* `10gbase-kr` (value: `"10gbase-kr"`)

* `10gbase-kx4` (value: `"10gbase-kx4"`)

* `25gbase-kr` (value: `"25gbase-kr"`)

* `40gbase-kr4` (value: `"40gbase-kr4"`)

* `50gbase-kr` (value: `"50gbase-kr"`)

* `100gbase-kp4` (value: `"100gbase-kp4"`)

* `100gbase-kr2` (value: `"100gbase-kr2"`)

* `100gbase-kr4` (value: `"100gbase-kr4"`)

* `ieee802.11a` (value: `"ieee802.11a"`)

* `ieee802.11g` (value: `"ieee802.11g"`)

* `ieee802.11n` (value: `"ieee802.11n"`)

* `ieee802.11ac` (value: `"ieee802.11ac"`)

* `ieee802.11ad` (value: `"ieee802.11ad"`)

* `ieee802.11ax` (value: `"ieee802.11ax"`)

* `ieee802.11ay` (value: `"ieee802.11ay"`)

* `ieee802.15.1` (value: `"ieee802.15.1"`)

* `other-wireless` (value: `"other-wireless"`)

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

* `64gfc-qsfpp` (value: `"64gfc-qsfpp"`)

* `128gfc-qsfp28` (value: `"128gfc-qsfp28"`)

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

* `xdsl` (value: `"xdsl"`)

* `docsis` (value: `"docsis"`)

* `gpon` (value: `"gpon"`)

* `xg-pon` (value: `"xg-pon"`)

* `xgs-pon` (value: `"xgs-pon"`)

* `ng-pon2` (value: `"ng-pon2"`)

* `epon` (value: `"epon"`)

* `10g-epon` (value: `"10g-epon"`)

* `cisco-stackwise` (value: `"cisco-stackwise"`)

* `cisco-stackwise-plus` (value: `"cisco-stackwise-plus"`)

* `cisco-flexstack` (value: `"cisco-flexstack"`)

* `cisco-flexstack-plus` (value: `"cisco-flexstack-plus"`)

* `cisco-stackwise-80` (value: `"cisco-stackwise-80"`)

* `cisco-stackwise-160` (value: `"cisco-stackwise-160"`)

* `cisco-stackwise-320` (value: `"cisco-stackwise-320"`)

* `cisco-stackwise-480` (value: `"cisco-stackwise-480"`)

* `cisco-stackwise-1t` (value: `"cisco-stackwise-1t"`)

* `juniper-vcp` (value: `"juniper-vcp"`)

* `extreme-summitstack` (value: `"extreme-summitstack"`)

* `extreme-summitstack-128` (value: `"extreme-summitstack-128"`)

* `extreme-summitstack-256` (value: `"extreme-summitstack-256"`)

* `extreme-summitstack-512` (value: `"extreme-summitstack-512"`)

* `other` (value: `"other"`)




