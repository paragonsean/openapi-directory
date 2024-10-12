

# GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCase

Each case has a Boolean condition. When it is evaluated to be True, the corresponding messages will be selected and evaluated recursively.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseContent** | [**List&lt;GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContent&gt;**](GoogleCloudDialogflowCxV3FulfillmentConditionalCasesCaseCaseContent.md) | A list of case content. |  [optional] |
|**condition** | **String** | The condition to activate and select this case. Empty means the condition is always true. The condition is evaluated against form parameters or session parameters. See the [conditions reference](https://cloud.google.com/dialogflow/cx/docs/reference/condition). |  [optional] |



