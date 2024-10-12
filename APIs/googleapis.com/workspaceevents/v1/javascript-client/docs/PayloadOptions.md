# GoogleWorkspaceEventsApi.PayloadOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldMask** | **String** | Optional. If &#x60;include_resource&#x60; is set to &#x60;true&#x60;, the list of fields to include in the event payload. Separate fields with a comma. For example, to include a Google Chat message&#39;s sender and create time, enter &#x60;message.sender,message.createTime&#x60;. If omitted, the payload includes all fields for the resource. If you specify a field that doesn&#39;t exist for the resource, the system ignores the field. | [optional] 
**includeResource** | **Boolean** | Optional. Whether the event payload includes data about the resource that changed. For example, for an event where a Google Chat message was created, whether the payload contains data about the [&#x60;Message&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages) resource. If false, the event payload only includes the name of the changed resource. | [optional] 


