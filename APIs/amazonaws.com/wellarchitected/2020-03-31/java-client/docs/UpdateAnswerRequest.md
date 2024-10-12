

# UpdateAnswerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**selectedChoices** | **List&lt;String&gt;** | &lt;p&gt;List of selected choice IDs in a question answer.&lt;/p&gt; &lt;p&gt;The values entered replace the previously selected choices.&lt;/p&gt; |  [optional] |
|**choiceUpdates** | [**Map&lt;String, ChoiceUpdate&gt;**](ChoiceUpdate.md) | A list of choices to update on a question in your workload. The String key corresponds to the choice ID to be updated. |  [optional] |
|**notes** | **String** | The notes associated with the workload. |  [optional] |
|**isApplicable** | **Boolean** | Defines whether this question is applicable to a lens review. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason why a question is not applicable to your workload. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| OUT_OF_SCOPE | &quot;OUT_OF_SCOPE&quot; |
| BUSINESS_PRIORITIES | &quot;BUSINESS_PRIORITIES&quot; |
| ARCHITECTURE_CONSTRAINTS | &quot;ARCHITECTURE_CONSTRAINTS&quot; |
| OTHER | &quot;OTHER&quot; |
| NONE | &quot;NONE&quot; |



