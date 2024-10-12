# MerakiDashboardApi.GetNetworkSwitchAccessControlLists200ResponseRulesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | Description of the rule (optional) | [optional] 
**dstCidr** | **String** | Destination IP address (in IP or CIDR notation) | [optional] 
**dstPort** | **String** | Destination port | [optional] 
**ipVersion** | **String** | IP address version | [optional] 
**policy** | **String** | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule | [optional] 
**protocol** | **String** | The type of protocol | [optional] 
**srcCidr** | **String** | Source IP address (in IP or CIDR notation) | [optional] 
**srcPort** | **String** | Source port | [optional] 
**vlan** | **String** | ncoming traffic VLAN | [optional] 



## Enum: IpVersionEnum


* `any` (value: `"any"`)

* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)





## Enum: PolicyEnum


* `allow` (value: `"allow"`)

* `deny` (value: `"deny"`)





## Enum: ProtocolEnum


* `any` (value: `"any"`)

* `tcp` (value: `"tcp"`)

* `udp` (value: `"udp"`)




