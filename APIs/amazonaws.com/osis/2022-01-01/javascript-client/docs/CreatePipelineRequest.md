# AmazonOpenSearchIngestion.CreatePipelineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipelineName** | **String** | The name of the OpenSearch Ingestion pipeline to create. Pipeline names are unique across the pipelines owned by an account within an Amazon Web Services Region. | 
**minUnits** | **Number** | The minimum pipeline capacity, in Ingestion Compute Units (ICUs). | 
**maxUnits** | **Number** | The maximum pipeline capacity, in Ingestion Compute Units (ICUs). | 
**pipelineConfigurationBody** | **String** | The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with &lt;code&gt;\\n&lt;/code&gt;. | 
**logPublishingOptions** | [**CreatePipelineRequestLogPublishingOptions**](CreatePipelineRequestLogPublishingOptions.md) |  | [optional] 
**vpcOptions** | [**CreatePipelineRequestVpcOptions**](CreatePipelineRequestVpcOptions.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | List of tags to add to the pipeline upon creation. | [optional] 


