

# DescribeSimulationJobResponse


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
|**vpcConfig** | [**DescribeSimulationJobResponseVpcConfig**](DescribeSimulationJobResponseVpcConfig.md) |  |  [optional] |
|**networkInterface** | [**DescribeSimulationJobResponseNetworkInterface**](DescribeSimulationJobResponseNetworkInterface.md) |  |  [optional] |
|**compute** | [**CreateSimulationJobResponseCompute**](CreateSimulationJobResponseCompute.md) |  |  [optional] |



