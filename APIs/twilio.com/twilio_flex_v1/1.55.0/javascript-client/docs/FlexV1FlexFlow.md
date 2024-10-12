# TwilioFlex.FlexV1FlexFlow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Flow resource and owns this Workflow. | [optional] 
**channelType** | [**FlexFlowEnumChannelType**](FlexFlowEnumChannelType.md) |  | [optional] 
**chatServiceSid** | **String** | The SID of the chat service. | [optional] 
**contactIdentity** | **String** | The channel contact&#39;s Identity. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**enabled** | **Boolean** | Whether the Flex Flow is enabled. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**integration** | **Object** | An object that contains specific parameters for the integration. | [optional] 
**integrationType** | [**FlexFlowEnumIntegrationType**](FlexFlowEnumIntegrationType.md) |  | [optional] 
**janitorEnabled** | **Boolean** | When enabled, the Messaging Channel Janitor will remove active Proxy sessions if the associated Task is deleted outside of the Flex UI. Defaults to &#x60;false&#x60;. | [optional] 
**longLived** | **Boolean** | When enabled, Flex will keep the chat channel active so that it may be used for subsequent interactions with a contact identity. Defaults to &#x60;false&#x60;. | [optional] 
**sid** | **String** | The unique string that we created to identify the Flex Flow resource. | [optional] 
**url** | **String** | The absolute URL of the Flex Flow resource. | [optional] 


