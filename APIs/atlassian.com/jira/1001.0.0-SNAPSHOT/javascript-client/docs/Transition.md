# TheJiraCloudPlatformRestApi.Transition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the transition. | 
**from** | **[String]** | The statuses the transition can start from. | 
**id** | **String** | The ID of the transition. | 
**name** | **String** | The name of the transition. | 
**properties** | **{String: Object}** | The properties of the transition. | [optional] 
**rules** | [**WorkflowRules**](WorkflowRules.md) |  | [optional] 
**screen** | [**TransitionScreenDetails**](TransitionScreenDetails.md) |  | [optional] 
**to** | **String** | The status the transition goes to. | 
**type** | **String** | The type of the transition. | 



## Enum: TypeEnum


* `global` (value: `"global"`)

* `initial` (value: `"initial"`)

* `directed` (value: `"directed"`)




