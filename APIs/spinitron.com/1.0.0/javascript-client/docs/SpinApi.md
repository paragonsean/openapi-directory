# SpinitronV2Api.SpinApi

All URIs are relative to *https://spinitron.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spinsGet**](SpinApi.md#spinsGet) | **GET** /spins | Returns spins optionally filtered by {start} and/or {end} datetimes
[**spinsIdGet**](SpinApi.md#spinsIdGet) | **GET** /spins/{id} | Get a Spin by id
[**spinsPost**](SpinApi.md#spinsPost) | **POST** /spins | Log a Spin



## spinsGet

> SpinsGet200Response spinsGet(opts)

Returns spins optionally filtered by {start} and/or {end} datetimes

Get Spins optionally filtered by a datetime range. Only past Spins will be returned. 

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.SpinApi();
let opts = {
  'start': new Date("2013-10-20T19:20:30+01:00"), // Date | The datetime starting from items must be returned. 
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | The ending datetime. 
  'playlistId': 56, // Number | Filter by playlist
  'showId': 56, // Number | Filter by show
  'count': 20, // Number | Amount of items to return
  'page': 56, // Number | Offset, used together with count
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.spinsGet(opts, (error, data, response) => {
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
 **start** | **Date**| The datetime starting from items must be returned.  | [optional] 
 **end** | **Date**| The ending datetime.  | [optional] 
 **playlistId** | **Number**| Filter by playlist | [optional] 
 **showId** | **Number**| Filter by show | [optional] 
 **count** | **Number**| Amount of items to return | [optional] [default to 20]
 **page** | **Number**| Offset, used together with count | [optional] 
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**SpinsGet200Response**](SpinsGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## spinsIdGet

> Spin spinsIdGet(id, opts)

Get a Spin by id

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.SpinApi();
let id = 56; // Number | 
let opts = {
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.spinsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**Spin**](Spin.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## spinsPost

> Spin spinsPost(artist, song, opts)

Log a Spin

An endpoint for automation systems to log spins into the spin table.

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.SpinApi();
let artist = "artist_example"; // String | 
let song = "song_example"; // String | 
let opts = {
  'composer': "composer_example", // String | 
  'duration': 56, // Number | 
  'genre': "genre_example", // String | 
  'isrc': "isrc_example", // String | 
  'label': "label_example", // String | 
  'live': true, // Boolean | Only when automation params are configured with the \\\"Pass through\\\" mode. Enables \\\"live assist\\\" mode. Default mode is \\\"full automation\\\". 
  'release': "release_example", // String | 
  'start': new Date("2013-10-20T19:20:30+01:00") // Date | 
};
apiInstance.spinsPost(artist, song, opts, (error, data, response) => {
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
 **artist** | **String**|  | 
 **song** | **String**|  | 
 **composer** | **String**|  | [optional] 
 **duration** | **Number**|  | [optional] 
 **genre** | **String**|  | [optional] 
 **isrc** | **String**|  | [optional] 
 **label** | **String**|  | [optional] 
 **live** | **Boolean**| Only when automation params are configured with the \\\&quot;Pass through\\\&quot; mode. Enables \\\&quot;live assist\\\&quot; mode. Default mode is \\\&quot;full automation\\\&quot;.  | [optional] 
 **release** | **String**|  | [optional] 
 **start** | **Date**|  | [optional] 

### Return type

[**Spin**](Spin.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

