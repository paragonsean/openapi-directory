# TwilioNumbers.NumbersV2RegulatoryComplianceBundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**email** | **String** | The email address that will receive updates when the Bundle resource changes status. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**links** | **Object** | The URLs of the Assigned Items of the Bundle resource. | [optional] 
**regulationSid** | **String** | The unique string of a regulation that is associated to the Bundle resource. | [optional] 
**sid** | **String** | The unique string that we created to identify the Bundle resource. | [optional] 
**status** | [**BundleEnumStatus**](BundleEnumStatus.md) |  | [optional] 
**statusCallback** | **String** | The URL we call to inform your application of status changes. | [optional] 
**url** | **String** | The absolute URL of the Bundle resource. | [optional] 
**validUntil** | **Date** | The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until. | [optional] 


