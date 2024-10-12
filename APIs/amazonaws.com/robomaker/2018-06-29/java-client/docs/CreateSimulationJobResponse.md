

# CreateSimulationJobResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**status** | [**SimulationJobStatus**](SimulationJobStatus.md) |  |  [optional] |
|**lastStartedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**failureBehavior** | [**FailureBehavior**](FailureBehavior.md) |  |  [optional] |
|**failureCode** | [**SimulationJobErrorCode**](SimulationJobErrorCode.md) |  |  [optional] |
|**clientRequestToken** | [**String**](String.md) |  |  [optional] |
|**outputLocation** | [**CreateSimulationJobResponseOutputLocation**](CreateSimulationJobResponseOutputLocation.md) |  |  [optional] |
|**loggingConfig** | [**CreateSimulationJobResponseLoggingConfig**](CreateSimulationJobResponseLoggingConfig.md) |  |  [optional] |
|**maxJobDurationInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**simulationTimeMillis** | [**Integer**](Integer.md) |  |  [optional] |
|**iamRole** | [**String**](String.md) |  |  [optional] |
|**robotApplications** | [**List**](List.md) |  |  [optional] |
|**simulationApplications** | [**List**](List.md) |  |  [optional] |
|**dataSources** | [**List**](List.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**vpcConfig** | [**CreateSimulationJobResponseVpcConfig**](CreateSimulationJobResponseVpcConfig.md) |  |  [optional] |
|**compute** | [**CreateSimulationJobResponseCompute**](CreateSimulationJobResponseCompute.md) |  |  [optional] |



