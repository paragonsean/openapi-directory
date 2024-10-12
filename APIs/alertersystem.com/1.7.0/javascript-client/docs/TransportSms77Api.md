# AlerterSystemApi.TransportSms77Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportSms77GetCollection**](TransportSms77Api.md#apiTransportSms77GetCollection) | **GET** /api/transport-sms77 | Retrieves the collection of TransportSms77 resources.
[**apiTransportSms77IdDelete**](TransportSms77Api.md#apiTransportSms77IdDelete) | **DELETE** /api/transport-sms77/{id} | Removes the TransportSms77 resource.
[**apiTransportSms77IdGet**](TransportSms77Api.md#apiTransportSms77IdGet) | **GET** /api/transport-sms77/{id} | Retrieves a TransportSms77 resource.
[**apiTransportSms77IdPatch**](TransportSms77Api.md#apiTransportSms77IdPatch) | **PATCH** /api/transport-sms77/{id} | Updates the TransportSms77 resource.
[**apiTransportSms77IdPut**](TransportSms77Api.md#apiTransportSms77IdPut) | **PUT** /api/transport-sms77/{id} | Replaces the TransportSms77 resource.
[**apiTransportSms77Post**](TransportSms77Api.md#apiTransportSms77Post) | **POST** /api/transport-sms77 | Creates a TransportSms77 resource.



## apiTransportSms77GetCollection

> [TransportSms77Get] apiTransportSms77GetCollection(opts)

Retrieves the collection of TransportSms77 resources.

Retrieves the collection of TransportSms77 resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSms77Api();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportSms77GetCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] [default to 1]
 **dataSegmentCode** | **String**|  | [optional] 
 **dataSegmentCode2** | [**[String]**](String.md)|  | [optional] 
 **partition** | **String**|  | [optional] 
 **partition2** | [**[String]**](String.md)|  | [optional] 
 **properties** | [**[String]**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] 

### Return type

[**[TransportSms77Get]**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSms77IdDelete

> apiTransportSms77IdDelete(id)

Removes the TransportSms77 resource.

Removes the TransportSms77 resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSms77Api();
let id = "id_example"; // String | TransportSms77 identifier
apiInstance.apiTransportSms77IdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportSms77 identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportSms77IdGet

> TransportSms77Get apiTransportSms77IdGet(id)

Retrieves a TransportSms77 resource.

Retrieves a TransportSms77 resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSms77Api();
let id = "id_example"; // String | TransportSms77 identifier
apiInstance.apiTransportSms77IdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportSms77 identifier | 

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSms77IdPatch

> TransportSms77Get apiTransportSms77IdPatch(id, transportSms77Patch)

Updates the TransportSms77 resource.

Updates the TransportSms77 resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSms77Api();
let id = "id_example"; // String | TransportSms77 identifier
let transportSms77Patch = new AlerterSystemApi.TransportSms77Patch(); // TransportSms77Patch | The updated TransportSms77 resource
apiInstance.apiTransportSms77IdPatch(id, transportSms77Patch, (error, data, response) => {
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
 **id** | **String**| TransportSms77 identifier | 
 **transportSms77Patch** | [**TransportSms77Patch**](TransportSms77Patch.md)| The updated TransportSms77 resource | 

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSms77IdPut

> TransportSms77Get apiTransportSms77IdPut(id, transportSms77Put)

Replaces the TransportSms77 resource.

Replaces the TransportSms77 resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSms77Api();
let id = "id_example"; // String | TransportSms77 identifier
let transportSms77Put = new AlerterSystemApi.TransportSms77Put(); // TransportSms77Put | The updated TransportSms77 resource
apiInstance.apiTransportSms77IdPut(id, transportSms77Put, (error, data, response) => {
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
 **id** | **String**| TransportSms77 identifier | 
 **transportSms77Put** | [**TransportSms77Put**](TransportSms77Put.md)| The updated TransportSms77 resource | 

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportSms77Post

> TransportSms77Get apiTransportSms77Post(transportSms77Post)

Creates a TransportSms77 resource.

Creates a TransportSms77 resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportSms77Api();
let transportSms77Post = new AlerterSystemApi.TransportSms77Post(); // TransportSms77Post | The new TransportSms77 resource
apiInstance.apiTransportSms77Post(transportSms77Post, (error, data, response) => {
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
 **transportSms77Post** | [**TransportSms77Post**](TransportSms77Post.md)| The new TransportSms77 resource | 

### Return type

[**TransportSms77Get**](TransportSms77Get.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

