

# SapDiscoveryResource

Message describing a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceProperties** | [**SapDiscoveryResourceInstanceProperties**](SapDiscoveryResourceInstanceProperties.md) |  |  [optional] |
|**relatedResources** | **List&lt;String&gt;** | Optional. A list of resource URIs related to this resource. |  [optional] |
|**resourceKind** | [**ResourceKindEnum**](#ResourceKindEnum) | Required. ComputeInstance, ComputeDisk, VPC, Bare Metal server, etc. |  [optional] |
|**resourceType** | [**ResourceTypeEnum**](#ResourceTypeEnum) | Required. The type of this resource. |  [optional] |
|**resourceUri** | **String** | Required. URI of the resource, includes project, location, and name. |  [optional] |
|**updateTime** | **String** | Required. Unix timestamp of when this resource last had its discovery data updated. |  [optional] |



## Enum: ResourceKindEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RESOURCE_KIND_UNSPECIFIED&quot; |
| INSTANCE | &quot;RESOURCE_KIND_INSTANCE&quot; |
| DISK | &quot;RESOURCE_KIND_DISK&quot; |
| ADDRESS | &quot;RESOURCE_KIND_ADDRESS&quot; |
| FILESTORE | &quot;RESOURCE_KIND_FILESTORE&quot; |
| HEALTH_CHECK | &quot;RESOURCE_KIND_HEALTH_CHECK&quot; |
| FORWARDING_RULE | &quot;RESOURCE_KIND_FORWARDING_RULE&quot; |
| BACKEND_SERVICE | &quot;RESOURCE_KIND_BACKEND_SERVICE&quot; |
| SUBNETWORK | &quot;RESOURCE_KIND_SUBNETWORK&quot; |
| NETWORK | &quot;RESOURCE_KIND_NETWORK&quot; |
| PUBLIC_ADDRESS | &quot;RESOURCE_KIND_PUBLIC_ADDRESS&quot; |
| INSTANCE_GROUP | &quot;RESOURCE_KIND_INSTANCE_GROUP&quot; |



## Enum: ResourceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RESOURCE_TYPE_UNSPECIFIED&quot; |
| COMPUTE | &quot;RESOURCE_TYPE_COMPUTE&quot; |
| STORAGE | &quot;RESOURCE_TYPE_STORAGE&quot; |
| NETWORK | &quot;RESOURCE_TYPE_NETWORK&quot; |



