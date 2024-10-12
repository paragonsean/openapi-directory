

# PlacementGroup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**id** | **Integer** | ID of the Resource |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**name** | **String** | Name of the Resource. Must be unique per Project. |  |
|**servers** | **List&lt;Integer&gt;** | Array of IDs of Servers that are part of this Placement Group |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Placement Group |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SPREAD | &quot;spread&quot; |



