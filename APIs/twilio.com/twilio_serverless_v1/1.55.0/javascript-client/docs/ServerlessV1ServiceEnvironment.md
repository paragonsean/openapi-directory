# TwilioServerless.ServerlessV1ServiceEnvironment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Environment resource. | [optional] 
**buildSid** | **String** | The SID of the build deployed in the environment. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the Environment resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the Environment resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**domainName** | **String** | The domain name for all Functions and Assets deployed in the Environment, using the Service unique name, a randomly-generated Service suffix, and an optional Environment domain suffix. | [optional] 
**domainSuffix** | **String** | A URL-friendly name that represents the environment and forms part of the domain name. | [optional] 
**links** | **Object** | The URLs of the Environment resource&#39;s nested resources. | [optional] 
**serviceSid** | **String** | The SID of the Service that the Environment resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Environment resource. | [optional] 
**uniqueName** | **String** | A user-defined string that uniquely identifies the Environment resource. | [optional] 
**url** | **String** | The absolute URL of the Environment resource. | [optional] 


