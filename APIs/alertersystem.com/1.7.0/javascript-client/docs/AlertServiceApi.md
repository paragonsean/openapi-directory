# AlerterSystemApi.AlertServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiAlertServiceGetCollection**](AlertServiceApi.md#apiAlertServiceGetCollection) | **GET** /api/alert-service | Retrieves the collection of AlertService resources.
[**apiAlertServiceIdDelete**](AlertServiceApi.md#apiAlertServiceIdDelete) | **DELETE** /api/alert-service/{id} | Removes the AlertService resource.
[**apiAlertServiceIdGet**](AlertServiceApi.md#apiAlertServiceIdGet) | **GET** /api/alert-service/{id} | Retrieves a AlertService resource.
[**apiAlertServiceIdPatch**](AlertServiceApi.md#apiAlertServiceIdPatch) | **PATCH** /api/alert-service/{id} | Updates the AlertService resource.
[**apiAlertServiceIdPut**](AlertServiceApi.md#apiAlertServiceIdPut) | **PUT** /api/alert-service/{id} | Replaces the AlertService resource.
[**apiAlertServicePost**](AlertServiceApi.md#apiAlertServicePost) | **POST** /api/alert-service | Creates a AlertService resource.



## apiAlertServiceGetCollection

> [AlertServiceGet] apiAlertServiceGetCollection(opts)

Retrieves the collection of AlertService resources.

Retrieves the collection of AlertService resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiAlertServiceGetCollection(opts, (error, data, response) => {
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

[**[AlertServiceGet]**](AlertServiceGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiAlertServiceIdDelete

> apiAlertServiceIdDelete(id)

Removes the AlertService resource.

Removes the AlertService resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceApi();
let id = "id_example"; // String | AlertService identifier
apiInstance.apiAlertServiceIdDelete(id, (error, data, response) => {
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
 **id** | **String**| AlertService identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiAlertServiceIdGet

> AlertServiceGet apiAlertServiceIdGet(id)

Retrieves a AlertService resource.

Retrieves a AlertService resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceApi();
let id = "id_example"; // String | AlertService identifier
apiInstance.apiAlertServiceIdGet(id, (error, data, response) => {
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
 **id** | **String**| AlertService identifier | 

### Return type

[**AlertServiceGet**](AlertServiceGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiAlertServiceIdPatch

> AlertServiceGet apiAlertServiceIdPatch(id, alertServicePatch)

Updates the AlertService resource.

Updates the AlertService resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceApi();
let id = "id_example"; // String | AlertService identifier
let alertServicePatch = new AlerterSystemApi.AlertServicePatch(); // AlertServicePatch | The updated AlertService resource
apiInstance.apiAlertServiceIdPatch(id, alertServicePatch, (error, data, response) => {
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
 **id** | **String**| AlertService identifier | 
 **alertServicePatch** | [**AlertServicePatch**](AlertServicePatch.md)| The updated AlertService resource | 

### Return type

[**AlertServiceGet**](AlertServiceGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiAlertServiceIdPut

> AlertServiceGet apiAlertServiceIdPut(id, alertServicePut)

Replaces the AlertService resource.

Replaces the AlertService resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceApi();
let id = "id_example"; // String | AlertService identifier
let alertServicePut = new AlerterSystemApi.AlertServicePut(); // AlertServicePut | The updated AlertService resource
apiInstance.apiAlertServiceIdPut(id, alertServicePut, (error, data, response) => {
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
 **id** | **String**| AlertService identifier | 
 **alertServicePut** | [**AlertServicePut**](AlertServicePut.md)| The updated AlertService resource | 

### Return type

[**AlertServiceGet**](AlertServiceGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiAlertServicePost

> AlertServiceGet apiAlertServicePost(alertServicePost)

Creates a AlertService resource.

Creates a AlertService resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.AlertServiceApi();
let alertServicePost = new AlerterSystemApi.AlertServicePost(); // AlertServicePost | The new AlertService resource
apiInstance.apiAlertServicePost(alertServicePost, (error, data, response) => {
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
 **alertServicePost** | [**AlertServicePost**](AlertServicePost.md)| The new AlertService resource | 

### Return type

[**AlertServiceGet**](AlertServiceGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

