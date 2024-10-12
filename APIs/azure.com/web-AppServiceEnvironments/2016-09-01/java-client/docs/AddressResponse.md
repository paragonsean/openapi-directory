

# AddressResponse

Describes main public IP address and any extra virtual IPs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**internalIpAddress** | **String** | Virtual Network internal IP address of the App Service Environment if it is in internal load-balancing mode. |  [optional] |
|**outboundIpAddresses** | **List&lt;String&gt;** | IP addresses appearing on outbound connections. |  [optional] |
|**serviceIpAddress** | **String** | Main public virtual IP. |  [optional] |
|**vipMappings** | [**List&lt;AddressResponseVipMappingsInner&gt;**](AddressResponseVipMappingsInner.md) | Additional virtual IPs. |  [optional] |



