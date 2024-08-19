

# M2tsSettings

MPEG-2 TS container settings. These apply to outputs in a File output group when the output's container is MPEG-2 Transport Stream (M2TS). In these assets, data is organized by the program map table (PMT). Each transport stream program contains subsets of data, including audio, video, and metadata. Each of these subsets of data has a numerical label called a packet identifier (PID). Each transport stream program corresponds to one MediaConvert output. The PMT lists the types of data in a program along with their PID. Downstream systems and players use the program map table to look up the PID for each type of data it accesses and then uses the PIDs to locate specific data within the asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioBufferModel** | [**M2tsAudioBufferModel**](M2tsAudioBufferModel.md) |  |  [optional] |
|**audioDuration** | [**M2tsAudioDuration**](M2tsAudioDuration.md) |  |  [optional] |
|**audioFramesPerPes** | [**Integer**](Integer.md) |  |  [optional] |
|**audioPids** | [**List**](List.md) |  |  [optional] |
|**bitrate** | [**Integer**](Integer.md) |  |  [optional] |
|**bufferModel** | [**M2tsBufferModel**](M2tsBufferModel.md) |  |  [optional] |
|**dataPTSControl** | [**M2tsDataPtsControl**](M2tsDataPtsControl.md) |  |  [optional] |
|**dvbNitSettings** | [**M2tsSettingsDvbNitSettings**](M2tsSettingsDvbNitSettings.md) |  |  [optional] |
|**dvbSdtSettings** | [**M2tsSettingsDvbSdtSettings**](M2tsSettingsDvbSdtSettings.md) |  |  [optional] |
|**dvbSubPids** | [**List**](List.md) |  |  [optional] |
|**dvbTdtSettings** | [**M2tsSettingsDvbTdtSettings**](M2tsSettingsDvbTdtSettings.md) |  |  [optional] |
|**dvbTeletextPid** | [**Integer**](Integer.md) |  |  [optional] |
|**ebpAudioInterval** | [**M2tsEbpAudioInterval**](M2tsEbpAudioInterval.md) |  |  [optional] |
|**ebpPlacement** | [**M2tsEbpPlacement**](M2tsEbpPlacement.md) |  |  [optional] |
|**esRateInPes** | [**M2tsEsRateInPes**](M2tsEsRateInPes.md) |  |  [optional] |
|**forceTsVideoEbpOrder** | [**M2tsForceTsVideoEbpOrder**](M2tsForceTsVideoEbpOrder.md) |  |  [optional] |
|**fragmentTime** | [**Double**](Double.md) |  |  [optional] |
|**klvMetadata** | [**M2tsKlvMetadata**](M2tsKlvMetadata.md) |  |  [optional] |
|**maxPcrInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**minEbpInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**nielsenId3** | [**M2tsNielsenId3**](M2tsNielsenId3.md) |  |  [optional] |
|**nullPacketBitrate** | [**Double**](Double.md) |  |  [optional] |
|**patInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**pcrControl** | [**M2tsPcrControl**](M2tsPcrControl.md) |  |  [optional] |
|**pcrPid** | [**Integer**](Integer.md) |  |  [optional] |
|**pmtInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**pmtPid** | [**Integer**](Integer.md) |  |  [optional] |
|**privateMetadataPid** | [**Integer**](Integer.md) |  |  [optional] |
|**programNumber** | [**Integer**](Integer.md) |  |  [optional] |
|**rateMode** | [**M2tsRateMode**](M2tsRateMode.md) |  |  [optional] |
|**scte35Esam** | [**M2tsSettingsScte35Esam**](M2tsSettingsScte35Esam.md) |  |  [optional] |
|**scte35Pid** | [**Integer**](Integer.md) |  |  [optional] |
|**scte35Source** | [**M2tsScte35Source**](M2tsScte35Source.md) |  |  [optional] |
|**segmentationMarkers** | [**M2tsSegmentationMarkers**](M2tsSegmentationMarkers.md) |  |  [optional] |
|**segmentationStyle** | [**M2tsSegmentationStyle**](M2tsSegmentationStyle.md) |  |  [optional] |
|**segmentationTime** | [**Double**](Double.md) |  |  [optional] |
|**timedMetadataPid** | [**Integer**](Integer.md) |  |  [optional] |
|**transportStreamId** | [**Integer**](Integer.md) |  |  [optional] |
|**videoPid** | [**Integer**](Integer.md) |  |  [optional] |



