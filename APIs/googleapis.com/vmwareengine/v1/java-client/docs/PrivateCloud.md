

# PrivateCloud

Represents a private cloud resource. Private clouds of type `STANDARD` and `TIME_LIMITED` are zonal resources, `STRETCHED` private clouds are regional.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Creation time of this resource. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. Time when the resource was scheduled for deletion. |  [optional] [readonly] |
|**description** | **String** | User-provided description for this private cloud. |  [optional] |
|**expireTime** | **String** | Output only. Time when the resource will be irreversibly deleted. |  [optional] [readonly] |
|**hcx** | [**Hcx**](Hcx.md) |  |  [optional] |
|**managementCluster** | [**ManagementCluster**](ManagementCluster.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of this private cloud. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60; |  [optional] [readonly] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**nsx** | [**Nsx**](Nsx.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the resource. New values may be added to this enum when appropriate. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. Type of the private cloud. Defaults to STANDARD. |  [optional] |
|**uid** | **String** | Output only. System-generated unique identifier for the resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Last update time of this resource. |  [optional] [readonly] |
|**vcenter** | [**Vcenter**](Vcenter.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETED | &quot;DELETED&quot; |
| PURGING | &quot;PURGING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;STANDARD&quot; |
| TIME_LIMITED | &quot;TIME_LIMITED&quot; |
| STRETCHED | &quot;STRETCHED&quot; |



