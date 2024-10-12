# TwilioContent.ContentV1LegacyContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | A string name used to describe the Content resource. Not visible to the end recipient. | [optional] 
**language** | **String** | Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in. | [optional] 
**legacyBody** | **String** | The string body field of the legacy content template associated with this Content resource | [optional] 
**legacyTemplateName** | **String** | The string name of the legacy content template associated with this Content resource, unique across all template names for its account.  Only lowercase letters, numbers and underscores are allowed | [optional] 
**sid** | **String** | The unique string that that we created to identify the Content resource. | [optional] 
**types** | **Object** | The [Content types](https://www.twilio.com/docs/content/content-types-overview) (e.g. twilio/text) for this Content resource. | [optional] 
**url** | **String** | The URL of the resource, relative to &#x60;https://content.twilio.com&#x60;. | [optional] 
**variables** | **Object** | Defines the default placeholder values for variables included in the Content resource. e.g. {\&quot;1\&quot;: \&quot;Customer_Name\&quot;}. | [optional] 


