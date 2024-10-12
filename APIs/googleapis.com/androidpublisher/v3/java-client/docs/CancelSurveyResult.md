

# CancelSurveyResult

Result of the cancel survey when the subscription was canceled by the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason the user selected in the cancel survey. |  [optional] |
|**reasonUserInput** | **String** | Only set for CANCEL_SURVEY_REASON_OTHERS. This is the user&#39;s freeform response to the survey. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CANCEL_SURVEY_REASON_UNSPECIFIED&quot; |
| NOT_ENOUGH_USAGE | &quot;CANCEL_SURVEY_REASON_NOT_ENOUGH_USAGE&quot; |
| TECHNICAL_ISSUES | &quot;CANCEL_SURVEY_REASON_TECHNICAL_ISSUES&quot; |
| COST_RELATED | &quot;CANCEL_SURVEY_REASON_COST_RELATED&quot; |
| FOUND_BETTER_APP | &quot;CANCEL_SURVEY_REASON_FOUND_BETTER_APP&quot; |
| OTHERS | &quot;CANCEL_SURVEY_REASON_OTHERS&quot; |



