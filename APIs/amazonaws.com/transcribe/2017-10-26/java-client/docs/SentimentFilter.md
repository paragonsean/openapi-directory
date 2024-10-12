

# SentimentFilter

<p>Flag the presence or absence of specific sentiments detected in your Call Analytics transcription output.</p> <p>Rules using <code>SentimentFilter</code> are designed to match:</p> <ul> <li> <p>The presence or absence of a positive sentiment felt by the customer, agent, or both at specified points in the call</p> </li> <li> <p>The presence or absence of a negative sentiment felt by the customer, agent, or both at specified points in the call</p> </li> <li> <p>The presence or absence of a neutral sentiment felt by the customer, agent, or both at specified points in the call</p> </li> <li> <p>The presence or absence of a mixed sentiment felt by the customer, the agent, or both at specified points in the call</p> </li> </ul> <p>See <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html#tca-rules-batch\">Rule criteria for post-call categories</a> for usage examples.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sentiments** | [**List**](List.md) |  |  |
|**absoluteTimeRange** | [**SentimentFilterAbsoluteTimeRange**](SentimentFilterAbsoluteTimeRange.md) |  |  [optional] |
|**relativeTimeRange** | [**SentimentFilterRelativeTimeRange**](SentimentFilterRelativeTimeRange.md) |  |  [optional] |
|**participantRole** | [**ParticipantRole**](ParticipantRole.md) |  |  [optional] |
|**negate** | [**Boolean**](Boolean.md) |  |  [optional] |



