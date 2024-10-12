# NetworkConnectivityApi.Route

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time the route was created. | [optional] [readonly] 
**description** | **String** | An optional description of the route. | [optional] 
**ipCidrRange** | **String** | The destination IP address range. | [optional] 
**labels** | **{String: String}** | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). | [optional] 
**location** | **String** | Output only. The location of the route. Uses the following form: \&quot;projects/{project}/locations/{location}\&quot; Example: projects/1234/locations/us-central1 | [optional] [readonly] 
**name** | **String** | Immutable. The name of the route. Route names must be unique. Route names use the following form: &#x60;projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}/routes/{route_id}&#x60; | [optional] 
**nextHopVpcNetwork** | [**NextHopVpcNetwork**](NextHopVpcNetwork.md) |  | [optional] 
**spoke** | **String** | Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE | [optional] 
**state** | **String** | Output only. The current lifecycle state of the route. | [optional] [readonly] 
**type** | **String** | Output only. The route&#39;s type. Its type is determined by the properties of its IP address range. | [optional] [readonly] 
**uid** | **String** | Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different &#x60;uid&#x60;. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time the route was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `ACCEPTING` (value: `"ACCEPTING"`)

* `REJECTING` (value: `"REJECTING"`)

* `UPDATING` (value: `"UPDATING"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `OBSOLETE` (value: `"OBSOLETE"`)





## Enum: TypeEnum


* `ROUTE_TYPE_UNSPECIFIED` (value: `"ROUTE_TYPE_UNSPECIFIED"`)

* `VPC_PRIMARY_SUBNET` (value: `"VPC_PRIMARY_SUBNET"`)

* `VPC_SECONDARY_SUBNET` (value: `"VPC_SECONDARY_SUBNET"`)




