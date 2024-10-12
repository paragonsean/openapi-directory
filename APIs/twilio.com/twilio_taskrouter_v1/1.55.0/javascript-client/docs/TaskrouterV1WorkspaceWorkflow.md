# TwilioTaskrouter.TaskrouterV1WorkspaceWorkflow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workflow resource. | [optional] 
**assignmentCallbackUrl** | **String** | The URL that we call when a task managed by the Workflow is assigned to a Worker. See Assignment Callback URL for more information. | [optional] 
**configuration** | **String** | A JSON string that contains the Workflow&#39;s configuration. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**documentContentType** | **String** | The MIME type of the document. | [optional] 
**fallbackAssignmentCallbackUrl** | **String** | The URL that we call when a call to the &#x60;assignment_callback_url&#x60; fails. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the Workflow resource. For example, &#x60;Customer Support&#x60; or &#x60;2014 Election Campaign&#x60;. | [optional] 
**links** | **Object** | The URLs of related resources. | [optional] 
**sid** | **String** | The unique string that we created to identify the Workflow resource. | [optional] 
**taskReservationTimeout** | **Number** | How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;. | [optional] 
**url** | **String** | The absolute URL of the Workflow resource. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that contains the Workflow. | [optional] 


