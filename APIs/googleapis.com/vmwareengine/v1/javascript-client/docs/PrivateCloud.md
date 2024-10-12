# VMwareEngineApi.PrivateCloud

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of this resource. | [optional] [readonly] 
**deleteTime** | **String** | Output only. Time when the resource was scheduled for deletion. | [optional] [readonly] 
**description** | **String** | User-provided description for this private cloud. | [optional] 
**expireTime** | **String** | Output only. Time when the resource will be irreversibly deleted. | [optional] [readonly] 
**hcx** | [**Hcx**](Hcx.md) |  | [optional] 
**managementCluster** | [**ManagementCluster**](ManagementCluster.md) |  | [optional] 
**name** | **String** | Output only. The resource name of this private cloud. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud&#x60; | [optional] [readonly] 
**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  | [optional] 
**nsx** | [**Nsx**](Nsx.md) |  | [optional] 
**state** | **String** | Output only. State of the resource. New values may be added to this enum when appropriate. | [optional] [readonly] 
**type** | **String** | Optional. Type of the private cloud. Defaults to STANDARD. | [optional] 
**uid** | **String** | Output only. System-generated unique identifier for the resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update time of this resource. | [optional] [readonly] 
**vcenter** | [**Vcenter**](Vcenter.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `UPDATING` (value: `"UPDATING"`)

* `FAILED` (value: `"FAILED"`)

* `DELETED` (value: `"DELETED"`)

* `PURGING` (value: `"PURGING"`)





## Enum: TypeEnum


* `STANDARD` (value: `"STANDARD"`)

* `TIME_LIMITED` (value: `"TIME_LIMITED"`)

* `STRETCHED` (value: `"STRETCHED"`)




