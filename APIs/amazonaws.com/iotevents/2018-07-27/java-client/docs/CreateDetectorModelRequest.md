

# CreateDetectorModelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detectorModelName** | **String** | The name of the detector model. |  |
|**detectorModelDefinition** | [**CreateDetectorModelRequestDetectorModelDefinition**](CreateDetectorModelRequestDetectorModelDefinition.md) |  |  |
|**detectorModelDescription** | **String** | A brief description of the detector model. |  [optional] |
|**key** | **String** | The input attribute key used to identify a device or system to create a detector (an instance of the detector model) and then to route each input received to the appropriate detector (instance). This parameter uses a JSON-path expression in the message payload of each input to specify the attribute-value pair that is used to identify the device associated with the input. |  [optional] |
|**roleArn** | **String** | The ARN of the role that grants permission to AWS IoT Events to perform its operations. |  |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | Metadata that can be used to manage the detector model. |  [optional] |
|**evaluationMethod** | [**EvaluationMethodEnum**](#EvaluationMethodEnum) | Information about the order in which events are evaluated and how actions are executed.  |  [optional] |



## Enum: EvaluationMethodEnum

| Name | Value |
|---- | -----|
| BATCH | &quot;BATCH&quot; |
| SERIAL | &quot;SERIAL&quot; |



