# ShutterstockApiExplorer.CustomMusicApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAudioRenders**](CustomMusicApi.md#createAudioRenders) | **POST** /v2/ai/audio/renders | Create rendered audio
[**fetchRenders**](CustomMusicApi.md#fetchRenders) | **GET** /v2/ai/audio/renders | Get details about audio renders
[**listCustomDescriptors**](CustomMusicApi.md#listCustomDescriptors) | **GET** /v2/ai/audio/descriptors | List computer audio descriptors
[**listCustomInstruments**](CustomMusicApi.md#listCustomInstruments) | **GET** /v2/ai/audio/instruments | List computer audio instruments



## createAudioRenders

> AudioRendersListResults createAudioRenders(createAudioRendersRequest)

Create rendered audio

This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.CustomMusicApi();
let createAudioRendersRequest = {"$ref":"#/components/schemas/CreateAudioRendersRequest/example"}; // CreateAudioRendersRequest | Parameters for the audio, including the timeline and information about the output file
apiInstance.createAudioRenders(createAudioRendersRequest, (error, data, response) => {
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
 **createAudioRendersRequest** | [**CreateAudioRendersRequest**](CreateAudioRendersRequest.md)| Parameters for the audio, including the timeline and information about the output file | 

### Return type

[**AudioRendersListResults**](AudioRendersListResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fetchRenders

> AudioRendersListResults fetchRenders(id)

Get details about audio renders

This endpoint shows the status of one or more audio renders, including download links for completed audio.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.CustomMusicApi();
let id = ["null"]; // [String] | One or more render IDs
apiInstance.fetchRenders(id, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| One or more render IDs | 

### Return type

[**AudioRendersListResults**](AudioRendersListResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomDescriptors

> DescriptorsListResult listCustomDescriptors(opts)

List computer audio descriptors

This endpoint lists the descriptors that you can use in the audio regions in an audio render.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.CustomMusicApi();
let opts = {
  'renderSpeedOver': 5, // Number | Show descriptors with an average render speed that is greater than or equal to the specified value
  'bandId': "Corporate Folk Bonfire Band 1", // String | Show descriptors that contain the specified band (case-sentsitive)
  'bandName': "Documentary Underscore Heartfelt Band 1", // String | Show descriptors with the specified band name (case-sensitive)
  'page': 1, // Number | Page number
  'perPage': 1, // Number | Number of results per page
  'id': ["null"], // [String] | Show descriptors with the specified IDs (case-sensitive)
  'instrumentName': "Precision Bass - Full", // String | Show descriptors with the specified instrument name (case-sensitive)
  'instrumentId': "direct_fluorescent_synth_lead", // String | Show descriptors with the specified instrument ID (case-sensitive)
  'tempo': 90, // Number | Show descriptors whose tempo range includes the specified tempo in beats per minute
  'tempoTo': 120, // Number | Show descriptors with a tempo that is less than or equal to the specified number
  'tempoFrom': 60, // Number | Show descriptors that have a tempo range that includes the specified tempo in beats per minute
  'name': "Corporate Pop Inspirational High Energy", // String | Show descriptors with the specified name (case-sensitive)
  'tag': "Cinematic" // String | Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive)
};
apiInstance.listCustomDescriptors(opts, (error, data, response) => {
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
 **renderSpeedOver** | **Number**| Show descriptors with an average render speed that is greater than or equal to the specified value | [optional] 
 **bandId** | **String**| Show descriptors that contain the specified band (case-sentsitive) | [optional] 
 **bandName** | **String**| Show descriptors with the specified band name (case-sensitive) | [optional] 
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **id** | [**[String]**](String.md)| Show descriptors with the specified IDs (case-sensitive) | [optional] 
 **instrumentName** | **String**| Show descriptors with the specified instrument name (case-sensitive) | [optional] 
 **instrumentId** | **String**| Show descriptors with the specified instrument ID (case-sensitive) | [optional] 
 **tempo** | **Number**| Show descriptors whose tempo range includes the specified tempo in beats per minute | [optional] 
 **tempoTo** | **Number**| Show descriptors with a tempo that is less than or equal to the specified number | [optional] 
 **tempoFrom** | **Number**| Show descriptors that have a tempo range that includes the specified tempo in beats per minute | [optional] 
 **name** | **String**| Show descriptors with the specified name (case-sensitive) | [optional] 
 **tag** | **String**| Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive) | [optional] 

### Return type

[**DescriptorsListResult**](DescriptorsListResult.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCustomInstruments

> InstrumentsListResult listCustomInstruments(opts)

List computer audio instruments

This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new ShutterstockApiExplorer.CustomMusicApi();
let opts = {
  'id': ["null"], // [String] | Show instruments with the specified ID
  'perPage': 1, // Number | Number of results per page
  'page': 1, // Number | Page number
  'name': "Precision Bass - Full", // String | Show instruments with the specified name (case-sensitive)
  'tag': "Percussion" // String | Show instruments with the specified tag, such as Percussion or Strings (case-sensitive)
};
apiInstance.listCustomInstruments(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Show instruments with the specified ID | [optional] 
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **page** | **Number**| Page number | [optional] [default to 1]
 **name** | **String**| Show instruments with the specified name (case-sensitive) | [optional] 
 **tag** | **String**| Show instruments with the specified tag, such as Percussion or Strings (case-sensitive) | [optional] 

### Return type

[**InstrumentsListResult**](InstrumentsListResult.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

