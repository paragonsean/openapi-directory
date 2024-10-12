

# UpdateOrganizationSnmpRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**peerIps** | **List&lt;String&gt;** | The list of IPv4 addresses that are allowed to access the SNMP server. |  [optional] |
|**v2cEnabled** | **Boolean** | Boolean indicating whether SNMP version 2c is enabled for the organization. |  [optional] |
|**v3AuthMode** | [**V3AuthModeEnum**](#V3AuthModeEnum) | The SNMP version 3 authentication mode. Can be either &#39;MD5&#39; or &#39;SHA&#39;. |  [optional] |
|**v3AuthPass** | **String** | The SNMP version 3 authentication password. Must be at least 8 characters if specified. |  [optional] |
|**v3Enabled** | **Boolean** | Boolean indicating whether SNMP version 3 is enabled for the organization. |  [optional] |
|**v3PrivMode** | [**V3PrivModeEnum**](#V3PrivModeEnum) | The SNMP version 3 privacy mode. Can be either &#39;DES&#39; or &#39;AES128&#39;. |  [optional] |
|**v3PrivPass** | **String** | The SNMP version 3 privacy password. Must be at least 8 characters if specified. |  [optional] |



## Enum: V3AuthModeEnum

| Name | Value |
|---- | -----|
| MD5 | &quot;MD5&quot; |
| SHA | &quot;SHA&quot; |



## Enum: V3PrivModeEnum

| Name | Value |
|---- | -----|
| AES128 | &quot;AES128&quot; |
| DES | &quot;DES&quot; |



