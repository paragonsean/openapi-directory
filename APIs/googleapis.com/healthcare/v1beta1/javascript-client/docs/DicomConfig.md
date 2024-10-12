# CloudHealthcareApi.DicomConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterProfile** | **String** | Tag filtering profile that determines which tags to keep/remove. | [optional] 
**keepList** | [**TagFilterList**](TagFilterList.md) |  | [optional] 
**removeList** | [**TagFilterList**](TagFilterList.md) |  | [optional] 
**skipIdRedaction** | **Boolean** | If true, skip replacing StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID, and MediaStorageSOPInstanceUID and leave them untouched. The Cloud Healthcare API regenerates these UIDs by default based on the DICOM Standard&#39;s reasoning: \&quot;Whilst these UIDs cannot be mapped directly to an individual out of context, given access to the original images, or to a database of the original images containing the UIDs, it would be possible to recover the individual&#39;s identity.\&quot; http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.9.html | [optional] 



## Enum: FilterProfileEnum


* `TAG_FILTER_PROFILE_UNSPECIFIED` (value: `"TAG_FILTER_PROFILE_UNSPECIFIED"`)

* `MINIMAL_KEEP_LIST_PROFILE` (value: `"MINIMAL_KEEP_LIST_PROFILE"`)

* `ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE` (value: `"ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE"`)

* `KEEP_ALL_PROFILE` (value: `"KEEP_ALL_PROFILE"`)

* `DEIDENTIFY_TAG_CONTENTS` (value: `"DEIDENTIFY_TAG_CONTENTS"`)




