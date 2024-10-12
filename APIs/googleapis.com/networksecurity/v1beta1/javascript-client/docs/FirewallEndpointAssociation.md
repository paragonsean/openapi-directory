# NetworkSecurityApi.FirewallEndpointAssociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Create time stamp | [optional] [readonly] 
**firewallEndpoint** | **String** | Required. The URL of the FirewallEndpoint that is being associated. | [optional] 
**labels** | **{String: String}** | Optional. Labels as key value pairs | [optional] 
**name** | **String** | Immutable. Identifier. name of resource | [optional] 
**network** | **String** | Required. The URL of the network that is being associated. | [optional] 
**reconciling** | **Boolean** | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the association. | [optional] [readonly] 
**tlsInspectionPolicy** | **String** | Optional. The URL of the TlsInspectionPolicy that is being associated. | [optional] 
**updateTime** | **String** | Output only. Update time stamp | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `INACTIVE` (value: `"INACTIVE"`)




