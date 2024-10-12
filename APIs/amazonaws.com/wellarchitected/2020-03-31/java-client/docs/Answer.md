

# Answer

An answer of the question.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**questionId** | **String** | The ID of the question. |  [optional] |
|**pillarId** | **String** | &lt;p&gt;The ID used to identify a pillar, for example, &lt;code&gt;security&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A pillar is identified by its &lt;a&gt;PillarReviewSummary$PillarId&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**questionTitle** | **String** | The title of the question. |  [optional] |
|**questionDescription** | **String** | The description of the question. |  [optional] |
|**improvementPlanUrl** | **String** | &lt;p&gt;The improvement plan URL for a question in an Amazon Web Services official lenses.&lt;/p&gt; &lt;p&gt;This value is only available if the question has been answered.&lt;/p&gt; &lt;p&gt;This value does not apply to custom lenses.&lt;/p&gt; |  [optional] |
|**helpfulResourceUrl** | **String** | &lt;p&gt;The helpful resource URL.&lt;/p&gt; &lt;p&gt;For Amazon Web Services official lenses, this is the helpful resource URL for a question or choice.&lt;/p&gt; &lt;p&gt;For custom lenses, this is the helpful resource URL for a question and is only provided if &lt;code&gt;HelpfulResourceDisplayText&lt;/code&gt; was specified for the question.&lt;/p&gt; |  [optional] |
|**helpfulResourceDisplayText** | [**String**](String.md) |  |  [optional] |
|**choices** | [**List&lt;Choice&gt;**](Choice.md) | List of choices available for a question. |  [optional] |
|**selectedChoices** | **List&lt;String&gt;** | &lt;p&gt;List of selected choice IDs in a question answer.&lt;/p&gt; &lt;p&gt;The values entered replace the previously selected choices.&lt;/p&gt; |  [optional] |
|**choiceAnswers** | [**List**](List.md) |  |  [optional] |
|**isApplicable** | **Boolean** | Defines whether this question is applicable to a lens review. |  [optional] |
|**risk** | **Risk** |  |  [optional] |
|**notes** | **String** | The notes associated with the workload. |  [optional] |
|**reason** | [**AnswerReason**](AnswerReason.md) |  |  [optional] |



