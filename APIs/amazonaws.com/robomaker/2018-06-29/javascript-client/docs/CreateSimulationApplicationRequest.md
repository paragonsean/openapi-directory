# AwsRoboMaker.CreateSimulationApplicationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the simulation application. | 
**sources** | [**[SourceConfig]**](SourceConfig.md) | The sources of the simulation application. | [optional] 
**simulationSoftwareSuite** | [**CreateSimulationApplicationRequestSimulationSoftwareSuite**](CreateSimulationApplicationRequestSimulationSoftwareSuite.md) |  | 
**robotSoftwareSuite** | [**CreateRobotApplicationRequestRobotSoftwareSuite**](CreateRobotApplicationRequestRobotSoftwareSuite.md) |  | 
**renderingEngine** | [**CreateSimulationApplicationRequestRenderingEngine**](CreateSimulationApplicationRequestRenderingEngine.md) |  | [optional] 
**tags** | **{String: String}** | A map that contains tag keys and tag values that are attached to the simulation application. | [optional] 
**environment** | [**CreateRobotApplicationRequestEnvironment**](CreateRobotApplicationRequestEnvironment.md) |  | [optional] 


