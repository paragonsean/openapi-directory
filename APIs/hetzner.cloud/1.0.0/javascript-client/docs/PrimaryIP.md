# HetznerCloudApi.PrimaryIP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigneeId** | **Number** | ID of the resource the Primary IP is assigned to, null if it is not assigned at all | 
**assigneeType** | **String** | Resource type the Primary IP can be assigned to | 
**autoDelete** | **Boolean** | Delete this Primary IP when the resource it is assigned to is deleted | 
**blocked** | **Boolean** | Whether the IP is blocked | 
**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) | 
**datacenter** | [**PrimaryIPDatacenter**](PrimaryIPDatacenter.md) |  | 
**dnsPtr** | [**[PrimaryIPDnsPtrInner]**](PrimaryIPDnsPtrInner.md) | Array of reverse DNS entries | 
**id** | **Number** | ID of the Resource | 
**ip** | **String** | IP address | 
**labels** | **{String: String}** | User-defined labels (key-value pairs) | 
**name** | **String** | Name of the Resource. Must be unique per Project. | 
**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  | 
**type** | **String** | Type of the Primary IP | 



## Enum: AssigneeTypeEnum


* `server` (value: `"server"`)





## Enum: TypeEnum


* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)




