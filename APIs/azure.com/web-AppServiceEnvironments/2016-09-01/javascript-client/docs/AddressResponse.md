# AppServiceEnvironmentsApiClient.AddressResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internalIpAddress** | **String** | Virtual Network internal IP address of the App Service Environment if it is in internal load-balancing mode. | [optional] 
**outboundIpAddresses** | **[String]** | IP addresses appearing on outbound connections. | [optional] 
**serviceIpAddress** | **String** | Main public virtual IP. | [optional] 
**vipMappings** | [**[AddressResponseVipMappingsInner]**](AddressResponseVipMappingsInner.md) | Additional virtual IPs. | [optional] 


