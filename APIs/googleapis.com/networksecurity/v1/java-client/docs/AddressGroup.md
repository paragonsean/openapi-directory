

# AddressGroup

AddressGroup is a resource that specifies how a collection of IP/DNS used in Firewall Policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Required. Capacity of the Address Group |  [optional] |
|**createTime** | **String** | Output only. The timestamp when the resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Free-text description of the resource. |  [optional] |
|**items** | **List&lt;String&gt;** | Optional. List of items. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Set of label tags associated with the AddressGroup resource. |  [optional] |
|**name** | **String** | Required. Name of the AddressGroup resource. It matches pattern &#x60;projects/_*_/locations/{location}/addressGroups/&#x60;. |  [optional] |
|**selfLink** | **String** | Output only. Server-defined fully-qualified URL for this resource. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. The type of the Address Group. Possible values are \&quot;IPv4\&quot; or \&quot;IPV6\&quot;. |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the resource was updated. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| IPV4 | &quot;IPV4&quot; |
| IPV6 | &quot;IPV6&quot; |



