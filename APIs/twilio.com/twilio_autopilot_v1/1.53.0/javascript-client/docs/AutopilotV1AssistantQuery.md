# TwilioAutopilot.AutopilotV1AssistantQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Query resource. | [optional] 
**assistantSid** | **String** | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dialogueSid** | **String** | The SID of the [Dialogue](https://www.twilio.com/docs/autopilot/api/dialogue). | [optional] 
**language** | **String** | The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used by the Query. For example: &#x60;en-US&#x60;. | [optional] 
**modelBuildSid** | **String** | The SID of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) queried. | [optional] 
**query** | **String** | The end-user&#39;s natural language input. | [optional] 
**results** | **Object** | The natural language analysis results that include the [Task](https://www.twilio.com/docs/autopilot/api/task) recognized and a list of identified [Fields](https://www.twilio.com/docs/autopilot/api/task-field). | [optional] 
**sampleSid** | **String** | The SID of an optional reference to the [Sample](https://www.twilio.com/docs/autopilot/api/task-sample) created from the query. | [optional] 
**sid** | **String** | The unique string that we created to identify the Query resource. | [optional] 
**sourceChannel** | **String** | The communication channel from where the end-user input came. | [optional] 
**status** | **String** | The status of the Query. Can be: &#x60;pending-review&#x60;, &#x60;reviewed&#x60;, or &#x60;discarded&#x60; | [optional] 
**url** | **String** | The absolute URL of the Query resource. | [optional] 


