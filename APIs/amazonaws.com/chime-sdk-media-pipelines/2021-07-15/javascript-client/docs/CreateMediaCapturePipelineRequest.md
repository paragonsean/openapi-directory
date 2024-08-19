# AmazonChimeSdkMediaPipelines.CreateMediaCapturePipelineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sourceType** | **String** | Source type from which the media artifacts are captured. A Chime SDK Meeting is the only supported source. | 
**sourceArn** | **String** | ARN of the source from which the media artifacts are captured. | 
**sinkType** | **String** | Destination type to which the media artifacts are saved. You must use an S3 bucket. | 
**sinkArn** | **String** | The ARN of the sink type. | 
**clientRequestToken** | **String** | The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media pipeline request. | [optional] 
**chimeSdkMeetingConfiguration** | [**CreateMediaCapturePipelineRequestChimeSdkMeetingConfiguration**](CreateMediaCapturePipelineRequestChimeSdkMeetingConfiguration.md) |  | [optional] 
**tags** | [**[Tag]**](Tag.md) | The tag key-value pairs. | [optional] 



## Enum: SourceTypeEnum


* `ChimeSdkMeeting` (value: `"ChimeSdkMeeting"`)





## Enum: SinkTypeEnum


* `S3Bucket` (value: `"S3Bucket"`)




