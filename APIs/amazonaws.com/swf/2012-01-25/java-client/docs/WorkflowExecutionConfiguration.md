

# WorkflowExecutionConfiguration

The configuration settings for a workflow execution including timeout values, tasklist etc. These configuration settings are determined from the defaults specified when registering the workflow type and those specified when starting the workflow execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**taskStartToCloseTimeout** | [**String**](String.md) |  |  |
|**executionStartToCloseTimeout** | [**String**](String.md) |  |  |
|**taskList** | [**WorkflowExecutionConfigurationTaskList**](WorkflowExecutionConfigurationTaskList.md) |  |  |
|**taskPriority** | [**String**](String.md) |  |  [optional] |
|**childPolicy** | [**ChildPolicy**](ChildPolicy.md) |  |  |
|**lambdaRole** | [**String**](String.md) |  |  [optional] |



