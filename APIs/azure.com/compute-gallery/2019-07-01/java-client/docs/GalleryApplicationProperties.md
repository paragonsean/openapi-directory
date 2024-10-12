

# GalleryApplicationProperties

Describes the properties of a gallery Application Definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of this gallery Application Definition resource. This property is updatable. |  [optional] |
|**endOfLifeDate** | **OffsetDateTime** | The end of life date of the gallery Application Definition. This property can be used for decommissioning purposes. This property is updatable. |  [optional] |
|**eula** | **String** | The Eula agreement for the gallery Application Definition. |  [optional] |
|**privacyStatementUri** | **String** | The privacy statement uri. |  [optional] |
|**releaseNoteUri** | **String** | The release note uri. |  [optional] |
|**supportedOSType** | [**SupportedOSTypeEnum**](#SupportedOSTypeEnum) | This property allows you to specify the supported type of the OS that application is built for. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **Windows** &lt;br&gt;&lt;br&gt; **Linux** |  |



## Enum: SupportedOSTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



