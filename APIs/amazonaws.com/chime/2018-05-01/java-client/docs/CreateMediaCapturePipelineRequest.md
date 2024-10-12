

# CreateMediaCapturePipelineRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Source type from which the media artifacts will be captured. A Chime SDK Meeting is the only supported source. |  |
|**sourceArn** | **String** | ARN of the source from which the media artifacts are captured. |  |
|**sinkType** | [**SinkTypeEnum**](#SinkTypeEnum) | Destination type to which the media artifacts are saved. You must use an S3 bucket.  |  |
|**sinkArn** | **String** | The ARN of the sink type. |  |
|**clientRequestToken** | **String** | The unique identifier for the client request. The token makes the API request idempotent. Use a different token for different media pipeline requests. |  [optional] |
|**chimeSdkMeetingConfiguration** | [**CreateMediaCapturePipelineRequestChimeSdkMeetingConfiguration**](CreateMediaCapturePipelineRequestChimeSdkMeetingConfiguration.md) |  |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| CHIME_SDK_MEETING | &quot;ChimeSdkMeeting&quot; |



## Enum: SinkTypeEnum

| Name | Value |
|---- | -----|
| S3_BUCKET | &quot;S3Bucket&quot; |



