# VMwareEngineApi.ManagementDnsZoneBinding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Creation time of this resource. | [optional] [readonly] 
**description** | **String** | User-provided description for this resource. | [optional] 
**name** | **String** | Output only. The resource name of this binding. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding&#x60; | [optional] [readonly] 
**state** | **String** | Output only. The state of the resource. | [optional] [readonly] 
**uid** | **String** | Output only. System-generated unique identifier for the resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update time of this resource. | [optional] [readonly] 
**vmwareEngineNetwork** | **String** | Network to bind is a VMware Engine network. Specify the name in the following form for VMware engine network: &#x60;projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}&#x60;. &#x60;{project}&#x60; can either be a project number or a project ID. | [optional] 
**vpcNetwork** | **String** | Network to bind is a standard consumer VPC. Specify the name in the following form for consumer VPC network: &#x60;projects/{project}/global/networks/{network_id}&#x60;. &#x60;{project}&#x60; can either be a project number or a project ID. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `UPDATING` (value: `"UPDATING"`)

* `DELETING` (value: `"DELETING"`)

* `FAILED` (value: `"FAILED"`)




