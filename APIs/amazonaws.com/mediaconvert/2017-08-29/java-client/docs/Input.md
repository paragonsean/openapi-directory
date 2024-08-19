

# Input

Use inputs to define the source files used in your transcoding job. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/specify-input-settings.html. You can use multiple video inputs to do input stitching. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/assembling-multiple-inputs-and-input-clips.html

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advancedInputFilter** | [**AdvancedInputFilter**](AdvancedInputFilter.md) |  |  [optional] |
|**advancedInputFilterSettings** | [**InputAdvancedInputFilterSettings**](InputAdvancedInputFilterSettings.md) |  |  [optional] |
|**audioSelectorGroups** | [**Map**](Map.md) |  |  [optional] |
|**audioSelectors** | [**Map**](Map.md) |  |  [optional] |
|**captionSelectors** | [**Map**](Map.md) |  |  [optional] |
|**crop** | [**InputCrop**](InputCrop.md) |  |  [optional] |
|**deblockFilter** | [**InputDeblockFilter**](InputDeblockFilter.md) |  |  [optional] |
|**decryptionSettings** | [**InputDecryptionSettings**](InputDecryptionSettings.md) |  |  [optional] |
|**denoiseFilter** | [**InputDenoiseFilter**](InputDenoiseFilter.md) |  |  [optional] |
|**dolbyVisionMetadataXml** | [**String**](String.md) |  |  [optional] |
|**fileInput** | [**String**](String.md) |  |  [optional] |
|**filterEnable** | [**InputFilterEnable**](InputFilterEnable.md) |  |  [optional] |
|**filterStrength** | [**Integer**](Integer.md) |  |  [optional] |
|**imageInserter** | [**InputImageInserter**](InputImageInserter.md) |  |  [optional] |
|**inputClippings** | [**List**](List.md) |  |  [optional] |
|**inputScanType** | [**InputScanType**](InputScanType.md) |  |  [optional] |
|**position** | [**InputPosition**](InputPosition.md) |  |  [optional] |
|**programNumber** | [**Integer**](Integer.md) |  |  [optional] |
|**psiControl** | [**InputPsiControl**](InputPsiControl.md) |  |  [optional] |
|**supplementalImps** | [**List**](List.md) |  |  [optional] |
|**timecodeSource** | [**InputTimecodeSource**](InputTimecodeSource.md) |  |  [optional] |
|**timecodeStart** | [**String**](String.md) |  |  [optional] |
|**videoGenerator** | [**InputVideoGenerator**](InputVideoGenerator.md) |  |  [optional] |
|**videoSelector** | [**InputVideoSelector**](InputVideoSelector.md) |  |  [optional] |



