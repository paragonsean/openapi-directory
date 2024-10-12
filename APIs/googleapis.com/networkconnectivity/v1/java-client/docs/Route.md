

# Route

A route defines a path from VM instances within a spoke to a specific destination resource. Only VPC spokes have routes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time the route was created. |  [optional] [readonly] |
|**description** | **String** | An optional description of the route. |  [optional] |
|**ipCidrRange** | **String** | The destination IP address range. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |  [optional] |
|**location** | **String** | Output only. The location of the route. Uses the following form: \&quot;projects/{project}/locations/{location}\&quot; Example: projects/1234/locations/us-central1 |  [optional] [readonly] |
|**name** | **String** | Immutable. The name of the route. Route names must be unique. Route names use the following form: &#x60;projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}/routes/{route_id}&#x60; |  [optional] |
|**nextHopVpcNetwork** | [**NextHopVpcNetwork**](NextHopVpcNetwork.md) |  |  [optional] |
|**spoke** | **String** | Immutable. The spoke that this route leads to. Example: projects/12345/locations/global/spokes/SPOKE |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current lifecycle state of the route. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The route&#39;s type. Its type is determined by the properties of its IP address range. |  [optional] [readonly] |
|**uid** | **String** | Output only. The Google-generated UUID for the route. This value is unique across all Network Connectivity Center route resources. If a route is deleted and another with the same name is created, the new route is assigned a different &#x60;uid&#x60;. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time the route was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| ACCEPTING | &quot;ACCEPTING&quot; |
| REJECTING | &quot;REJECTING&quot; |
| UPDATING | &quot;UPDATING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| OBSOLETE | &quot;OBSOLETE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ROUTE_TYPE_UNSPECIFIED | &quot;ROUTE_TYPE_UNSPECIFIED&quot; |
| VPC_PRIMARY_SUBNET | &quot;VPC_PRIMARY_SUBNET&quot; |
| VPC_SECONDARY_SUBNET | &quot;VPC_SECONDARY_SUBNET&quot; |



