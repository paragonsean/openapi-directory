

# CreateMediaCapturePipelineRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Source type from which the media artifacts are captured. A Chime SDK Meeting is the only supported source. |  |
|**sourceArn** | **String** | ARN of the source from which the media artifacts are captured. |  |
|**sinkType** | [**SinkTypeEnum**](#SinkTypeEnum) | Destination type to which the media artifacts are saved. You must use an S3 bucket. |  |
|**sinkArn** | **String** | The ARN of the sink type. |  |
|**clientRequestToken** | **String** | The unique identifier for the client request. The token makes the API request idempotent. Use a unique token for each media pipeline request. |  [optional] |
|**chimeSdkMeetingConfiguration** | [**CreateMediaCapturePipelineRequestChimeSdkMeetingConfiguration**](CreateMediaCapturePipelineRequestChimeSdkMeetingConfiguration.md) |  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | The tag key-value pairs. |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| CHIME_SDK_MEETING | &quot;ChimeSdkMeeting&quot; |



## Enum: SinkTypeEnum

| Name | Value |
|---- | -----|
| S3_BUCKET | &quot;S3Bucket&quot; |



