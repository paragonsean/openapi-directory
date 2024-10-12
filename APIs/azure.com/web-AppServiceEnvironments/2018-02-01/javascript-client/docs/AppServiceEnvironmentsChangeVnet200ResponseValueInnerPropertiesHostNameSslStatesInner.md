# AppServiceEnvironmentsApiClient.AppServiceEnvironmentsChangeVnet200ResponseValueInnerPropertiesHostNameSslStatesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostType** | **String** | Indicates whether the hostname is a standard or repository hostname. | [optional] 
**name** | **String** | Hostname. | [optional] 
**sslState** | **String** | SSL type. | [optional] 
**thumbprint** | **String** | SSL certificate thumbprint. | [optional] 
**toUpdate** | **Boolean** | Set to &lt;code&gt;true&lt;/code&gt; to update existing hostname. | [optional] 
**virtualIP** | **String** | Virtual IP address assigned to the hostname if IP based SSL is enabled. | [optional] 



## Enum: HostTypeEnum


* `Standard` (value: `"Standard"`)

* `Repository` (value: `"Repository"`)





## Enum: SslStateEnum


* `Disabled` (value: `"Disabled"`)

* `SniEnabled` (value: `"SniEnabled"`)

* `IpBasedEnabled` (value: `"IpBasedEnabled"`)




