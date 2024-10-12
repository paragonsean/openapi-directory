# WebSiteManagementClient.AddressResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internalIpAddress** | **String** | VNET internal ip address of the hostingEnvironment (App Service Environment) if it is in internal load-balancing mode | [optional] 
**outboundIpAddresses** | **[String]** | IP addresses appearing on outbound connections | [optional] 
**serviceIpAddress** | **String** | Main public vip | [optional] 
**vipMappings** | [**[VirtualIPMapping]**](VirtualIPMapping.md) | Additional vips | [optional] 


