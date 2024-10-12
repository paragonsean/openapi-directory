

# HlsRenditionGroupSettings

Settings specific to audio sources in an HLS alternate rendition group. Specify the properties (renditionGroupId, renditionName or renditionLanguageCode) to identify the unique audio track among the alternative rendition groups present in the HLS manifest. If no unique track is found, or multiple tracks match the properties provided, the job fails. If no properties in hlsRenditionGroupSettings are specified, the default audio track within the video segment is chosen. If there is no audio within video segment, the alternative audio with DEFAULT=YES is chosen instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**renditionGroupId** | [**String**](String.md) |  |  [optional] |
|**renditionLanguageCode** | [**LanguageCode**](LanguageCode.md) |  |  [optional] |
|**renditionName** | [**String**](String.md) |  |  [optional] |



