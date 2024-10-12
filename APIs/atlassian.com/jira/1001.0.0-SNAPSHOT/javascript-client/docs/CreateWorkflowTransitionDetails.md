# TheJiraCloudPlatformRestApi.CreateWorkflowTransitionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the transition. The maximum length is 1000 characters. | [optional] 
**from** | **[String]** | The statuses the transition can start from. | [optional] 
**name** | **String** | The name of the transition. The maximum length is 60 characters. | 
**properties** | **{String: String}** | The properties of the transition. | [optional] 
**rules** | [**CreateWorkflowTransitionRulesDetails**](CreateWorkflowTransitionRulesDetails.md) | The rules of the transition. | [optional] 
**screen** | [**CreateWorkflowTransitionScreenDetails**](CreateWorkflowTransitionScreenDetails.md) | The screen of the transition. | [optional] 
**to** | **String** | The status the transition goes to. | 
**type** | **String** | The type of the transition. | 



## Enum: TypeEnum


* `global` (value: `"global"`)

* `initial` (value: `"initial"`)

* `directed` (value: `"directed"`)




