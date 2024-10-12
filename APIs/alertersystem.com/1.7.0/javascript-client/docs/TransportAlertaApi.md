# AlerterSystemApi.TransportAlertaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportAlertaGetCollection**](TransportAlertaApi.md#apiTransportAlertaGetCollection) | **GET** /api/transport-alerta | Retrieves the collection of TransportAlerta resources.
[**apiTransportAlertaIdDelete**](TransportAlertaApi.md#apiTransportAlertaIdDelete) | **DELETE** /api/transport-alerta/{id} | Removes the TransportAlerta resource.
[**apiTransportAlertaIdGet**](TransportAlertaApi.md#apiTransportAlertaIdGet) | **GET** /api/transport-alerta/{id} | Retrieves a TransportAlerta resource.
[**apiTransportAlertaIdPatch**](TransportAlertaApi.md#apiTransportAlertaIdPatch) | **PATCH** /api/transport-alerta/{id} | Updates the TransportAlerta resource.
[**apiTransportAlertaIdPut**](TransportAlertaApi.md#apiTransportAlertaIdPut) | **PUT** /api/transport-alerta/{id} | Replaces the TransportAlerta resource.
[**apiTransportAlertaPost**](TransportAlertaApi.md#apiTransportAlertaPost) | **POST** /api/transport-alerta | Creates a TransportAlerta resource.



## apiTransportAlertaGetCollection

> [TransportAlertaGet] apiTransportAlertaGetCollection(opts)

Retrieves the collection of TransportAlerta resources.

Retrieves the collection of TransportAlerta resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAlertaApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportAlertaGetCollection(opts, (error, data, response) => {
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

[**[TransportAlertaGet]**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAlertaIdDelete

> apiTransportAlertaIdDelete(id)

Removes the TransportAlerta resource.

Removes the TransportAlerta resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAlertaApi();
let id = "id_example"; // String | TransportAlerta identifier
apiInstance.apiTransportAlertaIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportAlerta identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportAlertaIdGet

> TransportAlertaGet apiTransportAlertaIdGet(id)

Retrieves a TransportAlerta resource.

Retrieves a TransportAlerta resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAlertaApi();
let id = "id_example"; // String | TransportAlerta identifier
apiInstance.apiTransportAlertaIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportAlerta identifier | 

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAlertaIdPatch

> TransportAlertaGet apiTransportAlertaIdPatch(id, transportAlertaPatch)

Updates the TransportAlerta resource.

Updates the TransportAlerta resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAlertaApi();
let id = "id_example"; // String | TransportAlerta identifier
let transportAlertaPatch = new AlerterSystemApi.TransportAlertaPatch(); // TransportAlertaPatch | The updated TransportAlerta resource
apiInstance.apiTransportAlertaIdPatch(id, transportAlertaPatch, (error, data, response) => {
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
 **id** | **String**| TransportAlerta identifier | 
 **transportAlertaPatch** | [**TransportAlertaPatch**](TransportAlertaPatch.md)| The updated TransportAlerta resource | 

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAlertaIdPut

> TransportAlertaGet apiTransportAlertaIdPut(id, transportAlertaPut)

Replaces the TransportAlerta resource.

Replaces the TransportAlerta resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAlertaApi();
let id = "id_example"; // String | TransportAlerta identifier
let transportAlertaPut = new AlerterSystemApi.TransportAlertaPut(); // TransportAlertaPut | The updated TransportAlerta resource
apiInstance.apiTransportAlertaIdPut(id, transportAlertaPut, (error, data, response) => {
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
 **id** | **String**| TransportAlerta identifier | 
 **transportAlertaPut** | [**TransportAlertaPut**](TransportAlertaPut.md)| The updated TransportAlerta resource | 

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportAlertaPost

> TransportAlertaGet apiTransportAlertaPost(transportAlertaPost)

Creates a TransportAlerta resource.

Creates a TransportAlerta resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportAlertaApi();
let transportAlertaPost = new AlerterSystemApi.TransportAlertaPost(); // TransportAlertaPost | The new TransportAlerta resource
apiInstance.apiTransportAlertaPost(transportAlertaPost, (error, data, response) => {
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
 **transportAlertaPost** | [**TransportAlertaPost**](TransportAlertaPost.md)| The new TransportAlerta resource | 

### Return type

[**TransportAlertaGet**](TransportAlertaGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

