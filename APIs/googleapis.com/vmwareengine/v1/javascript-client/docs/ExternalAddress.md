# VMwareEngineApi.ExternalAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of this resource. | [optional] [readonly] 
**description** | **String** | User-provided description for this resource. | [optional] 
**externalIp** | **String** | Output only. The external IP address of a workload VM. | [optional] [readonly] 
**internalIp** | **String** | The internal IP address of a workload VM. | [optional] 
**name** | **String** | Output only. The resource name of this external IP address. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address&#x60; | [optional] [readonly] 
**state** | **String** | Output only. The state of the resource. | [optional] [readonly] 
**uid** | **String** | Output only. System-generated unique identifier for the resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update time of this resource. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)




