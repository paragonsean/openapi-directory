

# InterruptionFilter

<p>Flag the presence or absence of interruptions in your Call Analytics transcription output.</p> <p>Rules using <code>InterruptionFilter</code> are designed to match:</p> <ul> <li> <p>Instances where an agent interrupts a customer</p> </li> <li> <p>Instances where a customer interrupts an agent</p> </li> <li> <p>Either participant interrupting the other</p> </li> <li> <p>A lack of interruptions</p> </li> </ul> <p>See <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-categories-batch.html#tca-rules-batch\">Rule criteria for post-call categories</a> for usage examples.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**threshold** | [**Integer**](Integer.md) |  |  [optional] |
|**participantRole** | [**ParticipantRole**](ParticipantRole.md) |  |  [optional] |
|**absoluteTimeRange** | [**InterruptionFilterAbsoluteTimeRange**](InterruptionFilterAbsoluteTimeRange.md) |  |  [optional] |
|**relativeTimeRange** | [**InterruptionFilterRelativeTimeRange**](InterruptionFilterRelativeTimeRange.md) |  |  [optional] |
|**negate** | [**Boolean**](Boolean.md) |  |  [optional] |



