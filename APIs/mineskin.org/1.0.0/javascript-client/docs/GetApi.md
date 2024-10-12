# MineSkinApi.GetApi

All URIs are relative to *https://api.mineskin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDelayGet**](GetApi.md#getDelayGet) | **GET** /get/delay | 
[**getIdIdGet**](GetApi.md#getIdIdGet) | **GET** /get/id/{id} | 
[**getListPageGet**](GetApi.md#getListPageGet) | **GET** /get/list/{page} | 
[**getUuidUuidGet**](GetApi.md#getUuidUuidGet) | **GET** /get/uuid/{uuid} | 



## getDelayGet

> GetDelayGet200Response getDelayGet(userAgent)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';
let defaultClient = MineSkinApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new MineSkinApi.GetApi();
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
apiInstance.getDelayGet(userAgent, (error, data, response) => {
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
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 

### Return type

[**GetDelayGet200Response**](GetDelayGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIdIdGet

> SkinInfo getIdIdGet(id, userAgent)



Deprecated. Use /get/uuid instead.

### Example

```javascript
import MineSkinApi from 'mine_skin_api';

let apiInstance = new MineSkinApi.GetApi();
let id = 3.4; // Number | 
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
apiInstance.getIdIdGet(id, userAgent, (error, data, response) => {
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
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 

### Return type

[**SkinInfo**](SkinInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListPageGet

> GetListPageGet200Response getListPageGet(page, userAgent)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';

let apiInstance = new MineSkinApi.GetApi();
let page = 3.4; // Number | For reference pagination, the uuid of the last skin in the previous page. For numeric pagination (deprecated), the page number or 'start'.
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
apiInstance.getListPageGet(page, userAgent, (error, data, response) => {
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
 **page** | **Number**| For reference pagination, the uuid of the last skin in the previous page. For numeric pagination (deprecated), the page number or &#39;start&#39;. | 
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 

### Return type

[**GetListPageGet200Response**](GetListPageGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUuidUuidGet

> SkinInfo getUuidUuidGet(uuid, userAgent)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';

let apiInstance = new MineSkinApi.GetApi();
let uuid = "uuid_example"; // String | 
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
apiInstance.getUuidUuidGet(uuid, userAgent, (error, data, response) => {
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
 **uuid** | **String**|  | 
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 

### Return type

[**SkinInfo**](SkinInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

