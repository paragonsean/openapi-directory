# TwilioApi.ApiV2010AccountAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource. | [optional] 
**city** | **String** | The city in which the address is located. | [optional] 
**customerName** | **String** | The name associated with the address.This property has a maximum length of 16 4-byte characters, or 21 3-byte characters. | [optional] 
**dateCreated** | **String** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**emergencyEnabled** | **Boolean** | Whether emergency calling has been enabled on this number. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**isoCountry** | **String** | The ISO country code of the address. | [optional] 
**postalCode** | **String** | The postal code of the address. | [optional] 
**region** | **String** | The state or region of the address. | [optional] 
**sid** | **String** | The unique string that that we created to identify the Address resource. | [optional] 
**street** | **String** | The number and street address of the address. | [optional] 
**streetSecondary** | **String** | The additional number and street address of the address. | [optional] 
**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 
**validated** | **Boolean** | Whether the address has been validated to comply with local regulation. In countries that require valid addresses, an invalid address will not be accepted. &#x60;true&#x60; indicates the Address has been validated. &#x60;false&#x60; indicate the country doesn&#39;t require validation or the Address is not valid. | [optional] 
**verified** | **Boolean** | Whether the address has been verified to comply with regulation. In countries that require valid addresses, an invalid address will not be accepted. &#x60;true&#x60; indicates the Address has been verified. &#x60;false&#x60; indicate the country doesn&#39;t require verified or the Address is not valid. | [optional] 


