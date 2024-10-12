# TwilioApi.ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberNational

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressRequirements** | **String** | The type of [Address](https://www.twilio.com/docs/usage/api/address) resource the phone number requires. Can be: &#x60;none&#x60;, &#x60;any&#x60;, &#x60;local&#x60;, or &#x60;foreign&#x60;. &#x60;none&#x60; means no address is required. &#x60;any&#x60; means an address is required, but it can be anywhere in the world. &#x60;local&#x60; means an address in the phone number&#39;s country is required. &#x60;foreign&#x60; means an address outside of the phone number&#39;s country is required. | [optional] 
**beta** | **Boolean** | Whether the phone number is new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
**capabilities** | [**ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberLocalCapabilities**](ApiV2010AccountAvailablePhoneNumberCountryAvailablePhoneNumberLocalCapabilities.md) |  | [optional] 
**friendlyName** | **String** | A formatted version of the phone number. | [optional] 
**isoCountry** | **String** | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of this phone number. | [optional] 
**lata** | **String** | The [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) of this phone number. Available for only phone numbers from the US and Canada. | [optional] 
**latitude** | **Number** | The latitude of this phone number&#39;s location. Available for only phone numbers from the US and Canada. | [optional] 
**locality** | **String** | The locality or city of this phone number&#39;s location. | [optional] 
**longitude** | **Number** | The longitude of this phone number&#39;s location. Available for only phone numbers from the US and Canada. | [optional] 
**phoneNumber** | **String** | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number. | [optional] 
**postalCode** | **String** | The postal or ZIP code of this phone number&#39;s location. Available for only phone numbers from the US and Canada. | [optional] 
**rateCenter** | **String** | The [rate center](https://en.wikipedia.org/wiki/Telephone_exchange) of this phone number. Available for only phone numbers from the US and Canada. | [optional] 
**region** | **String** | The two-letter state or province abbreviation of this phone number&#39;s location. Available for only phone numbers from the US and Canada. | [optional] 


