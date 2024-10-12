# AmazonChimeSdkMediaPipelines.CreateMediaInsightsPipelineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mediaInsightsPipelineConfigurationArn** | **String** | The ARN of the pipeline&#39;s configuration. | 
**kinesisVideoStreamSourceRuntimeConfiguration** | [**CreateMediaInsightsPipelineRequestKinesisVideoStreamSourceRuntimeConfiguration**](CreateMediaInsightsPipelineRequestKinesisVideoStreamSourceRuntimeConfiguration.md) |  | [optional] 
**mediaInsightsRuntimeMetadata** | **{String: String}** | The runtime metadata for the media insights pipeline. Consists of a key-value map of strings. | [optional] 
**kinesisVideoStreamRecordingSourceRuntimeConfiguration** | [**CreateMediaInsightsPipelineRequestKinesisVideoStreamRecordingSourceRuntimeConfiguration**](CreateMediaInsightsPipelineRequestKinesisVideoStreamRecordingSourceRuntimeConfiguration.md) |  | [optional] 
**s3RecordingSinkRuntimeConfiguration** | [**CreateMediaInsightsPipelineRequestS3RecordingSinkRuntimeConfiguration**](CreateMediaInsightsPipelineRequestS3RecordingSinkRuntimeConfiguration.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | The tags assigned to the media insights pipeline. | [optional] 
**clientRequestToken** | **String** | The unique identifier for the media insights pipeline request. | [optional] 


