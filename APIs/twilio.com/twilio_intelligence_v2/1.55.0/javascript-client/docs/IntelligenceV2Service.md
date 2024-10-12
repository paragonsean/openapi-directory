# TwilioIntelligence.IntelligenceV2Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique SID identifier of the Account the Service belongs to. | [optional] 
**autoRedaction** | **Boolean** | Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service. | [optional] 
**autoTranscribe** | **Boolean** | Instructs the Speech Recognition service to automatically transcribe all recordings made on the account. | [optional] 
**dataLogging** | **Boolean** | Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent. | [optional] 
**dateCreated** | **Date** | The date that this Service was created, given in ISO 8601 format. | [optional] 
**dateUpdated** | **Date** | The date that this Service was updated, given in ISO 8601 format. | [optional] 
**friendlyName** | **String** | A human readable description of this resource, up to 64 characters. | [optional] 
**languageCode** | **String** | The default language code of the audio. | [optional] 
**mediaRedaction** | **Boolean** | Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise. | [optional] 
**sid** | **String** | A 34 character string that uniquely identifies this Service. | [optional] 
**uniqueName** | **String** | Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID. | [optional] 
**url** | **String** | The URL of this resource. | [optional] 
**version** | **Number** | The version number of this Service. | [optional] 
**webhookHttpMethod** | [**ServiceEnumHttpMethod**](ServiceEnumHttpMethod.md) |  | [optional] 
**webhookUrl** | **String** | The URL Twilio will request when executing the Webhook. | [optional] 


