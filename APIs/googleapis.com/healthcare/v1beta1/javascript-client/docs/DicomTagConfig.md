# CloudHealthcareApi.DicomTagConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[Action]**](Action.md) | Specifies custom tag selections and &#x60;Actions&#x60; to apply to them. Overrides &#x60;options&#x60; and &#x60;profile&#x60;. Conflicting &#x60;Actions&#x60; are applied in the order given. | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**profileType** | **String** | Base profile type for handling DICOM tags. | [optional] 



## Enum: ProfileTypeEnum


* `PROFILE_TYPE_UNSPECIFIED` (value: `"PROFILE_TYPE_UNSPECIFIED"`)

* `MINIMAL_KEEP_LIST_PROFILE` (value: `"MINIMAL_KEEP_LIST_PROFILE"`)

* `ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE` (value: `"ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE"`)

* `KEEP_ALL_PROFILE` (value: `"KEEP_ALL_PROFILE"`)

* `DEIDENTIFY_TAG_CONTENTS` (value: `"DEIDENTIFY_TAG_CONTENTS"`)




