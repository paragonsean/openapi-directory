# DialogflowApi.GoogleCloudDialogflowV2beta1IntentMessageTelephonyPlayAudio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioUri** | **String** | Required. URI to a Google Cloud Storage object containing the audio to play, e.g., \&quot;gs://bucket/object\&quot;. The object must contain a single channel (mono) of linear PCM audio (2 bytes / sample) at 8kHz. This object must be readable by the &#x60;service-@gcp-sa-dialogflow.iam.gserviceaccount.com&#x60; service account where is the number of the Telephony Gateway project (usually the same as the Dialogflow agent project). If the Google Cloud Storage bucket is in the Telephony Gateway project, this permission is added by default when enabling the Dialogflow V2 API. For audio from other sources, consider using the &#x60;TelephonySynthesizeSpeech&#x60; message with SSML. | [optional] 


