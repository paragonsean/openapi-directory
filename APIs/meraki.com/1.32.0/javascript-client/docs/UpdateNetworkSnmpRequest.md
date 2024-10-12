# MerakiDashboardApi.UpdateNetworkSnmpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **String** | The type of SNMP access. Can be one of &#39;none&#39; (disabled), &#39;community&#39; (V1/V2c), or &#39;users&#39; (V3). | [optional] 
**communityString** | **String** | The SNMP community string. Only relevant if &#39;access&#39; is set to &#39;community&#39;. | [optional] 
**users** | [**[UpdateNetworkSnmpRequestUsersInner]**](UpdateNetworkSnmpRequestUsersInner.md) | The list of SNMP users. Only relevant if &#39;access&#39; is set to &#39;users&#39;. | [optional] 



## Enum: AccessEnum


* `community` (value: `"community"`)

* `none` (value: `"none"`)

* `users` (value: `"users"`)




