

# TranscriptionJob

<p>Provides detailed information about a transcription job.</p> <p>To view the status of the specified transcription job, check the <code>TranscriptionJobStatus</code> field. If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p> <p>If you enabled content redaction, the redacted transcript can be found at the location specified in <code>RedactedTranscriptFileUri</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transcriptionJobName** | [**String**](String.md) |  |  [optional] |
|**transcriptionJobStatus** | [**TranscriptionJobStatus**](TranscriptionJobStatus.md) |  |  [optional] |
|**languageCode** | [**LanguageCode**](LanguageCode.md) |  |  [optional] |
|**mediaSampleRateHertz** | [**Integer**](Integer.md) |  |  [optional] |
|**mediaFormat** | [**MediaFormat**](MediaFormat.md) |  |  [optional] |
|**media** | [**TranscriptionJobMedia**](TranscriptionJobMedia.md) |  |  [optional] |
|**transcript** | [**TranscriptionJobTranscript**](TranscriptionJobTranscript.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**settings** | [**TranscriptionJobSettings**](TranscriptionJobSettings.md) |  |  [optional] |
|**modelSettings** | [**TranscriptionJobModelSettings**](TranscriptionJobModelSettings.md) |  |  [optional] |
|**jobExecutionSettings** | [**TranscriptionJobJobExecutionSettings**](TranscriptionJobJobExecutionSettings.md) |  |  [optional] |
|**contentRedaction** | [**TranscriptionJobContentRedaction**](TranscriptionJobContentRedaction.md) |  |  [optional] |
|**identifyLanguage** | [**Boolean**](Boolean.md) |  |  [optional] |
|**identifyMultipleLanguages** | [**Boolean**](Boolean.md) |  |  [optional] |
|**languageOptions** | [**List**](List.md) |  |  [optional] |
|**identifiedLanguageScore** | [**Float**](Float.md) |  |  [optional] |
|**languageCodes** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**subtitles** | [**TranscriptionJobSubtitles**](TranscriptionJobSubtitles.md) |  |  [optional] |
|**languageIdSettings** | [**Map**](Map.md) |  |  [optional] |
|**toxicityDetection** | [**List**](List.md) |  |  [optional] |



