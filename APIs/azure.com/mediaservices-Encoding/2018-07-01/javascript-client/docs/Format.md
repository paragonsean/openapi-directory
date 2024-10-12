# AzureMediaServices.Format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** | The discriminator for derived types. | 
**filenamePattern** | **String** | The pattern of the file names for the generated output files. The following macros are supported in the file name: {Basename} - The base name of the input video {Extension} - The appropriate extension for this format. {Label} - The label assigned to the codec/layer. {Index} - A unique index for thumbnails. Only applicable to thumbnails. {Bitrate} - The audio/video bitrate. Not applicable to thumbnails. {Codec} - The type of the audio/video codec. Any unsubstituted macros will be collapsed and removed from the filename. | 


