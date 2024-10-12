# ContainerAnalysisApi.Command

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **[String]** | Command-line arguments used when executing this Command. | [optional] 
**dir** | **String** | Working directory (relative to project source root) used when running this Command. | [optional] 
**env** | **[String]** | Environment variables set before running this Command. | [optional] 
**id** | **String** | Optional unique identifier for this Command, used in wait_for to reference this Command as a dependency. | [optional] 
**name** | **String** | Name of the command, as presented on the command line, or if the command is packaged as a Docker container, as presented to &#x60;docker pull&#x60;. | [optional] 
**waitFor** | **[String]** | The ID(s) of the Command(s) that this Command depends on. | [optional] 


