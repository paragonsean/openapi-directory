# TwilioMessaging.MessagingV1ServicePhoneNumber

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PhoneNumber resource. | [optional] 
**capabilities** | **[String]** | An array of values that describe whether the number can receive calls or messages. Can be: &#x60;Voice&#x60;, &#x60;SMS&#x60;, and &#x60;MMS&#x60;. | [optional] 
**countryCode** | **String** | The 2-character [ISO Country Code](https://www.iso.org/iso-3166-country-codes.html) of the number. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**phoneNumber** | **String** | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the PhoneNumber resource. | [optional] 
**url** | **String** | The absolute URL of the PhoneNumber resource. | [optional] 


