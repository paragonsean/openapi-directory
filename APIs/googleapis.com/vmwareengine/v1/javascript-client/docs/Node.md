# VMwareEngineApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customCoreCount** | **String** | Output only. Customized number of cores | [optional] [readonly] 
**fqdn** | **String** | Output only. Fully qualified domain name of the node. | [optional] [readonly] 
**internalIp** | **String** | Output only. Internal IP address of the node. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of this node. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster/nodes/my-node | [optional] [readonly] 
**nodeTypeId** | **String** | Output only. The canonical identifier of the node type (corresponds to the &#x60;NodeType&#x60;). For example: standard-72. | [optional] [readonly] 
**state** | **String** | Output only. The state of the appliance. | [optional] [readonly] 
**version** | **String** | Output only. The version number of the VMware ESXi management component in this cluster. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `FAILED` (value: `"FAILED"`)

* `UPGRADING` (value: `"UPGRADING"`)




