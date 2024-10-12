# ElevenLabsApiDocumentation.TextToSpeechApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**textToSpeechV1TextToSpeechVoiceIdPost**](TextToSpeechApi.md#textToSpeechV1TextToSpeechVoiceIdPost) | **POST** /v1/text-to-speech/{voice_id} | Text To Speech
[**textToSpeechV1TextToSpeechVoiceIdStreamPost**](TextToSpeechApi.md#textToSpeechV1TextToSpeechVoiceIdStreamPost) | **POST** /v1/text-to-speech/{voice_id}/stream | Text To Speech



## textToSpeechV1TextToSpeechVoiceIdPost

> textToSpeechV1TextToSpeechVoiceIdPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdPost, opts)

Text To Speech

Converts text into speech using a voice of your choice and returns audio.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.TextToSpeechApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let bodyTextToSpeechV1TextToSpeechVoiceIdPost = new ElevenLabsApiDocumentation.BodyTextToSpeechV1TextToSpeechVoiceIdPost(); // BodyTextToSpeechV1TextToSpeechVoiceIdPost | 
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.textToSpeechV1TextToSpeechVoiceIdPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdPost, opts, (error, data, response) => {
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
 **bodyTextToSpeechV1TextToSpeechVoiceIdPost** | [**BodyTextToSpeechV1TextToSpeechVoiceIdPost**](BodyTextToSpeechV1TextToSpeechVoiceIdPost.md)|  | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: audio/mpeg, application/json


## textToSpeechV1TextToSpeechVoiceIdStreamPost

> textToSpeechV1TextToSpeechVoiceIdStreamPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost, opts)

Text To Speech

Converts text into speech using a voice of your choice and returns audio as an audio stream.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.TextToSpeechApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost = new ElevenLabsApiDocumentation.BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost(); // BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost | 
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.textToSpeechV1TextToSpeechVoiceIdStreamPost(voiceId, bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost, opts, (error, data, response) => {
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
 **bodyTextToSpeechV1TextToSpeechVoiceIdStreamPost** | [**BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost**](BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost.md)|  | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

