# ElevenLabsApiDocumentation.VoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVoiceV1VoicesAddPost**](VoicesApi.md#addVoiceV1VoicesAddPost) | **POST** /v1/voices/add | Add Voice
[**deleteVoiceV1VoicesVoiceIdDelete**](VoicesApi.md#deleteVoiceV1VoicesVoiceIdDelete) | **DELETE** /v1/voices/{voice_id} | Delete Voice
[**editVoiceSettingsV1VoicesVoiceIdSettingsEditPost**](VoicesApi.md#editVoiceSettingsV1VoicesVoiceIdSettingsEditPost) | **POST** /v1/voices/{voice_id}/settings/edit | Edit Voice Settings
[**editVoiceV1VoicesVoiceIdEditPost**](VoicesApi.md#editVoiceV1VoicesVoiceIdEditPost) | **POST** /v1/voices/{voice_id}/edit | Edit Voice
[**getDefaultVoiceSettingsV1VoicesSettingsDefaultGet**](VoicesApi.md#getDefaultVoiceSettingsV1VoicesSettingsDefaultGet) | **GET** /v1/voices/settings/default | Get Default Voice Settings.
[**getVoiceSettingsV1VoicesVoiceIdSettingsGet**](VoicesApi.md#getVoiceSettingsV1VoicesVoiceIdSettingsGet) | **GET** /v1/voices/{voice_id}/settings | Get Voice Settings
[**getVoiceV1VoicesVoiceIdGet**](VoicesApi.md#getVoiceV1VoicesVoiceIdGet) | **GET** /v1/voices/{voice_id} | Get Voice
[**getVoicesV1VoicesGet**](VoicesApi.md#getVoicesV1VoicesGet) | **GET** /v1/voices | Get Voices



## addVoiceV1VoicesAddPost

> AddVoiceResponseModel addVoiceV1VoicesAddPost(files, name, opts)

Add Voice

Add a new voice to your collection of voices in VoiceLab.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let files = ["null"]; // [File] | One or more audio files to clone the voice from
let name = "name_example"; // String | The name that identifies this voice. This will be displayed in the dropdown of the website.
let opts = {
  'xiApiKey': "xiApiKey_example", // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
  'description': "description_example", // String | How would you describe the voice?
  'labels': "labels_example" // String | Serialized labels dictionary for the voice.
};
apiInstance.addVoiceV1VoicesAddPost(files, name, opts, (error, data, response) => {
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
 **files** | **[File]**| One or more audio files to clone the voice from | 
 **name** | **String**| The name that identifies this voice. This will be displayed in the dropdown of the website. | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 
 **description** | **String**| How would you describe the voice? | [optional] 
 **labels** | **String**| Serialized labels dictionary for the voice. | [optional] 

### Return type

[**AddVoiceResponseModel**](AddVoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## deleteVoiceV1VoicesVoiceIdDelete

> Object deleteVoiceV1VoicesVoiceIdDelete(voiceId, opts)

Delete Voice

Deletes a voice by its ID.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.deleteVoiceV1VoicesVoiceIdDelete(voiceId, opts, (error, data, response) => {
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
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editVoiceSettingsV1VoicesVoiceIdSettingsEditPost

> Object editVoiceSettingsV1VoicesVoiceIdSettingsEditPost(voiceId, voiceSettingsResponseModel, opts)

Edit Voice Settings

Edit your settings for a specific voice. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let voiceSettingsResponseModel = new ElevenLabsApiDocumentation.VoiceSettingsResponseModel(); // VoiceSettingsResponseModel | 
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.editVoiceSettingsV1VoicesVoiceIdSettingsEditPost(voiceId, voiceSettingsResponseModel, opts, (error, data, response) => {
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
 **voiceSettingsResponseModel** | [**VoiceSettingsResponseModel**](VoiceSettingsResponseModel.md)|  | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## editVoiceV1VoicesVoiceIdEditPost

> Object editVoiceV1VoicesVoiceIdEditPost(voiceId, name, opts)

Edit Voice

Edit a voice created by you.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let name = "name_example"; // String | The name that identifies this voice. This will be displayed in the dropdown of the website.
let opts = {
  'xiApiKey': "xiApiKey_example", // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
  'description': "description_example", // String | How would you describe the voice?
  'files': ["null"], // [File] | Audio files to add to the voice
  'labels': "labels_example" // String | Serialized labels dictionary for the voice.
};
apiInstance.editVoiceV1VoicesVoiceIdEditPost(voiceId, name, opts, (error, data, response) => {
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
 **name** | **String**| The name that identifies this voice. This will be displayed in the dropdown of the website. | 
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 
 **description** | **String**| How would you describe the voice? | [optional] 
 **files** | **[File]**| Audio files to add to the voice | [optional] 
 **labels** | **String**| Serialized labels dictionary for the voice. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## getDefaultVoiceSettingsV1VoicesSettingsDefaultGet

> VoiceSettingsResponseModel getDefaultVoiceSettingsV1VoicesSettingsDefaultGet()

Get Default Voice Settings.

Gets the default settings for voices. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
apiInstance.getDefaultVoiceSettingsV1VoicesSettingsDefaultGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**VoiceSettingsResponseModel**](VoiceSettingsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceSettingsV1VoicesVoiceIdSettingsGet

> VoiceSettingsResponseModel getVoiceSettingsV1VoicesVoiceIdSettingsGet(voiceId, opts)

Get Voice Settings

Returns the settings for a specific voice. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getVoiceSettingsV1VoicesVoiceIdSettingsGet(voiceId, opts, (error, data, response) => {
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
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

[**VoiceSettingsResponseModel**](VoiceSettingsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceV1VoicesVoiceIdGet

> VoiceResponseModel getVoiceV1VoicesVoiceIdGet(voiceId, opts)

Get Voice

Returns metadata about a specific voice.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let voiceId = "21m00Tcm4TlvDq8ikWAM"; // String | Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
let opts = {
  'withSettings': false, // Boolean | If set will return settings information corresponding to the voice, requires authorization.
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getVoiceV1VoicesVoiceIdGet(voiceId, opts, (error, data, response) => {
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
 **withSettings** | **Boolean**| If set will return settings information corresponding to the voice, requires authorization. | [optional] [default to false]
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

[**VoiceResponseModel**](VoiceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoicesV1VoicesGet

> GetVoicesResponseModel getVoicesV1VoicesGet(opts)

Get Voices

Gets a list of all available voices for a user.

### Example

```javascript
import ElevenLabsApiDocumentation from 'eleven_labs_api_documentation';

let apiInstance = new ElevenLabsApiDocumentation.VoicesApi();
let opts = {
  'xiApiKey': "xiApiKey_example" // String | Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the 'Profile' tab on the website.
};
apiInstance.getVoicesV1VoicesGet(opts, (error, data, response) => {
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
 **xiApiKey** | **String**| Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website. | [optional] 

### Return type

[**GetVoicesResponseModel**](GetVoicesResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

