# MerakiDashboardApi.UpdateOrganizationSnmpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peerIps** | **[String]** | The list of IPv4 addresses that are allowed to access the SNMP server. | [optional] 
**v2cEnabled** | **Boolean** | Boolean indicating whether SNMP version 2c is enabled for the organization. | [optional] 
**v3AuthMode** | **String** | The SNMP version 3 authentication mode. Can be either &#39;MD5&#39; or &#39;SHA&#39;. | [optional] 
**v3AuthPass** | **String** | The SNMP version 3 authentication password. Must be at least 8 characters if specified. | [optional] 
**v3Enabled** | **Boolean** | Boolean indicating whether SNMP version 3 is enabled for the organization. | [optional] 
**v3PrivMode** | **String** | The SNMP version 3 privacy mode. Can be either &#39;DES&#39; or &#39;AES128&#39;. | [optional] 
**v3PrivPass** | **String** | The SNMP version 3 privacy password. Must be at least 8 characters if specified. | [optional] 



## Enum: V3AuthModeEnum


* `MD5` (value: `"MD5"`)

* `SHA` (value: `"SHA"`)





## Enum: V3PrivModeEnum


* `AES128` (value: `"AES128"`)

* `DES` (value: `"DES"`)




