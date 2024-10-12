# ElevenLabsApiDocumentation.SamplesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete**](SamplesApi.md#deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete) | **DELETE** /v1/voices/{voice_id}/samples/{sample_id} | Delete Sample
[**getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet**](SamplesApi.md#getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet) | **GET** /v1/voices/{voice_id}/samples/{sample_id}/audio | Get Audio From Sample



## deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete

> Object deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete(voiceId, sampleId, opts)

Delete Sample

Removes a sample by its ID.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.SamplesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let sampleId = "VW7YKqPnjY4h39yTbx2L"; // String | Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.deleteSampleV1VoicesVoiceIdSamplesSampleIdDelete(voiceId, sampleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceId** | **String**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **sampleId** | **String**| Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice. | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet

> getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet(voiceId, sampleId, opts)

Get Audio From Sample

Returns the audio corresponding to a sample attached to a voice.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.SamplesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let sampleId = "VW7YKqPnjY4h39yTbx2L"; // String | Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getAudioFromSampleV1VoicesVoiceIdSamplesSampleIdAudioGet(voiceId, sampleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceId** | **String**| Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices. | 
 **sampleId** | **String**| Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice. | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*, application/json

