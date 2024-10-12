

# Pipeline

Specifies a series of actions to execute, expressed as Docker containers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;Action&gt;**](Action.md) | The list of actions to execute, in the order they are specified. |  [optional] |
|**encryptedEnvironment** | [**Secret**](Secret.md) |  |  [optional] |
|**environment** | **Map&lt;String, String&gt;** | The environment to pass into every action. Each action can also specify additional environment variables but cannot delete an entry from this map (though they can overwrite it with a different value). |  [optional] |
|**resources** | [**Resources**](Resources.md) |  |  [optional] |
|**timeout** | **String** | The maximum amount of time to give the pipeline to complete. This includes the time spent waiting for a worker to be allocated. If the pipeline fails to complete before the timeout, it will be cancelled and the error code will be set to DEADLINE_EXCEEDED. If unspecified, it will default to 7 days. |  [optional] |



