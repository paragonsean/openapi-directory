# CallFireApiDocumentation.CampaignsApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCampaignSound**](CampaignsApi.md#deleteCampaignSound) | **DELETE** /campaigns/sounds/{id} | Delete a specific sound
[**findCampaignSounds**](CampaignsApi.md#findCampaignSounds) | **GET** /campaigns/sounds | Find sounds
[**getCampaignBatch**](CampaignsApi.md#getCampaignBatch) | **GET** /campaigns/batches/{id} | Find a specific batch
[**getCampaignSound**](CampaignsApi.md#getCampaignSound) | **GET** /campaigns/sounds/{id} | Find a specific sound
[**getCampaignSoundDataMp3**](CampaignsApi.md#getCampaignSoundDataMp3) | **GET** /campaigns/sounds/{id}.mp3 | Download a MP3 sound
[**getCampaignSoundDataWav**](CampaignsApi.md#getCampaignSoundDataWav) | **GET** /campaigns/sounds/{id}.wav | Download a WAV sound
[**postCallCampaignSound**](CampaignsApi.md#postCallCampaignSound) | **POST** /campaigns/sounds/calls | Add sound via call
[**postFileCampaignSound**](CampaignsApi.md#postFileCampaignSound) | **POST** /campaigns/sounds/files | Add sound via file
[**postTTSCampaignSound**](CampaignsApi.md#postTTSCampaignSound) | **POST** /campaigns/sounds/tts | Add sound via text-to-speech
[**updateCampaignBatch**](CampaignsApi.md#updateCampaignBatch) | **PUT** /campaigns/batches/{id} | Update a batch



## deleteCampaignSound

> deleteCampaignSound(id)

Delete a specific sound

Deletes a single campaign sound instance for a specific campaign sound id, this operation does not delete sound completely, it sets sound status to ARCHIVED which means that sound will no longer appear in &#39;find&#39; operation results, but still accessible via &#39;get&#39; operation

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let id = 789; // Number | An id of a campaign sound
apiInstance.deleteCampaignSound(id, (error, data, response) => {
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
 **id** | **Number**| An id of a campaign sound | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCampaignSounds

> CampaignSoundPage findCampaignSounds(opts)

Find sounds

To find all campaign sounds which were created by user. Returns all sounds available to be used in campaigns

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let opts = {
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'filter': "filter_example", // String | value to filter file names again; this value is used to check if the filename contains the filter value.
  'includeArchived': true, // Boolean | Includes ARCHIVED sounds for \"true\" value
  'includePending': true, // Boolean | Includes UPLOAD/RECORDING sounds for \"true\" value
  'includeScrubbed': true, // Boolean | Includes SCRUBBED sounds for \"true\" value
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findCampaignSounds(opts, (error, data, response) => {
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
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **filter** | **String**| value to filter file names again; this value is used to check if the filename contains the filter value. | [optional] 
 **includeArchived** | **Boolean**| Includes ARCHIVED sounds for \&quot;true\&quot; value | [optional] 
 **includePending** | **Boolean**| Includes UPLOAD/RECORDING sounds for \&quot;true\&quot; value | [optional] 
 **includeScrubbed** | **Boolean**| Includes SCRUBBED sounds for \&quot;true\&quot; value | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**CampaignSoundPage**](CampaignSoundPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignBatch

> Batch getCampaignBatch(id, opts)

Find a specific batch

Returns a single Batch instance for a given batch id. This API is useful for determining the state of a validating batch

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let id = 789; // Number | An id of a batch
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCampaignBatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a batch | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Batch**](Batch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignSound

> CampaignSound getCampaignSound(id, opts)

Find a specific sound

Returns a single CampaignSound instance for a given sound id in campaign. This is a meta data to the sounds. No audio data is returned from this API

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let id = 789; // Number | An id of a sound campaign
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCampaignSound(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a sound campaign | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**CampaignSound**](CampaignSound.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignSoundDataMp3

> Object getCampaignSoundDataMp3(id)

Download a MP3 sound

Download the MP3 version of a hosted file. This is an audio data endpoint. Returns binary response of the &#39;audio/mpeg&#39; content type

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let id = 789; // Number | An id of a campaign sound
apiInstance.getCampaignSoundDataMp3(id, (error, data, response) => {
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
 **id** | **Number**| An id of a campaign sound | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/mpeg


## getCampaignSoundDataWav

> Object getCampaignSoundDataWav(id)

Download a WAV sound

Download the WAV version of the hosted file. This is an audio data endpoint. Returns binary response of the &#39;audio/mpeg&#39; content type

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let id = 789; // Number | An id of a campaign sound
apiInstance.getCampaignSoundDataWav(id, (error, data, response) => {
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
 **id** | **Number**| An id of a campaign sound | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/wav


## postCallCampaignSound

> CampaignSound postCallCampaignSound(opts)

Add sound via call

Use this API to create a sound via a phone call. Provide the required phone number in the CallCreateSound object inside the request, and user will receive a call shortly after with instructions on how to record a sound over the phone.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'callCreateSound': new CallFireApiDocumentation.CallCreateSound() // CallCreateSound | Request object containing the name of a new campaign sound and phone number to call up
};
apiInstance.postCallCampaignSound(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **callCreateSound** | [**CallCreateSound**](CallCreateSound.md)| Request object containing the name of a new campaign sound and phone number to call up | [optional] 

### Return type

[**CampaignSound**](CampaignSound.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postFileCampaignSound

> CampaignSound postFileCampaignSound(file, opts)

Add sound via file

Create a campaign sound file via a supplied .mp3 or .wav file

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let file = "/path/to/file"; // File | A sound file encoded in binary form
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'name': "name_example" // String | Optional name of a sound file, if the name is empty than it will be taken from a file
};
apiInstance.postFileCampaignSound(file, opts, (error, data, response) => {
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
 **file** | **File**| A sound file encoded in binary form | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **name** | **String**| Optional name of a sound file, if the name is empty than it will be taken from a file | [optional] 

### Return type

[**CampaignSound**](CampaignSound.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postTTSCampaignSound

> CampaignSound postTTSCampaignSound(opts)

Add sound via text-to-speech

Use this API to create a sound file via a supplied string of text. Add a text in the TextToSpeech.message field, and pick a voice in the TextToSpeech.voice field. Available voices are: MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'textToSpeech': new CallFireApiDocumentation.TextToSpeech() // TextToSpeech | textToSpeech
};
apiInstance.postTTSCampaignSound(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **textToSpeech** | [**TextToSpeech**](TextToSpeech.md)| textToSpeech | [optional] 

### Return type

[**CampaignSound**](CampaignSound.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCampaignBatch

> updateCampaignBatch(id, opts)

Update a batch

Updates a single Batch instance, currently batch can only be turned \&quot;on/off\&quot;

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CampaignsApi();
let id = 789; // Number | An id of a batch to update
let opts = {
  'batch': new CallFireApiDocumentation.Batch() // Batch | A batch instance
};
apiInstance.updateCampaignBatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a batch to update | 
 **batch** | [**Batch**](Batch.md)| A batch instance | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

