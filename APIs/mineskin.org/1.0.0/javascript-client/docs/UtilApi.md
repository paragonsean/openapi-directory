# MineSkinApi.UtilApi

All URIs are relative to *https://api.mineskin.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validateNameNameGet**](UtilApi.md#validateNameNameGet) | **GET** /validate/name/{name} | 
[**validateUuidUuidGet**](UtilApi.md#validateUuidUuidGet) | **GET** /validate/uuid/{uuid} | 



## validateNameNameGet

> UserValidation validateNameNameGet(name, userAgent)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';

let apiInstance = new MineSkinApi.UtilApi();
let name = "name_example"; // String | 
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
apiInstance.validateNameNameGet(name, userAgent, (error, data, response) => {
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
 **name** | **String**|  | 
 **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | 

### Return type

[**UserValidation**](UserValidation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## validateUuidUuidGet

> UserValidation validateUuidUuidGet(uuid, userAgent)



### Example

```javascript
import MineSkinApi from 'mine_skin_api';

let apiInstance = new MineSkinApi.UtilApi();
let uuid = "uuid_example"; // String | 
let userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
apiInstance.validateUuidUuidGet(uuid, userAgent, (error, data, response) => {
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

[**UserValidation**](UserValidation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

