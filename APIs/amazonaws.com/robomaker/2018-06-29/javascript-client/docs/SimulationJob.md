# AwsRoboMaker.SimulationJob

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
**vpcConfig** | [**SimulationJobVpcConfig**](SimulationJobVpcConfig.md) |  | [optional] 
**networkInterface** | [**SimulationJobNetworkInterface**](SimulationJobNetworkInterface.md) |  | [optional] 
**compute** | [**SimulationJobCompute**](SimulationJobCompute.md) |  | [optional] 


