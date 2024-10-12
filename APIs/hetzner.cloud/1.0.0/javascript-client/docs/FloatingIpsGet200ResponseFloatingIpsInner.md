# HetznerCloudApi.FloatingIpsGet200ResponseFloatingIpsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **Boolean** | Whether the IP is blocked | 
**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) | 
**description** | **String** | Description of the Resource | 
**dnsPtr** | [**[FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner]**](FloatingIpsGet200ResponseFloatingIpsInnerDnsPtrInner.md) | Array of reverse DNS entries | 
**homeLocation** | [**FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation**](FloatingIpsGet200ResponseFloatingIpsInnerHomeLocation.md) |  | 
**id** | **Number** | ID of the Resource | 
**ip** | **String** | IP address | 
**labels** | **{String: String}** | User-defined labels (key-value pairs) | 
**name** | **String** | Name of the Resource. Must be unique per Project. | 
**protection** | [**FloatingIpsGet200ResponseFloatingIpsInnerProtection**](FloatingIpsGet200ResponseFloatingIpsInnerProtection.md) |  | 
**server** | **Number** | ID of the Server the Floating IP is assigned to, null if it is not assigned at all | 
**type** | **String** | Type of the Floating IP | 



## Enum: TypeEnum


* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)




