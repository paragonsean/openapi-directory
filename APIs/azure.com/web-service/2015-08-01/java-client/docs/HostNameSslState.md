

# HostNameSslState

Object that represents a SSL-enabled host name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Host name |  [optional] |
|**sslState** | [**SslStateEnum**](#SslStateEnum) | SSL type |  |
|**thumbprint** | **String** | SSL cert thumbprint |  [optional] |
|**toUpdate** | **Boolean** | Set this flag to update existing host name |  [optional] |
|**virtualIP** | **String** | Virtual IP address assigned to the host name if IP based SSL is enabled |  [optional] |



## Enum: SslStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| SNI_ENABLED | &quot;SniEnabled&quot; |
| IP_BASED_ENABLED | &quot;IpBasedEnabled&quot; |



