# MerakiDashboardApi.UpdateNetworkWirelessAlternateManagementInterfaceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPoints** | [**[UpdateNetworkWirelessAlternateManagementInterfaceRequestAccessPointsInner]**](UpdateNetworkWirelessAlternateManagementInterfaceRequestAccessPointsInner.md) | Array of access point serial number and IP assignment. Note: accessPoints IP assignment is not applicable for template networks, in other words, do not put &#39;accessPoints&#39; in the body when updating template networks. Also, an empty &#39;accessPoints&#39; array will remove all previous static IP assignments | [optional] 
**enabled** | **Boolean** | Boolean value to enable or disable alternate management interface | [optional] 
**protocols** | **[String]** | Can be one or more of the following values: &#39;radius&#39;, &#39;snmp&#39;, &#39;syslog&#39; or &#39;ldap&#39; | [optional] 
**vlanId** | **Number** | Alternate management interface VLAN, must be between 1 and 4094 | [optional] 



## Enum: [ProtocolsEnum]


* `ldap` (value: `"ldap"`)

* `radius` (value: `"radius"`)

* `snmp` (value: `"snmp"`)

* `syslog` (value: `"syslog"`)




