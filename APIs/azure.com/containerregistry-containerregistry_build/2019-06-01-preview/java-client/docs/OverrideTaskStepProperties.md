

# OverrideTaskStepProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | [**List&lt;Argument&gt;**](Argument.md) | Gets or sets the collection of override arguments to be used when  executing a build step. |  [optional] |
|**contextPath** | **String** | The source context against which run has to be queued. |  [optional] |
|**_file** | **String** | The file against which run has to be queued. |  [optional] |
|**target** | **String** | The name of the target build stage for the docker build. |  [optional] |
|**updateTriggerToken** | **String** | Base64 encoded update trigger token that will be attached with the base image trigger webhook. |  [optional] |
|**values** | [**List&lt;SetValue&gt;**](SetValue.md) | The collection of overridable values that can be passed when running a Task. |  [optional] |



