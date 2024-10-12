# AmazonChimeSdkMediaPipelines.CreateMediaInsightsPipelineConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mediaInsightsPipelineConfigurationName** | **String** | The name of the media insights pipeline configuration. | 
**resourceAccessRoleArn** | **String** | The ARN of the role used by the service to access Amazon Web Services resources, including &lt;code&gt;Transcribe&lt;/code&gt; and &lt;code&gt;Transcribe Call Analytics&lt;/code&gt;, on the caller’s behalf. | 
**realTimeAlertConfiguration** | [**CreateMediaInsightsPipelineConfigurationRequestRealTimeAlertConfiguration**](CreateMediaInsightsPipelineConfigurationRequestRealTimeAlertConfiguration.md) |  | [optional] 
**elements** | [**[MediaInsightsPipelineConfigurationElement]**](MediaInsightsPipelineConfigurationElement.md) | The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream. | 
**tags** | [**[Tag]**](Tag.md) | The tags assigned to the media insights pipeline configuration. | [optional] 
**clientRequestToken** | **String** | The unique identifier for the media insights pipeline configuration request. | [optional] 


