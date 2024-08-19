# GoogleFormsApi.FormResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | [**{String: Answer}**](Answer.md) | Output only. The actual answers to the questions, keyed by question_id. | [optional] [readonly] 
**createTime** | **String** | Output only. Timestamp for the first time the response was submitted. | [optional] [readonly] 
**formId** | **String** | Output only. The form ID. | [optional] [readonly] 
**lastSubmittedTime** | **String** | Output only. Timestamp for the most recent time the response was submitted. Does not track changes to grades. | [optional] [readonly] 
**respondentEmail** | **String** | Output only. The email address (if collected) for the respondent. | [optional] [readonly] 
**responseId** | **String** | Output only. The response ID. | [optional] [readonly] 
**totalScore** | **Number** | Output only. The total number of points the respondent received for their submission Only set if the form was a quiz and the response was graded. This includes points automatically awarded via autograding adjusted by any manual corrections entered by the form owner. | [optional] [readonly] 


