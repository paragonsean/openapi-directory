# TwilioProxy.ProxyV1ServicePhoneNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PhoneNumber resource. | [optional] 
**capabilities** | [**ProxyV1ServicePhoneNumberCapabilities**](ProxyV1ServicePhoneNumberCapabilities.md) |  | [optional] 
**dateCreated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created. | [optional] 
**dateUpdated** | **Date** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**inUse** | **Number** | The number of open session assigned to the number. See the [How many Phone Numbers do I need?](https://www.twilio.com/docs/proxy/phone-numbers-needed) guide for more information. | [optional] 
**isReserved** | **Boolean** | Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information. | [optional] 
**isoCountry** | **String** | The ISO Country Code for the phone number. | [optional] 
**phoneNumber** | **String** | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**serviceSid** | **String** | The SID of the PhoneNumber resource&#39;s parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | [optional] 
**sid** | **String** | The unique string that we created to identify the PhoneNumber resource. | [optional] 
**url** | **String** | The absolute URL of the PhoneNumber resource. | [optional] 


