

# ApiPublicV1MaintenancemodeStartPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**names** | **List&lt;String&gt;** | Routing keys that maintenance mode state covers. An empty list indicates global maintenance mode |  [optional] |
|**purpose** | **String** | the reason for the maintenance mode |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ROUTING_KEYS | &quot;RoutingKeys&quot; |



