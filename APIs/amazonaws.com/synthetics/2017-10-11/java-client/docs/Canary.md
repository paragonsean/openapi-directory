

# Canary

This structure contains all information about one canary in your account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**code** | [**CanaryCodeOutput**](CanaryCodeOutput.md) |  |  [optional] |
|**executionRoleArn** | [**String**](String.md) |  |  [optional] |
|**schedule** | [**CanarySchedule**](CanarySchedule.md) |  |  [optional] |
|**runConfig** | [**CanaryRunConfigOutput**](CanaryRunConfigOutput.md) |  |  [optional] |
|**successRetentionPeriodInDays** | [**Integer**](Integer.md) |  |  [optional] |
|**failureRetentionPeriodInDays** | [**Integer**](Integer.md) |  |  [optional] |
|**status** | [**CanaryStatus**](CanaryStatus.md) |  |  [optional] |
|**timeline** | [**CanaryTimeline**](CanaryTimeline.md) |  |  [optional] |
|**artifactS3Location** | [**String**](String.md) |  |  [optional] |
|**engineArn** | [**String**](String.md) |  |  [optional] |
|**runtimeVersion** | [**String**](String.md) |  |  [optional] |
|**vpcConfig** | [**VpcConfigOutput**](VpcConfigOutput.md) |  |  [optional] |
|**visualReference** | [**CanaryVisualReference**](CanaryVisualReference.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**artifactConfig** | [**CanaryArtifactConfig**](CanaryArtifactConfig.md) |  |  [optional] |



