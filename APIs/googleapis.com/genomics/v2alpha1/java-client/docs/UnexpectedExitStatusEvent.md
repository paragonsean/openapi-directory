

# UnexpectedExitStatusEvent

An event generated when the execution of a container results in a non-zero exit status that was not otherwise ignored. Execution will continue, but only actions that are flagged as `ALWAYS_RUN` will be executed. Other actions will be skipped.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionId** | **Integer** | The numeric ID of the action that started the container. |  [optional] |
|**exitStatus** | **Integer** | The exit status of the container. |  [optional] |



