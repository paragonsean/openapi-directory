

# FloatingIpsGet200ResponseFloatingIpsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blocked** | **Boolean** | Whether the IP is blocked |  |
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**description** | **String** | Description of the Resource |  |
|**dnsPtr** | [**List&lt;FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner&gt;**](FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner.md) | Array of reverse DNS entries |  |
|**homeLocation** | [**FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation**](FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation.md) |  |  |
|**id** | **Integer** | ID of the Resource |  |
|**ip** | **String** | IP address |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**name** | **String** | Name of the Resource. Must be unique per Project. |  |
|**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  |  |
|**server** | **Integer** | ID of the Server the Floating IP is assigned to, null if it is not assigned at all |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Floating IP |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |



