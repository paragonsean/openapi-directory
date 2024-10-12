# OpenapiJsClient.PatientAmendment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amendmentFile** | **String** | A PDF file containing the amended information for the patient&#39;s record | 
**amendmentName** | **String** |  | 
**appointment** | **Number** | ID of the appointment to which the amendment applies, if any. If present, the &#x60;amendment_file&#x60; will be appended to the clinical note for this appointment. | [optional] 
**comments** | **String** |  | [optional] 
**doctor** | **Number** | ID of the doctor who owns the amendment | 
**id** | **Number** |  | [optional] [readonly] 
**patient** | **Number** | ID of the patient to whom the amendment applies | 


