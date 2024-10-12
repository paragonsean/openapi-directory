

# DebugRuleConfiguration

Configuration information for SageMaker Debugger rules for debugging. To learn more about how to configure the <code>DebugRuleConfiguration</code> parameter, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html\">Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleConfigurationName** | [**String**](String.md) |  |  |
|**localPath** | [**String**](String.md) |  |  [optional] |
|**s3OutputPath** | [**String**](String.md) |  |  [optional] |
|**ruleEvaluatorImage** | [**String**](String.md) |  |  |
|**instanceType** | [**ProcessingInstanceType**](ProcessingInstanceType.md) |  |  [optional] |
|**volumeSizeInGB** | [**Integer**](Integer.md) |  |  [optional] |
|**ruleParameters** | [**Map**](Map.md) |  |  [optional] |



