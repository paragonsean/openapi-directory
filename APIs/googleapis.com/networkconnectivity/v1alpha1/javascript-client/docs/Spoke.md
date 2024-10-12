# NetworkConnectivityApi.Spoke

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | The time when the Spoke was created. | [optional] 
**description** | **String** | Short description of the spoke resource | [optional] 
**hub** | **String** | The resource URL of the hub resource that the spoke is attached to | [optional] 
**labels** | **{String: String}** | User-defined labels. | [optional] 
**linkedInterconnectAttachments** | **[String]** | The URIs of linked interconnect attachment resources | [optional] 
**linkedRouterApplianceInstances** | [**[RouterApplianceInstance]**](RouterApplianceInstance.md) | The URIs of linked Router appliance resources | [optional] 
**linkedVpnTunnels** | **[String]** | The URIs of linked VPN tunnel resources | [optional] 
**name** | **String** | Immutable. The name of a Spoke resource. | [optional] 
**state** | **String** | Output only. The current lifecycle state of this Hub. | [optional] [readonly] 
**uniqueId** | **String** | Output only. Google-generated UUID for this resource. This is unique across all Spoke resources. If a Spoke resource is deleted and another with the same name is created, it gets a different unique_id. | [optional] [readonly] 
**updateTime** | **String** | The time when the Spoke was updated. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




