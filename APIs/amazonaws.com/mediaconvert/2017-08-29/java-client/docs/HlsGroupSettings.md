

# HlsGroupSettings

Settings related to your HLS output package. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/outputs-file-ABR.html.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adMarkers** | [**List**](List.md) |  |  [optional] |
|**additionalManifests** | [**List**](List.md) |  |  [optional] |
|**audioOnlyHeader** | [**HlsAudioOnlyHeader**](HlsAudioOnlyHeader.md) |  |  [optional] |
|**baseUrl** | [**String**](String.md) |  |  [optional] |
|**captionLanguageMappings** | [**List**](List.md) |  |  [optional] |
|**captionLanguageSetting** | [**HlsCaptionLanguageSetting**](HlsCaptionLanguageSetting.md) |  |  [optional] |
|**captionSegmentLengthControl** | [**HlsCaptionSegmentLengthControl**](HlsCaptionSegmentLengthControl.md) |  |  [optional] |
|**clientCache** | [**HlsClientCache**](HlsClientCache.md) |  |  [optional] |
|**codecSpecification** | [**HlsCodecSpecification**](HlsCodecSpecification.md) |  |  [optional] |
|**destination** | [**String**](String.md) |  |  [optional] |
|**destinationSettings** | [**CmafGroupSettingsDestinationSettings**](CmafGroupSettingsDestinationSettings.md) |  |  [optional] |
|**directoryStructure** | [**HlsDirectoryStructure**](HlsDirectoryStructure.md) |  |  [optional] |
|**encryption** | [**HlsGroupSettingsEncryption**](HlsGroupSettingsEncryption.md) |  |  [optional] |
|**imageBasedTrickPlay** | [**HlsImageBasedTrickPlay**](HlsImageBasedTrickPlay.md) |  |  [optional] |
|**imageBasedTrickPlaySettings** | [**HlsGroupSettingsImageBasedTrickPlaySettings**](HlsGroupSettingsImageBasedTrickPlaySettings.md) |  |  [optional] |
|**manifestCompression** | [**HlsManifestCompression**](HlsManifestCompression.md) |  |  [optional] |
|**manifestDurationFormat** | [**HlsManifestDurationFormat**](HlsManifestDurationFormat.md) |  |  [optional] |
|**minFinalSegmentLength** | [**Double**](Double.md) |  |  [optional] |
|**minSegmentLength** | [**Integer**](Integer.md) |  |  [optional] |
|**outputSelection** | [**HlsOutputSelection**](HlsOutputSelection.md) |  |  [optional] |
|**programDateTime** | [**HlsProgramDateTime**](HlsProgramDateTime.md) |  |  [optional] |
|**programDateTimePeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**progressiveWriteHlsManifest** | [**HlsProgressiveWriteHlsManifest**](HlsProgressiveWriteHlsManifest.md) |  |  [optional] |
|**segmentControl** | [**HlsSegmentControl**](HlsSegmentControl.md) |  |  [optional] |
|**segmentLength** | [**Integer**](Integer.md) |  |  [optional] |
|**segmentLengthControl** | [**HlsSegmentLengthControl**](HlsSegmentLengthControl.md) |  |  [optional] |
|**segmentsPerSubdirectory** | [**Integer**](Integer.md) |  |  [optional] |
|**streamInfResolution** | [**HlsStreamInfResolution**](HlsStreamInfResolution.md) |  |  [optional] |
|**targetDurationCompatibilityMode** | [**HlsTargetDurationCompatibilityMode**](HlsTargetDurationCompatibilityMode.md) |  |  [optional] |
|**timedMetadataId3Frame** | [**HlsTimedMetadataId3Frame**](HlsTimedMetadataId3Frame.md) |  |  [optional] |
|**timedMetadataId3Period** | [**Integer**](Integer.md) |  |  [optional] |
|**timestampDeltaMilliseconds** | [**Integer**](Integer.md) |  |  [optional] |



