# RadioMusicServices.PlayspaceApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getContainer**](PlayspaceApi.md#getContainer) | **GET** /my/playspace/containers/{id} | Playspace Container by ID
[**suggestContainer**](PlayspaceApi.md#suggestContainer) | **GET** /my/playspace/containers/suggested | Suggested Playspace Container



## getContainer

> PlayspaceContainer getContainer(authorization, xAPIKey, id)

Playspace Container by ID

Playspace Container by ID 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PlayspaceApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let id = "id_example"; // String | Playspace Container ID
apiInstance.getContainer(authorization, xAPIKey, id, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **id** | **String**| Playspace Container ID | 

### Return type

[**PlayspaceContainer**](PlayspaceContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suggestContainer

> PlayspaceContainer suggestContainer(authorization, xAPIKey, previousPid, opts)

Suggested Playspace Container

Suggested Playspace Container 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PlayspaceApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let previousPid = "previousPid_example"; // String | Clip or Episode PID of the previous or first content item in the Playspace stream.
let opts = {
  'previousContainer': "previousContainer_example" // String | Container ID of the previous container in the Playspace stream.
};
apiInstance.suggestContainer(authorization, xAPIKey, previousPid, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **previousPid** | **String**| Clip or Episode PID of the previous or first content item in the Playspace stream. | 
 **previousContainer** | **String**| Container ID of the previous container in the Playspace stream. | [optional] 

### Return type

[**PlayspaceContainer**](PlayspaceContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

