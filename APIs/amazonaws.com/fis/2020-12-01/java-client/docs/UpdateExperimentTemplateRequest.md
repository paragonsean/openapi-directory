

# UpdateExperimentTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description for the template. |  [optional] |
|**stopConditions** | [**List&lt;UpdateExperimentTemplateStopConditionInput&gt;**](UpdateExperimentTemplateStopConditionInput.md) | The stop conditions for the experiment. |  [optional] |
|**targets** | [**Map&lt;String, UpdateExperimentTemplateTargetInput&gt;**](UpdateExperimentTemplateTargetInput.md) | The targets for the experiment. |  [optional] |
|**actions** | [**Map&lt;String, UpdateExperimentTemplateActionInputItem&gt;**](UpdateExperimentTemplateActionInputItem.md) | The actions for the experiment. |  [optional] |
|**roleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf. |  [optional] |
|**logConfiguration** | [**CreateExperimentTemplateRequestLogConfiguration**](CreateExperimentTemplateRequestLogConfiguration.md) |  |  [optional] |



