# WorkloadManagerApi.SapDiscoveryResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceProperties** | [**SapDiscoveryResourceInstanceProperties**](SapDiscoveryResourceInstanceProperties.md) |  | [optional] 
**relatedResources** | **[String]** | Optional. A list of resource URIs related to this resource. | [optional] 
**resourceKind** | **String** | Required. ComputeInstance, ComputeDisk, VPC, Bare Metal server, etc. | [optional] 
**resourceType** | **String** | Required. The type of this resource. | [optional] 
**resourceUri** | **String** | Required. URI of the resource, includes project, location, and name. | [optional] 
**updateTime** | **String** | Required. Unix timestamp of when this resource last had its discovery data updated. | [optional] 



## Enum: ResourceKindEnum


* `UNSPECIFIED` (value: `"RESOURCE_KIND_UNSPECIFIED"`)

* `INSTANCE` (value: `"RESOURCE_KIND_INSTANCE"`)

* `DISK` (value: `"RESOURCE_KIND_DISK"`)

* `ADDRESS` (value: `"RESOURCE_KIND_ADDRESS"`)

* `FILESTORE` (value: `"RESOURCE_KIND_FILESTORE"`)

* `HEALTH_CHECK` (value: `"RESOURCE_KIND_HEALTH_CHECK"`)

* `FORWARDING_RULE` (value: `"RESOURCE_KIND_FORWARDING_RULE"`)

* `BACKEND_SERVICE` (value: `"RESOURCE_KIND_BACKEND_SERVICE"`)

* `SUBNETWORK` (value: `"RESOURCE_KIND_SUBNETWORK"`)

* `NETWORK` (value: `"RESOURCE_KIND_NETWORK"`)

* `PUBLIC_ADDRESS` (value: `"RESOURCE_KIND_PUBLIC_ADDRESS"`)

* `INSTANCE_GROUP` (value: `"RESOURCE_KIND_INSTANCE_GROUP"`)





## Enum: ResourceTypeEnum


* `UNSPECIFIED` (value: `"RESOURCE_TYPE_UNSPECIFIED"`)

* `COMPUTE` (value: `"RESOURCE_TYPE_COMPUTE"`)

* `STORAGE` (value: `"RESOURCE_TYPE_STORAGE"`)

* `NETWORK` (value: `"RESOURCE_TYPE_NETWORK"`)




