# AwsRoboMaker.DescribeSimulationJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**status** | [**SimulationJobStatus**](SimulationJobStatus.md) |  | [optional] 
**lastStartedAt** | **Date** |  | [optional] 
**lastUpdatedAt** | **Date** |  | [optional] 
**failureBehavior** | [**FailureBehavior**](FailureBehavior.md) |  | [optional] 
**failureCode** | [**SimulationJobErrorCode**](SimulationJobErrorCode.md) |  | [optional] 
**failureReason** | **String** |  | [optional] 
**clientRequestToken** | **String** |  | [optional] 
**outputLocation** | [**DescribeSimulationJobResponseOutputLocation**](DescribeSimulationJobResponseOutputLocation.md) |  | [optional] 
**loggingConfig** | [**CreateSimulationJobResponseLoggingConfig**](CreateSimulationJobResponseLoggingConfig.md) |  | [optional] 
**maxJobDurationInSeconds** | **Number** |  | [optional] 
**simulationTimeMillis** | **Number** |  | [optional] 
**iamRole** | **String** |  | [optional] 
**robotApplications** | **Array** |  | [optional] 
**simulationApplications** | **Array** |  | [optional] 
**dataSources** | **Array** |  | [optional] 
**tags** | **Object** |  | [optional] 
**vpcConfig** | [**DescribeSimulationJobResponseVpcConfig**](DescribeSimulationJobResponseVpcConfig.md) |  | [optional] 
**networkInterface** | [**DescribeSimulationJobResponseNetworkInterface**](DescribeSimulationJobResponseNetworkInterface.md) |  | [optional] 
**compute** | [**CreateSimulationJobResponseCompute**](CreateSimulationJobResponseCompute.md) |  | [optional] 


