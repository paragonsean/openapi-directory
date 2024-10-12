# AwsWellArchitectedTool.UpdateAnswerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectedChoices** | **[String]** | &lt;p&gt;List of selected choice IDs in a question answer.&lt;/p&gt; &lt;p&gt;The values entered replace the previously selected choices.&lt;/p&gt; | [optional] 
**choiceUpdates** | [**{String: ChoiceUpdate}**](ChoiceUpdate.md) | A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated. | [optional] 
**notes** | **String** | The notes associated with the workload. | [optional] 
**isApplicable** | **Boolean** | Defines whether this question is applicable to a lens review. | [optional] 
**reason** | **String** | The reason why a question is not applicable to your workload. | [optional] 



## Enum: ReasonEnum


* `OUT_OF_SCOPE` (value: `"OUT_OF_SCOPE"`)

* `BUSINESS_PRIORITIES` (value: `"BUSINESS_PRIORITIES"`)

* `ARCHITECTURE_CONSTRAINTS` (value: `"ARCHITECTURE_CONSTRAINTS"`)

* `OTHER` (value: `"OTHER"`)

* `NONE` (value: `"NONE"`)




