

# ContainerPropertiesInstanceView

The instance view of the container instance. Only valid in response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentState** | [**ContainerState**](ContainerState.md) |  |  [optional] |
|**events** | [**List&lt;Event&gt;**](Event.md) | The events of the container instance. |  [optional] [readonly] |
|**previousState** | [**ContainerState**](ContainerState.md) |  |  [optional] |
|**restartCount** | **Integer** | The number of times that the container instance has been restarted. |  [optional] [readonly] |



