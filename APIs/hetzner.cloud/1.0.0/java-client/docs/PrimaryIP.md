

# PrimaryIP


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assigneeId** | **Integer** | ID of the resource the Primary IP is assigned to, null if it is not assigned at all |  |
|**assigneeType** | [**AssigneeTypeEnum**](#AssigneeTypeEnum) | Resource type the Primary IP can be assigned to |  |
|**autoDelete** | **Boolean** | Delete this Primary IP when the resource it is assigned to is deleted |  |
|**blocked** | **Boolean** | Whether the IP is blocked |  |
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**datacenter** | [**PrimaryIPDatacenter**](PrimaryIPDatacenter.md) |  |  |
|**dnsPtr** | [**List&lt;PrimaryIPDnsPtrInner&gt;**](PrimaryIPDnsPtrInner.md) | Array of reverse DNS entries |  |
|**id** | **Integer** | ID of the Resource |  |
|**ip** | **String** | IP address |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**name** | **String** | Name of the Resource. Must be unique per Project. |  |
|**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Primary IP |  |



## Enum: AssigneeTypeEnum

| Name | Value |
|---- | -----|
| SERVER | &quot;server&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |



