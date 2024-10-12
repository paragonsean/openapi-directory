

# SimulationJob

Information about a simulation job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**SimulationJobStatus**](SimulationJobStatus.md) |  |  [optional] |
|**lastStartedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**failureBehavior** | [**FailureBehavior**](FailureBehavior.md) |  |  [optional] |
|**failureCode** | [**SimulationJobErrorCode**](SimulationJobErrorCode.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**clientRequestToken** | [**String**](String.md) |  |  [optional] |
|**outputLocation** | [**DescribeSimulationJobResponseOutputLocation**](DescribeSimulationJobResponseOutputLocation.md) |  |  [optional] |
|**loggingConfig** | [**CreateSimulationJobResponseLoggingConfig**](CreateSimulationJobResponseLoggingConfig.md) |  |  [optional] |
|**maxJobDurationInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**simulationTimeMillis** | [**Integer**](Integer.md) |  |  [optional] |
|**iamRole** | [**String**](String.md) |  |  [optional] |
|**robotApplications** | [**List**](List.md) |  |  [optional] |
|**simulationApplications** | [**List**](List.md) |  |  [optional] |
|**dataSources** | [**List**](List.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**vpcConfig** | [**SimulationJobVpcConfig**](SimulationJobVpcConfig.md) |  |  [optional] |
|**networkInterface** | [**SimulationJobNetworkInterface**](SimulationJobNetworkInterface.md) |  |  [optional] |
|**compute** | [**SimulationJobCompute**](SimulationJobCompute.md) |  |  [optional] |



