# TwilioVoice.VoiceV1DialingPermissionsDialingPermissionsCountry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continent** | **String** | The name of the continent in which the country is located. | [optional] 
**countryCodes** | **[String]** | The E.164 assigned [country codes(s)](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html) | [optional] 
**highRiskSpecialNumbersEnabled** | **Boolean** | Whether dialing to high-risk special services numbers is enabled. These prefixes include number ranges allocated by the country and include premium numbers, special services, shared cost, and others | [optional] 
**highRiskTollfraudNumbersEnabled** | **Boolean** | Whether dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers is enabled. These prefixes include narrow number ranges that have a high-risk of international revenue sharing fraud (IRSF) attacks, also known as [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html). These prefixes are collected from anti-fraud databases and verified by analyzing calls on our network. These prefixes are not available for download and are updated frequently | [optional] 
**isoCode** | **String** | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). | [optional] 
**links** | **Object** | A list of URLs related to this resource. | [optional] 
**lowRiskNumbersEnabled** | **Boolean** | Whether dialing to low-risk numbers is enabled. | [optional] 
**name** | **String** | The name of the country. | [optional] 
**url** | **String** | The absolute URL of this resource. | [optional] 


