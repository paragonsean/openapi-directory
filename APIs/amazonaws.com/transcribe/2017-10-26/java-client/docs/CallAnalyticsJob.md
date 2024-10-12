

# CallAnalyticsJob

<p>Provides detailed information about a Call Analytics job.</p> <p>To view the job's status, refer to <code>CallAnalyticsJobStatus</code>. If the status is <code>COMPLETED</code>, the job is finished. You can find your completed transcript at the URI specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p> <p>If you enabled personally identifiable information (PII) redaction, the redacted transcript appears at the location specified in <code>RedactedTranscriptFileUri</code>.</p> <p>If you chose to redact the audio in your media file, you can find your redacted media file at the location specified in the <code>RedactedMediaFileUri</code> field of your response.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callAnalyticsJobName** | [**String**](String.md) |  |  [optional] |
|**callAnalyticsJobStatus** | [**CallAnalyticsJobStatus**](CallAnalyticsJobStatus.md) |  |  [optional] |
|**languageCode** | [**LanguageCode**](LanguageCode.md) |  |  [optional] |
|**mediaSampleRateHertz** | [**Integer**](Integer.md) |  |  [optional] |
|**mediaFormat** | [**MediaFormat**](MediaFormat.md) |  |  [optional] |
|**media** | [**CallAnalyticsJobMedia**](CallAnalyticsJobMedia.md) |  |  [optional] |
|**transcript** | [**Transcript**](Transcript.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**dataAccessRoleArn** | [**String**](String.md) |  |  [optional] |
|**identifiedLanguageScore** | [**Float**](Float.md) |  |  [optional] |
|**settings** | [**CallAnalyticsJobSettings**](CallAnalyticsJobSettings.md) |  |  [optional] |
|**channelDefinitions** | [**List**](List.md) |  |  [optional] |



