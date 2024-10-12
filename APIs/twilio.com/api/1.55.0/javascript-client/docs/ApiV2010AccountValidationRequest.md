# TwilioApi.ApiV2010AccountValidationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the Caller ID. | [optional] 
**callSid** | **String** | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Caller ID is associated with. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**phoneNumber** | **String** | The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**validationCode** | **String** | The 6 digit validation code that someone must enter to validate the Caller ID  when &#x60;phone_number&#x60; is called. | [optional] 


