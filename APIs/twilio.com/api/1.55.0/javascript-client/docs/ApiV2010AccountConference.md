# TwilioApi.ApiV2010AccountConference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Conference resource. | [optional] 
**apiVersion** | **String** | The API version used to create this conference. | [optional] 
**callSidEndingConference** | **String** | The call SID that caused the conference to end. | [optional] 
**dateCreated** | **String** | The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | A string that you assigned to describe this conference room. Maxiumum length is 128 characters. | [optional] 
**reasonConferenceEnded** | [**ConferenceEnumReasonConferenceEnded**](ConferenceEnumReasonConferenceEnded.md) |  | [optional] 
**region** | **String** | A string that represents the Twilio Region where the conference audio was mixed. May be &#x60;us1&#x60;, &#x60;ie1&#x60;,  &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, and &#x60;jp1&#x60;. Basic conference audio will always be mixed in &#x60;us1&#x60;. Global Conference audio will be mixed nearest to the majority of participants. | [optional] 
**sid** | **String** | The unique string that that we created to identify this Conference resource. | [optional] 
**status** | [**ConferenceEnumStatus**](ConferenceEnumStatus.md) |  | [optional] 
**subresourceUris** | **Object** | A list of related resources identified by their URIs relative to &#x60;https://api.twilio.com&#x60;. | [optional] 
**uri** | **String** | The URI of this resource, relative to &#x60;https://api.twilio.com&#x60;. | [optional] 


