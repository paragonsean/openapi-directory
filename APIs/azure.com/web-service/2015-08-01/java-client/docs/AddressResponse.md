

# AddressResponse

Describes main public ip address and any extra vips

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**internalIpAddress** | **String** | VNET internal ip address of the hostingEnvironment (App Service Environment) if it is in internal load-balancing mode |  [optional] |
|**outboundIpAddresses** | **List&lt;String&gt;** | IP addresses appearing on outbound connections |  [optional] |
|**serviceIpAddress** | **String** | Main public vip |  [optional] |
|**vipMappings** | [**List&lt;VirtualIPMapping&gt;**](VirtualIPMapping.md) | Additional vips |  [optional] |



