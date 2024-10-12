# MerakiDashboardApi.UpdateNetworkSwitchStackRoutingInterfaceRequestIpv6

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The IPv6 address of the interface. Required if assignmentMode is included and set as &#39;static&#39;. Must not be included if assignmentMode is &#39;eui-64&#39;. | [optional] 
**assignmentMode** | **String** | The IPv6 assignment mode for the interface. Can be either &#39;eui-64&#39; or &#39;static&#39;. | [optional] 
**gateway** | **String** | The IPv6 default gateway of the interface. Required if prefix is defined and this is the first interface with IPv6 configured for the stack. | [optional] 
**prefix** | **String** | The IPv6 prefix of the interface. Required if IPv6 object is included and interface does not already have ipv6.prefix configured | [optional] 


