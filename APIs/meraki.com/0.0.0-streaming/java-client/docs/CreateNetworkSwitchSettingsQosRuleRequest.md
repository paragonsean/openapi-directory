

# CreateNetworkSwitchSettingsQosRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dscp** | **Integer** | DSCP tag. Set this to -1 to trust incoming DSCP. Default value is 0 |  [optional] |
|**dstPort** | **Integer** | The destination port of the incoming packet. Applicable only if protocol is TCP or UDP. |  [optional] |
|**dstPortRange** | **String** | The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80 |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol of the incoming packet. Can be one of \&quot;ANY\&quot;, \&quot;TCP\&quot; or \&quot;UDP\&quot;. Default value is \&quot;ANY\&quot; |  [optional] |
|**srcPort** | **Integer** | The source port of the incoming packet. Applicable only if protocol is TCP or UDP. |  [optional] |
|**srcPortRange** | **String** | The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80 |  [optional] |
|**vlan** | **Integer** | The VLAN of the incoming packet. A null value will match any VLAN. |  |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| ANY | &quot;ANY&quot; |
| TCP | &quot;TCP&quot; |
| UDP | &quot;UDP&quot; |



