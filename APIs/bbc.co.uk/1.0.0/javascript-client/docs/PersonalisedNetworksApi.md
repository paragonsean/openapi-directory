# RadioMusicServices.PersonalisedNetworksApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**myNetworksFollowsDelete**](PersonalisedNetworksApi.md#myNetworksFollowsDelete) | **DELETE** /my/networks/follows | Unfollow network
[**myNetworksFollowsGet**](PersonalisedNetworksApi.md#myNetworksFollowsGet) | **GET** /my/networks/follows | List of followed networks
[**myNetworksFollowsPost**](PersonalisedNetworksApi.md#myNetworksFollowsPost) | **POST** /my/networks/follows | Follow network



## myNetworksFollowsDelete

> myNetworksFollowsDelete(authorization, xAPIKey, body, opts)

Unfollow network

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedNetworksApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = new RadioMusicServices.Body3(); // Body3 | 
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.myNetworksFollowsDelete(authorization, xAPIKey, body, opts, (error, data, response) => {
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
 **body** | [**Body3**](Body3.md)|  | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## myNetworksFollowsGet

> PersonalisedNetworksResponse myNetworksFollowsGet(authorization, xAPIKey, opts)

List of followed networks

List of followed networks for a given user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedNetworksApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.myNetworksFollowsGet(authorization, xAPIKey, opts, (error, data, response) => {
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
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PersonalisedNetworksResponse**](PersonalisedNetworksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## myNetworksFollowsPost

> myNetworksFollowsPost(authorization, xAPIKey, body, opts)

Follow network

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PersonalisedNetworksApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = new RadioMusicServices.Body2(); // Body2 | 
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.myNetworksFollowsPost(authorization, xAPIKey, body, opts, (error, data, response) => {
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
 **body** | [**Body2**](Body2.md)|  | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

