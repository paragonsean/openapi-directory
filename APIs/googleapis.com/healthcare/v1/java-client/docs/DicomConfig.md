

# DicomConfig

Specifies the parameters needed for de-identification of DICOM stores.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterProfile** | [**FilterProfileEnum**](#FilterProfileEnum) | Tag filtering profile that determines which tags to keep/remove. |  [optional] |
|**keepList** | [**TagFilterList**](TagFilterList.md) |  |  [optional] |
|**removeList** | [**TagFilterList**](TagFilterList.md) |  |  [optional] |
|**skipIdRedaction** | **Boolean** | If true, skip replacing StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID, and MediaStorageSOPInstanceUID and leave them untouched. The Cloud Healthcare API regenerates these UIDs by default based on the DICOM Standard&#39;s reasoning: \&quot;Whilst these UIDs cannot be mapped directly to an individual out of context, given access to the original images, or to a database of the original images containing the UIDs, it would be possible to recover the individual&#39;s identity.\&quot; http://dicom.nema.org/medical/dicom/current/output/chtml/part15/sect_E.3.9.html |  [optional] |



## Enum: FilterProfileEnum

| Name | Value |
|---- | -----|
| TAG_FILTER_PROFILE_UNSPECIFIED | &quot;TAG_FILTER_PROFILE_UNSPECIFIED&quot; |
| MINIMAL_KEEP_LIST_PROFILE | &quot;MINIMAL_KEEP_LIST_PROFILE&quot; |
| ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE | &quot;ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE&quot; |
| KEEP_ALL_PROFILE | &quot;KEEP_ALL_PROFILE&quot; |
| DEIDENTIFY_TAG_CONTENTS | &quot;DEIDENTIFY_TAG_CONTENTS&quot; |



