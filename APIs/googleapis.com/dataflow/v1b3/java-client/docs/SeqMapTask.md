

# SeqMapTask

Describes a particular function to invoke.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputs** | [**List&lt;SideInputInfo&gt;**](SideInputInfo.md) | Information about each of the inputs. |  [optional] |
|**name** | **String** | The user-provided name of the SeqDo operation. |  [optional] |
|**outputInfos** | [**List&lt;SeqMapTaskOutputInfo&gt;**](SeqMapTaskOutputInfo.md) | Information about each of the outputs. |  [optional] |
|**stageName** | **String** | System-defined name of the stage containing the SeqDo operation. Unique across the workflow. |  [optional] |
|**systemName** | **String** | System-defined name of the SeqDo operation. Unique across the workflow. |  [optional] |
|**userFn** | **Map&lt;String, Object&gt;** | The user function to invoke. |  [optional] |



