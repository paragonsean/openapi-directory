# TwilioStudio.StudioV2FlowFlowRevision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flow resource. | [optional] 
**commitMessage** | **String** | Description of change made in the revision. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**definition** | **Object** | JSON representation of flow definition. | [optional] 
**errors** | **[Object]** | List of error in the flow definition. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the Flow. | [optional] 
**revision** | **Number** | The latest revision number of the Flow&#39;s definition. | [optional] 
**sid** | **String** | The unique string that we created to identify the Flow resource. | [optional] 
**status** | [**FlowRevisionEnumStatus**](FlowRevisionEnumStatus.md) |  | [optional] 
**url** | **String** | The absolute URL of the resource. | [optional] 
**valid** | **Boolean** | Boolean if the flow definition is valid. | [optional] 


