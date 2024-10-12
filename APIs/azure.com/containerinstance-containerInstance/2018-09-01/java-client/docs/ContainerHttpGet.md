

# ContainerHttpGet

The container Http Get settings, for liveness or readiness probe

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**path** | **String** | The path to probe. |  [optional] |
|**port** | **Integer** | The port number to probe. |  |
|**scheme** | [**SchemeEnum**](#SchemeEnum) | The scheme. |  [optional] |



## Enum: SchemeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |



