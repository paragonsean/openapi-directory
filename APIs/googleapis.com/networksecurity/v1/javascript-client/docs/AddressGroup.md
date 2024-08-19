# NetworkSecurityApi.AddressGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **Number** | Required. Capacity of the Address Group | [optional] 
**createTime** | **String** | Output only. The timestamp when the resource was created. | [optional] [readonly] 
**description** | **String** | Optional. Free-text description of the resource. | [optional] 
**items** | **[String]** | Optional. List of items. | [optional] 
**labels** | **{String: String}** | Optional. Set of label tags associated with the AddressGroup resource. | [optional] 
**name** | **String** | Required. Name of the AddressGroup resource. It matches pattern &#x60;projects/_*_/locations/{location}/addressGroups/&#x60;. | [optional] 
**selfLink** | **String** | Output only. Server-defined fully-qualified URL for this resource. | [optional] [readonly] 
**type** | **String** | Required. The type of the Address Group. Possible values are \&quot;IPv4\&quot; or \&quot;IPV6\&quot;. | [optional] 
**updateTime** | **String** | Output only. The timestamp when the resource was updated. | [optional] [readonly] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `IPV4` (value: `"IPV4"`)

* `IPV6` (value: `"IPV6"`)




