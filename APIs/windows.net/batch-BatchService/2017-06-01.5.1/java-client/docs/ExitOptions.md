

# ExitOptions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependencyAction** | [**DependencyActionEnum**](#DependencyActionEnum) | Values are:   satisfy - Satisfy the task&#39;s dependencies.  block - Block the task&#39;s dependencies.   The default is &#39;satisfy&#39; for exit code 0, and &#39;block&#39; for all other exit conditions. If the job&#39;s usesTaskDependencies property is set to false, then specifying the dependencyAction property returns an error and the add task request fails with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400  (Bad Request). |  [optional] |
|**jobAction** | [**JobActionEnum**](#JobActionEnum) | Values are:   none - Take no action.  disable - Disable the job. This is equivalent to calling the disable job API, with a disableTasks value of requeue.  terminate - Terminate the job. The terminateReason in the job&#39;s executionInfo is set to \&quot;TaskFailed\&quot;. The default is none for exit code 0 and terminate for all other exit conditions.   If the job&#39;s onTaskFailed property is noAction, then specifying this property returns an error and the add task request fails with an invalid property value error; if you are calling the REST API directly, the HTTP status code is 400 (Bad Request). |  [optional] |



## Enum: DependencyActionEnum

| Name | Value |
|---- | -----|
| SATISFY | &quot;satisfy&quot; |
| BLOCK | &quot;block&quot; |



## Enum: JobActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| DISABLE | &quot;disable&quot; |
| TERMINATE | &quot;terminate&quot; |



