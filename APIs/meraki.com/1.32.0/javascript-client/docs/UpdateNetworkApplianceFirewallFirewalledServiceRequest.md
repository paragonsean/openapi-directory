# MerakiDashboardApi.UpdateNetworkApplianceFirewallFirewalledServiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | A string indicating the rule for which IPs are allowed to use the specified service. Acceptable values are \&quot;blocked\&quot; (no remote IPs can access the service), \&quot;restricted\&quot; (only allowed IPs can access the service), and \&quot;unrestriced\&quot; (any remote IP can access the service). This field is required | 
**allowedIps** | **[String]** | An array of allowed IPs that can access the service. This field is required if \&quot;access\&quot; is set to \&quot;restricted\&quot;. Otherwise this field is ignored | [optional] 



## Enum: AccessEnum


* `blocked` (value: `"blocked"`)

* `restricted` (value: `"restricted"`)

* `unrestricted` (value: `"unrestricted"`)




