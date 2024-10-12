# ZapierNaturalLanguageActionsNlaApiBeta.ExecuteResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionUsed** | **String** | The name of the action that was executed. | 
**additionalResults** | **[Object]** | The rest of the full results. Always returns an array of objects | 
**assistantHint** | **String** | A hint for the assistant on what to do next. | [optional] 
**error** | **String** | The error message if the execution failed. | [optional] 
**id** | **String** | The id of the execution log. | 
**inputParams** | **Object** | The params we used / will use to execute the action. | 
**result** | **Object** | A trimmed down result of the first item of the full results. Ideal for humans and language models! | [optional] 
**resultFieldLabels** | **Object** | Human readable labels for some of the keys in the result. | [optional] 
**reviewUrl** | **String** | The URL to run the action or review the AI choices the AI made for input_params given instructions. | 
**status** | **String** | The status of the execution. | [optional] [default to &#39;success&#39;]



## Enum: StatusEnum


* `success` (value: `"success"`)

* `error` (value: `"error"`)

* `empty` (value: `"empty"`)

* `preview` (value: `"preview"`)




