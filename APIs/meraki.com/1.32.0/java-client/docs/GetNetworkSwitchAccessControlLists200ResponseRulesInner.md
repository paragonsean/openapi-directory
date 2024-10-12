

# GetNetworkSwitchAccessControlLists200ResponseRulesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | Description of the rule (optional) |  [optional] |
|**dstCidr** | **String** | Destination IP address (in IP or CIDR notation) |  [optional] |
|**dstPort** | **String** | Destination port |  [optional] |
|**ipVersion** | [**IpVersionEnum**](#IpVersionEnum) | IP address version |  [optional] |
|**policy** | [**PolicyEnum**](#PolicyEnum) | &#39;allow&#39; or &#39;deny&#39; traffic specified by this rule |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The type of protocol |  [optional] |
|**srcCidr** | **String** | Source IP address (in IP or CIDR notation) |  [optional] |
|**srcPort** | **String** | Source port |  [optional] |
|**vlan** | **String** | ncoming traffic VLAN |  [optional] |



## Enum: IpVersionEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |



## Enum: PolicyEnum

| Name | Value |
|---- | -----|
| ALLOW | &quot;allow&quot; |
| DENY | &quot;deny&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;any&quot; |
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



