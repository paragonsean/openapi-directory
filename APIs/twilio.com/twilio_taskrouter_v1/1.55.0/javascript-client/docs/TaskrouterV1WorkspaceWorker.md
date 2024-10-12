# TwilioTaskrouter.TaskrouterV1WorkspaceWorker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource. | [optional] 
**activityName** | **String** | The &#x60;friendly_name&#x60; of the Worker&#39;s current Activity. | [optional] 
**activitySid** | **String** | The SID of the Worker&#39;s current Activity. | [optional] 
**attributes** | **String** | The JSON string that describes the Worker. For example: &#x60;{ \&quot;email\&quot;: \&quot;Bob@example.com\&quot;, \&quot;phone\&quot;: \&quot;+5095551234\&quot; }&#x60;. **Note** If this property has been assigned a value, it will only be displayed in FETCH actions that return a single resource. Otherwise, this property will be null, even if it has a value. This data is passed to the &#x60;assignment_callback_url&#x60; when TaskRouter assigns a Task to the Worker. | [optional] 
**available** | **Boolean** | Whether the Worker is available to perform tasks. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateStatusChanged** | **Date** | The date and time in GMT of the last change to the Worker&#39;s activity specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Used to calculate Workflow statistics. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. Friendly names are case insensitive, and unique within the TaskRouter Workspace. | [optional] 
**links** | **Object** | The URLs of related resources. | [optional] 
**sid** | **String** | The unique string that we created to identify the Worker resource. | [optional] 
**url** | **String** | The absolute URL of the Worker resource. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that contains the Worker. | [optional] 


