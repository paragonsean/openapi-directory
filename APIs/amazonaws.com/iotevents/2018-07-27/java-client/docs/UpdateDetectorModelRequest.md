

# UpdateDetectorModelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detectorModelDefinition** | [**CreateDetectorModelRequestDetectorModelDefinition**](CreateDetectorModelRequestDetectorModelDefinition.md) |  |  |
|**detectorModelDescription** | **String** | A brief description of the detector model. |  [optional] |
|**roleArn** | **String** | The ARN of the role that grants permission to AWS IoT Events to perform its operations. |  |
|**evaluationMethod** | [**EvaluationMethodEnum**](#EvaluationMethodEnum) | Information about the order in which events are evaluated and how actions are executed.  |  [optional] |



## Enum: EvaluationMethodEnum

| Name | Value |
|---- | -----|
| BATCH | &quot;BATCH&quot; |
| SERIAL | &quot;SERIAL&quot; |



