

# Hub

A Network Connectivity Center hub is a global management resource to which you attach spokes. A single hub can contain spokes from multiple regions. However, if any of a hub's spokes use the site-to-site data transfer feature, the resources associated with those spokes must all be in the same VPC network. Spokes that do not use site-to-site data transfer can be associated with any VPC network in your project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time the hub was created. |  [optional] [readonly] |
|**description** | **String** | An optional description of the hub. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |  [optional] |
|**name** | **String** | Immutable. The name of the hub. Hub names must be unique. They use the following form: &#x60;projects/{project_number}/locations/global/hubs/{hub_id}&#x60; |  [optional] |
|**routeTables** | **List&lt;String&gt;** | Output only. The route tables that belong to this hub. They use the following form: &#x60;projects/{project_number}/locations/global/hubs/{hub_id}/routeTables/{route_table_id}&#x60; This field is read-only. Network Connectivity Center automatically populates it based on the route tables nested under the hub. |  [optional] [readonly] |
|**routingVpcs** | [**List&lt;RoutingVPC&gt;**](RoutingVPC.md) | The VPC networks associated with this hub&#39;s spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub. |  [optional] |
|**spokeSummary** | [**SpokeSummary**](SpokeSummary.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current lifecycle state of this hub. |  [optional] [readonly] |
|**uniqueId** | **String** | Output only. The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time the hub was last updated. |  [optional] [readonly] |



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



