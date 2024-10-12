# AmazonOpenSearchIngestion.UpdatePipelineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minUnits** | **Number** | The minimum pipeline capacity, in Ingestion Compute Units (ICUs). | [optional] 
**maxUnits** | **Number** | The maximum pipeline capacity, in Ingestion Compute Units (ICUs) | [optional] 
**pipelineConfigurationBody** | **String** | The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with &lt;code&gt;\\n&lt;/code&gt;. | [optional] 
**logPublishingOptions** | [**CreatePipelineRequestLogPublishingOptions**](CreatePipelineRequestLogPublishingOptions.md) |  | [optional] 


