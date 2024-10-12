

# Action

Specifies a selection of tags and an `Action` to apply to each one.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cleanImageTag** | [**ImageConfig**](ImageConfig.md) |  |  [optional] |
|**cleanTextTag** | **Object** | Inspect text and transform sensitive text. Configurable using TextConfig. Supported [Value Representations] (http://dicom.nema.org/medical/dicom/2018e/output/chtml/part05/sect_6.2.html#table_6.2-1): AE, LO, LT, PN, SH, ST, UC, UT, DA, DT, AS |  [optional] |
|**deleteTag** | **Object** | Delete tag. |  [optional] |
|**keepTag** | **Object** | Keep tag unchanged. |  [optional] |
|**queries** | **List&lt;String&gt;** | Select all tags with the listed tag IDs, names, or Value Representations (VRs). Examples: ID: \&quot;00100010\&quot; Keyword: \&quot;PatientName\&quot; VR: \&quot;PN\&quot; |  [optional] |
|**recurseTag** | **Object** | Recursively apply DICOM de-id to tags nested in a sequence. Supported [Value Representation] (http://dicom.nema.org/medical/dicom/2018e/output/chtml/part05/sect_6.2.html#table_6.2-1): SQ |  [optional] |
|**regenUidTag** | **Object** | Replace UID with a new generated UID. Supported [Value Representation] (http://dicom.nema.org/medical/dicom/2018e/output/chtml/part05/sect_6.2.html#table_6.2-1): UI |  [optional] |
|**removeTag** | **Object** | Replace with empty tag. |  [optional] |
|**resetTag** | **Object** | Reset tag to a placeholder value. |  [optional] |



