# TwilioInsights.InsightsV1CallAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique SID identifier of the Account. | [optional] 
**answeredBy** | [**AnnotationEnumAnsweredBy**](AnnotationEnumAnsweredBy.md) |  | [optional] 
**callScore** | **Number** | Specifies the Call Score, if available. This is of type integer. Use a range of 1-5 to indicate the call experience score, with the following mapping as a reference for rating the call [5: Excellent, 4: Good, 3 : Fair, 2 : Poor, 1: Bad]. | [optional] 
**callSid** | **String** | The unique SID identifier of the Call. | [optional] 
**comment** | **String** | Specifies any comments pertaining to the call. Twilio does not treat this field as PII, so no PII should be included in comments. | [optional] 
**connectivityIssue** | [**AnnotationEnumConnectivityIssue**](AnnotationEnumConnectivityIssue.md) |  | [optional] 
**incident** | **String** | Incident or support ticket associated with this call. The &#x60;incident&#x60; property is of type string with a maximum character limit of 100. Twilio does not treat this field as PII, so no PII should be included in &#x60;incident&#x60;. | [optional] 
**qualityIssues** | **[String]** | Specifies if the call had any subjective quality issues. Possible values are one or more of &#x60;no_quality_issue&#x60;, &#x60;low_volume&#x60;, &#x60;choppy_robotic&#x60;, &#x60;echo&#x60;, &#x60;dtmf&#x60;, &#x60;latency&#x60;, &#x60;owa&#x60;, or &#x60;static_noise&#x60;. | [optional] 
**spam** | **Boolean** | Specifies if the call was a spam call. Use this to provide feedback on whether calls placed from your account were marked as spam, or if inbound calls received by your account were unwanted spam. Is of type Boolean: true, false. Use true if the call was a spam call. | [optional] 
**url** | **String** |  | [optional] 


