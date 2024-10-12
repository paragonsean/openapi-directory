

# InferenceExecutionSummary

Contains information about the specific inference execution, including input and output data configuration, inference scheduling information, status, and so on. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**modelName** | [**String**](String.md) |  |  [optional] |
|**modelArn** | [**String**](String.md) |  |  [optional] |
|**inferenceSchedulerName** | [**String**](String.md) |  |  [optional] |
|**inferenceSchedulerArn** | [**String**](String.md) |  |  [optional] |
|**scheduledStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**dataStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**dataEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**dataInputConfiguration** | [**DescribeInferenceSchedulerResponseDataInputConfiguration**](DescribeInferenceSchedulerResponseDataInputConfiguration.md) |  |  [optional] |
|**dataOutputConfiguration** | [**InferenceExecutionSummaryDataOutputConfiguration**](InferenceExecutionSummaryDataOutputConfiguration.md) |  |  [optional] |
|**customerResultObject** | [**InferenceExecutionSummaryCustomerResultObject**](InferenceExecutionSummaryCustomerResultObject.md) |  |  [optional] |
|**status** | [**InferenceExecutionStatus**](InferenceExecutionStatus.md) |  |  [optional] |
|**failedReason** | [**String**](String.md) |  |  [optional] |



