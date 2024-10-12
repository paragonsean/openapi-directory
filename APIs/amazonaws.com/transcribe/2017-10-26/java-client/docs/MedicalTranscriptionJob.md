

# MedicalTranscriptionJob

<p>Provides detailed information about a medical transcription job.</p> <p>To view the status of the specified medical transcription job, check the <code>TranscriptionJobStatus</code> field. If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**medicalTranscriptionJobName** | [**String**](String.md) |  |  [optional] |
|**transcriptionJobStatus** | [**TranscriptionJobStatus**](TranscriptionJobStatus.md) |  |  [optional] |
|**languageCode** | [**LanguageCode**](LanguageCode.md) |  |  [optional] |
|**mediaSampleRateHertz** | [**Integer**](Integer.md) |  |  [optional] |
|**mediaFormat** | [**MediaFormat**](MediaFormat.md) |  |  [optional] |
|**media** | [**Media**](Media.md) |  |  [optional] |
|**transcript** | [**MedicalTranscriptionJobTranscript**](MedicalTranscriptionJobTranscript.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**settings** | [**MedicalTranscriptionJobSettings**](MedicalTranscriptionJobSettings.md) |  |  [optional] |
|**contentIdentificationType** | [**MedicalContentIdentificationType**](MedicalContentIdentificationType.md) |  |  [optional] |
|**specialty** | [**Specialty**](Specialty.md) |  |  [optional] |
|**type** | [**Type**](Type.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |



