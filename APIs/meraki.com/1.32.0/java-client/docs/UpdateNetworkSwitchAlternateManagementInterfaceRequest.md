

# UpdateNetworkSwitchAlternateManagementInterfaceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Boolean value to enable or disable AMI configuration. If enabled, VLAN and protocols must be set |  [optional] |
|**protocols** | [**List&lt;ProtocolsEnum&gt;**](#List&lt;ProtocolsEnum&gt;) | Can be one or more of the following values: &#39;radius&#39;, &#39;snmp&#39; or &#39;syslog&#39; |  [optional] |
|**switches** | [**List&lt;UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner&gt;**](UpdateNetworkSwitchAlternateManagementInterfaceRequestSwitchesInner.md) | Array of switch serial number and IP assignment. If parameter is present, it cannot have empty body. Note: switches parameter is not applicable for template networks, in other words, do not put &#39;switches&#39; in the body when updating template networks. Also, an empty &#39;switches&#39; array will remove all previous assignments |  [optional] |
|**vlanId** | **Integer** | Alternate management VLAN, must be between 1 and 4094 |  [optional] |



## Enum: List&lt;ProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| RADIUS | &quot;radius&quot; |
| SNMP | &quot;snmp&quot; |
| SYSLOG | &quot;syslog&quot; |



