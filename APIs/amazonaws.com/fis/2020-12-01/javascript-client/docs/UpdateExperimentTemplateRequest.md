# AwsFaultInjectionSimulator.UpdateExperimentTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description for the template. | [optional] 
**stopConditions** | [**[UpdateExperimentTemplateStopConditionInput]**](UpdateExperimentTemplateStopConditionInput.md) | The stop conditions for the experiment. | [optional] 
**targets** | [**{String: UpdateExperimentTemplateTargetInput}**](UpdateExperimentTemplateTargetInput.md) | The targets for the experiment. | [optional] 
**actions** | [**{String: UpdateExperimentTemplateActionInputItem}**](UpdateExperimentTemplateActionInputItem.md) | The actions for the experiment. | [optional] 
**roleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf. | [optional] 
**logConfiguration** | [**CreateExperimentTemplateRequestLogConfiguration**](CreateExperimentTemplateRequestLogConfiguration.md) |  | [optional] 


