# AwsRoboMaker.CreateSimulationJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **String** |  | [optional] 
**status** | [**SimulationJobStatus**](SimulationJobStatus.md) |  | [optional] 
**lastStartedAt** | **Date** |  | [optional] 
**lastUpdatedAt** | **Date** |  | [optional] 
**failureBehavior** | [**FailureBehavior**](FailureBehavior.md) |  | [optional] 
**failureCode** | [**SimulationJobErrorCode**](SimulationJobErrorCode.md) |  | [optional] 
**clientRequestToken** | **String** |  | [optional] 
**outputLocation** | [**CreateSimulationJobResponseOutputLocation**](CreateSimulationJobResponseOutputLocation.md) |  | [optional] 
**loggingConfig** | [**CreateSimulationJobResponseLoggingConfig**](CreateSimulationJobResponseLoggingConfig.md) |  | [optional] 
**maxJobDurationInSeconds** | **Number** |  | [optional] 
**simulationTimeMillis** | **Number** |  | [optional] 
**iamRole** | **String** |  | [optional] 
**robotApplications** | **Array** |  | [optional] 
**simulationApplications** | **Array** |  | [optional] 
**dataSources** | **Array** |  | [optional] 
**tags** | **Object** |  | [optional] 
**vpcConfig** | [**CreateSimulationJobResponseVpcConfig**](CreateSimulationJobResponseVpcConfig.md) |  | [optional] 
**compute** | [**CreateSimulationJobResponseCompute**](CreateSimulationJobResponseCompute.md) |  | [optional] 


