

# MultiBitrateFormat

Describes the properties for producing a collection of GOP aligned multi-bitrate files. The default behavior is to produce one output file for each video layer which is muxed together with all the audios. The exact output files produced can be controlled by specifying the outputFiles collection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outputFiles** | [**List&lt;OutputFile&gt;**](OutputFile.md) | The list of output files to produce.  Each entry in the list is a set of audio and video layer labels to be muxed together . |  [optional] |



