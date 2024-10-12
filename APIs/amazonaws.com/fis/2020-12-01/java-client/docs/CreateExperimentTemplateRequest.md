

# CreateExperimentTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  |
|**description** | **String** | A description for the experiment template. |  |
|**stopConditions** | [**List&lt;CreateExperimentTemplateStopConditionInput&gt;**](CreateExperimentTemplateStopConditionInput.md) | The stop conditions. |  |
|**targets** | [**Map&lt;String, CreateExperimentTemplateTargetInput&gt;**](CreateExperimentTemplateTargetInput.md) | The targets for the experiment. |  [optional] |
|**actions** | [**Map&lt;String, CreateExperimentTemplateActionInput&gt;**](CreateExperimentTemplateActionInput.md) | The actions for the experiment. |  |
|**roleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags to apply to the experiment template. |  [optional] |
|**logConfiguration** | [**CreateExperimentTemplateRequestLogConfiguration**](CreateExperimentTemplateRequestLogConfiguration.md) |  |  [optional] |



