# RadioMusicServices.PersonalisedPlaysApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**myPlaysPost**](PersonalisedPlaysApi.md#myPlaysPost) | **POST** /my/plays | Write Play Event



## myPlaysPost

> myPlaysPost(authorization, xAPIKey, body)

Write Play Event

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedPlaysApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = new RadioMusicServices.Body4(); // Body4 | 
apiInstance.myPlaysPost(authorization, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**Body4**](Body4.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

