# TwilioServerless.ServerlessV1Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the Service resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the Service resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**domainBase** | **String** | The base domain name for this Service, which is a combination of the unique name and a randomly generated string. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the Service resource. | [optional] 
**includeCredentials** | **Boolean** | Whether to inject Account credentials into a function invocation context. | [optional] 
**links** | **Object** | The URLs of the Service&#39;s nested resources. | [optional] 
**sid** | **String** | The unique string that we created to identify the Service resource. | [optional] 
**uiEditable** | **Boolean** | Whether the Service resource&#39;s properties and subresources can be edited via the UI. | [optional] 
**uniqueName** | **String** | A user-defined string that uniquely identifies the Service resource. It can be used in place of the Service resource&#39;s &#x60;sid&#x60; in the URL to address the Service resource. | [optional] 
**url** | **String** | The absolute URL of the Service resource. | [optional] 


