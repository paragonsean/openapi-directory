

# AnswerSummary

An answer summary of a lens review in a workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**questionId** | **String** | The ID of the question. |  [optional] |
|**pillarId** | **String** | &lt;p&gt;The ID used to identify a pillar, for example, &lt;code&gt;security&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;A pillar is identified by its &lt;a&gt;PillarReviewSummary$PillarId&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**questionTitle** | **String** | The title of the question. |  [optional] |
|**choices** | [**List&lt;Choice&gt;**](Choice.md) | List of choices available for a question. |  [optional] |
|**selectedChoices** | **List&lt;String&gt;** | &lt;p&gt;List of selected choice IDs in a question answer.&lt;/p&gt; &lt;p&gt;The values entered replace the previously selected choices.&lt;/p&gt; |  [optional] |
|**choiceAnswerSummaries** | [**List**](List.md) |  |  [optional] |
|**isApplicable** | **Boolean** | Defines whether this question is applicable to a lens review. |  [optional] |
|**risk** | **Risk** |  |  [optional] |
|**reason** | [**AnswerReason**](AnswerReason.md) |  |  [optional] |
|**questionType** | [**QuestionType**](QuestionType.md) |  |  [optional] |



