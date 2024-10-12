# DialogflowApi.GoogleCloudDialogflowV2beta1OriginalDetectIntentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **{String: Object}** | Optional. This field is set to the value of the &#x60;QueryParameters.payload&#x60; field passed in the request. Some integrations that query a Dialogflow agent may provide additional information in the payload. In particular, for the Dialogflow Phone Gateway integration, this field has the form: { \&quot;telephony\&quot;: { \&quot;caller_id\&quot;: \&quot;+18558363987\&quot; } } Note: The caller ID field (&#x60;caller_id&#x60;) will be redacted for Trial Edition agents and populated with the caller ID in [E.164 format](https://en.wikipedia.org/wiki/E.164) for Essentials Edition agents. | [optional] 
**source** | **String** | The source of this request, e.g., &#x60;google&#x60;, &#x60;facebook&#x60;, &#x60;slack&#x60;. It is set by Dialogflow-owned servers. | [optional] 
**version** | **String** | Optional. The version of the protocol used for this request. This field is AoG-specific. | [optional] 


