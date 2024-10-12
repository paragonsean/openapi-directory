

# DicomTagConfig

Specifies the parameters needed for the de-identification of DICOM stores.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actions** | [**List&lt;Action&gt;**](Action.md) | Specifies custom tag selections and &#x60;Actions&#x60; to apply to them. Overrides &#x60;options&#x60; and &#x60;profile&#x60;. Conflicting &#x60;Actions&#x60; are applied in the order given. |  [optional] |
|**options** | [**Options**](Options.md) |  |  [optional] |
|**profileType** | [**ProfileTypeEnum**](#ProfileTypeEnum) | Base profile type for handling DICOM tags. |  [optional] |



## Enum: ProfileTypeEnum

| Name | Value |
|---- | -----|
| PROFILE_TYPE_UNSPECIFIED | &quot;PROFILE_TYPE_UNSPECIFIED&quot; |
| MINIMAL_KEEP_LIST_PROFILE | &quot;MINIMAL_KEEP_LIST_PROFILE&quot; |
| ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE | &quot;ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE&quot; |
| KEEP_ALL_PROFILE | &quot;KEEP_ALL_PROFILE&quot; |
| DEIDENTIFY_TAG_CONTENTS | &quot;DEIDENTIFY_TAG_CONTENTS&quot; |



