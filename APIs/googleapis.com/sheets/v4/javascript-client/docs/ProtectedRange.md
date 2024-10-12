# GoogleSheetsApi.ProtectedRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of this protected range. | [optional] 
**editors** | [**Editors**](Editors.md) |  | [optional] 
**namedRangeId** | **String** | The named range this protected range is backed by, if any. When writing, only one of range or named_range_id may be set. | [optional] 
**protectedRangeId** | **Number** | The ID of the protected range. This field is read-only. | [optional] 
**range** | [**GridRange**](GridRange.md) |  | [optional] 
**requestingUserCanEdit** | **Boolean** | True if the user who requested this protected range can edit the protected area. This field is read-only. | [optional] 
**unprotectedRanges** | [**[GridRange]**](GridRange.md) | The list of unprotected ranges within a protected sheet. Unprotected ranges are only supported on protected sheets. | [optional] 
**warningOnly** | **Boolean** | True if this protected range will show a warning when editing. Warning-based protection means that every user can edit data in the protected range, except editing will prompt a warning asking the user to confirm the edit. When writing: if this field is true, then editors are ignored. Additionally, if this field is changed from true to false and the &#x60;editors&#x60; field is not set (nor included in the field mask), then the editors will be set to all the editors in the document. | [optional] 


