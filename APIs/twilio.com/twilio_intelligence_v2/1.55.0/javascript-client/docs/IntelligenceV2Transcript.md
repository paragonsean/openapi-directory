# TwilioIntelligence.IntelligenceV2Transcript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique SID identifier of the Account. | [optional] 
**channel** | **Object** | Media Channel describing Transcript Source and Participant Mapping | [optional] 
**customerKey** | **String** |  | [optional] 
**dataLogging** | **Boolean** | Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent. | [optional] 
**dateCreated** | **Date** | The date that this Transcript was created, given in ISO 8601 format. | [optional] 
**dateUpdated** | **Date** | The date that this Transcript was updated, given in ISO 8601 format. | [optional] 
**duration** | **Number** | The duration of this Transcript&#39;s source | [optional] 
**languageCode** | **String** | The default language code of the audio. | [optional] 
**links** | **Object** |  | [optional] 
**mediaStartTime** | **Date** | The date that this Transcript&#39;s media was started, given in ISO 8601 format. | [optional] 
**redaction** | **Boolean** | If the transcript has been redacted, a redacted alternative of the transcript will be available. | [optional] 
**serviceSid** | **String** | The unique SID identifier of the Service. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this Transcript. | [optional] 
**status** | [**TranscriptEnumStatus**](TranscriptEnumStatus.md) |  | [optional] 
**url** | **String** | The URL of this resource. | [optional] 


