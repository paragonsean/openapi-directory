

# RouteTable


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time the route table was created. |  [optional] [readonly] |
|**description** | **String** | An optional description of the route table. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |  [optional] |
|**name** | **String** | Immutable. The name of the route table. Route table names must be unique. They use the following form: &#x60;projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}&#x60; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current lifecycle state of this route table. |  [optional] [readonly] |
|**uid** | **String** | Output only. The Google-generated UUID for the route table. This value is unique across all route table resources. If a route table is deleted and another with the same name is created, the new route table is assigned a different &#x60;uid&#x60;. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time the route table was last updated. |  [optional] [readonly] |



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



