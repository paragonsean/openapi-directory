# MerakiDashboardApi.GetNetworkApplianceTrafficShapingUplinkSelection200ResponseVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **String** | CIDR format address (e.g.\&quot;192.168.10.1\&quot;, which is the same as \&quot;192.168.10.1/32\&quot;), or \&quot;any\&quot;. Cannot be used in combination with the \&quot;vlan\&quot; or \&quot;fqdn\&quot; property | [optional] 
**fqdn** | **String** | FQDN format address. Cannot be used in combination with the \&quot;cidr\&quot; or \&quot;fqdn\&quot; property and is currently only available in the \&quot;destination\&quot; object of the \&quot;vpnTrafficUplinkPreference\&quot; object. E.g.: \&quot;www.google.com\&quot; | [optional] 
**host** | **Number** | Host ID in the VLAN. Should not exceed the VLAN subnet capacity. Must be used along with the \&quot;vlan\&quot; property and is currently only available under a template network. | [optional] 
**network** | **String** | Meraki network ID. Currently only available under a template network, and the value should be ID of either same template network, or another template network currently. E.g.: \&quot;L_12345678\&quot;. | [optional] 
**port** | **String** | E.g.: \&quot;any\&quot;, \&quot;0\&quot; (also means \&quot;any\&quot;), \&quot;8080\&quot;, \&quot;1-1024\&quot; | [optional] 
**vlan** | **Number** | VLAN ID of the configured VLAN in the Meraki network. Cannot be used in combination with the \&quot;cidr\&quot; or \&quot;fqdn\&quot; property and is currently only available under a template network. | [optional] 


