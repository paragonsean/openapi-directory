

# AutoUserSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**elevationLevel** | **ElevationLevel** |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | pool - specifies that the task runs as the common auto user account which is created on every node in a pool. task - specifies that the service should create a new user for the task. The default value is task. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| TASK | &quot;Task&quot; |
| POOL | &quot;Pool&quot; |



