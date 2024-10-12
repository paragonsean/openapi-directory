# WebSiteManagementClient.HostNameSslState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Host name | [optional] 
**sslState** | **String** | SSL type | 
**thumbprint** | **String** | SSL cert thumbprint | [optional] 
**toUpdate** | **Boolean** | Set this flag to update existing host name | [optional] 
**virtualIP** | **String** | Virtual IP address assigned to the host name if IP based SSL is enabled | [optional] 



## Enum: SslStateEnum


* `Disabled` (value: `"Disabled"`)

* `SniEnabled` (value: `"SniEnabled"`)

* `IpBasedEnabled` (value: `"IpBasedEnabled"`)




