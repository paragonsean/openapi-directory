

# AppServicePlansListWebApps200ResponseValueInnerPropertiesHostNameSslStatesInner

SSL-enabled hostname.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostType** | [**HostTypeEnum**](#HostTypeEnum) | Indicates whether the hostname is a standard or repository hostname. |  [optional] |
|**name** | **String** | Hostname. |  [optional] |
|**sslState** | [**SslStateEnum**](#SslStateEnum) | SSL type. |  [optional] |
|**thumbprint** | **String** | SSL certificate thumbprint. |  [optional] |
|**toUpdate** | **Boolean** | Set to &lt;code&gt;true&lt;/code&gt; to update existing hostname. |  [optional] |
|**virtualIP** | **String** | Virtual IP address assigned to the hostname if IP based SSL is enabled. |  [optional] |



## Enum: HostTypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| REPOSITORY | &quot;Repository&quot; |



## Enum: SslStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| SNI_ENABLED | &quot;SniEnabled&quot; |
| IP_BASED_ENABLED | &quot;IpBasedEnabled&quot; |



