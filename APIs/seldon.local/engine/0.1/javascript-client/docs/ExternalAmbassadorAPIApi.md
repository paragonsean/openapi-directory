# SeldonExternalApi.ExternalAmbassadorAPIApi

All URIs are relative to *http://seldon.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict**](ExternalAmbassadorAPIApi.md#predict) | **POST** /seldon/{namespace}/{deployment}/api/v1.0/predictions | 
[**sendFeedback**](ExternalAmbassadorAPIApi.md#sendFeedback) | **POST** /seldon/{namespace}/{deployment}/api/v1.0/feedback | 



## predict

> SeldonMessage predict(namespace, deployment, seldonMessage)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';
let defaultClient = SeldonExternalApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SeldonExternalApi.ExternalAmbassadorAPIApi();
let namespace = "namespace_example"; // String | 
let deployment = "deployment_example"; // String | 
let seldonMessage = {"data":{"names":["feature1"],"tensor":{"shape":[1,1],"values":[1]}}}; // SeldonMessage | 
apiInstance.predict(namespace, deployment, seldonMessage, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **deployment** | **String**|  | 
 **seldonMessage** | [**SeldonMessage**](SeldonMessage.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, text/*
- **Accept**: application/json


## sendFeedback

> SeldonMessage sendFeedback(namespace, deployment, feedback)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';
let defaultClient = SeldonExternalApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SeldonExternalApi.ExternalAmbassadorAPIApi();
let namespace = "namespace_example"; // String | 
let deployment = "deployment_example"; // String | 
let feedback = new SeldonExternalApi.Feedback(); // Feedback | 
apiInstance.sendFeedback(namespace, deployment, feedback, (error, data, response) => {
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
 **namespace** | **String**|  | 
 **deployment** | **String**|  | 
 **feedback** | [**Feedback**](Feedback.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

