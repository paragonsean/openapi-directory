# GoogleDriveApi.LabelFieldModification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldId** | **String** | The ID of the field to be modified. | [optional] 
**kind** | **String** | This is always drive#labelFieldModification. | [optional] 
**setDateValues** | **[Date]** | Replaces the value of a dateString Field with these new values. The string must be in the RFC 3339 full-date format: YYYY-MM-DD. | [optional] 
**setIntegerValues** | **[String]** | Replaces the value of an &#x60;integer&#x60; field with these new values. | [optional] 
**setSelectionValues** | **[String]** | Replaces a &#x60;selection&#x60; field with these new values. | [optional] 
**setTextValues** | **[String]** | Sets the value of a &#x60;text&#x60; field. | [optional] 
**setUserValues** | **[String]** | Replaces a &#x60;user&#x60; field with these new values. The values must be valid email addresses. | [optional] 
**unsetValues** | **Boolean** | Unsets the values for this field. | [optional] 


