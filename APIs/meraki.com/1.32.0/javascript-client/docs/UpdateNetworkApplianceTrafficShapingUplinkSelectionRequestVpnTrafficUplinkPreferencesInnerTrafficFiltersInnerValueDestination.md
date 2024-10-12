# MerakiDashboardApi.UpdateNetworkApplianceTrafficShapingUplinkSelectionRequestVpnTrafficUplinkPreferencesInnerTrafficFiltersInnerValueDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **String** | CIDR format address, or \&quot;any\&quot;. E.g.: \&quot;192.168.10.0/24\&quot;,  \&quot;192.168.10.1\&quot; (same as \&quot;192.168.10.1/32\&quot;), \&quot;0.0.0.0/0\&quot; (same as \&quot;any\&quot;) | [optional] 
**fqdn** | **String** | FQDN format address. Currently only availabe in &#39;destination&#39; of &#39;vpnTrafficUplinkPreference&#39; object. E.g.: &#39;www.google.com&#39; | [optional] 
**host** | **Number** | Host ID in the VLAN, should be used along with &#39;vlan&#39;, and not exceed the vlan subnet capacity. Currently only available under a template network. | [optional] 
**network** | **String** | Meraki network ID. Currently only available under a template network, and the value should be ID of either same template network, or another template network currently. E.g.: \&quot;L_12345678\&quot;. | [optional] 
**port** | **String** | E.g.: \&quot;any\&quot;, \&quot;0\&quot; (also means \&quot;any\&quot;), \&quot;8080\&quot;, \&quot;1-1024\&quot; | [optional] 
**vlan** | **Number** | VLAN ID of the configured VLAN in the Meraki network. Currently only available under a template network. | [optional] 


