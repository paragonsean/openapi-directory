# FastApi.DefaultApi

All URIs are relative to *http://botschaft.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configConfigGet**](DefaultApi.md#configConfigGet) | **GET** /config | Config
[**topicTopicTopicNameGet**](DefaultApi.md#topicTopicTopicNameGet) | **GET** /topic/{topic_name} | Topic



## configConfigGet

> Config configConfigGet(opts)

Config

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let opts = {
  'authorization': "authorization_example" // String | 
};
apiInstance.configConfigGet(opts, (error, data, response) => {
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
 **authorization** | **String**|  | [optional] 

### Return type

[**Config**](Config.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicTopicTopicNameGet

> Object topicTopicTopicNameGet(topicName, opts)

Topic

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.DefaultApi();
let topicName = "topicName_example"; // String | 
let opts = {
  'message': "message_example", // String | 
  'base64Message': "base64Message_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.topicTopicTopicNameGet(topicName, opts, (error, data, response) => {
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
 **topicName** | **String**|  | 
 **message** | **String**|  | [optional] 
 **base64Message** | **String**|  | [optional] 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

