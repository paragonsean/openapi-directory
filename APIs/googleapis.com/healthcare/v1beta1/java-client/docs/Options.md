

# Options

Specifies additional options to apply to the base profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cleanDescriptors** | **Object** | This option is based on the DICOM Standard&#39;s [Clean Descriptors Option](http://dicom.nema.org/medical/dicom/2018e/output/chtml/part15/sect_E.3.5.html), and the &#x60;CleanText&#x60; &#x60;Action&#x60; is applied to all the specified fields. When cleaning text, the process attempts to transform phrases matching any of the tags marked for removal (action codes D, Z, X, and U) in the [Basic Profile](http://dicom.nema.org/medical/dicom/2018e/output/chtml/part15/chapter_E.html). These contextual phrases are replaced with the token \&quot;[CTX]\&quot;. This option uses an additional infoType during inspection. |  [optional] |
|**cleanImage** | [**ImageConfig**](ImageConfig.md) |  |  [optional] |
|**primaryIds** | [**PrimaryIdsEnum**](#PrimaryIdsEnum) | Set &#x60;Action&#x60; for [&#x60;StudyInstanceUID&#x60;, &#x60;SeriesInstanceUID&#x60;, &#x60;SOPInstanceUID&#x60;, and &#x60;MediaStorageSOPInstanceUID&#x60;](http://dicom.nema.org/medical/dicom/2018e/output/chtml/part06/chapter_6.html). |  [optional] |



## Enum: PrimaryIdsEnum

| Name | Value |
|---- | -----|
| PRIMARY_IDS_OPTION_UNSPECIFIED | &quot;PRIMARY_IDS_OPTION_UNSPECIFIED&quot; |
| KEEP | &quot;KEEP&quot; |
| REGEN | &quot;REGEN&quot; |



