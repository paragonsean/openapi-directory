# AlerterSystemApi.TransportFortySixElksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportFortySixElksGetCollection**](TransportFortySixElksApi.md#apiTransportFortySixElksGetCollection) | **GET** /api/transport-forty-six-elks | Retrieves the collection of TransportFortySixElks resources.
[**apiTransportFortySixElksIdDelete**](TransportFortySixElksApi.md#apiTransportFortySixElksIdDelete) | **DELETE** /api/transport-forty-six-elks/{id} | Removes the TransportFortySixElks resource.
[**apiTransportFortySixElksIdGet**](TransportFortySixElksApi.md#apiTransportFortySixElksIdGet) | **GET** /api/transport-forty-six-elks/{id} | Retrieves a TransportFortySixElks resource.
[**apiTransportFortySixElksIdPatch**](TransportFortySixElksApi.md#apiTransportFortySixElksIdPatch) | **PATCH** /api/transport-forty-six-elks/{id} | Updates the TransportFortySixElks resource.
[**apiTransportFortySixElksIdPut**](TransportFortySixElksApi.md#apiTransportFortySixElksIdPut) | **PUT** /api/transport-forty-six-elks/{id} | Replaces the TransportFortySixElks resource.
[**apiTransportFortySixElksPost**](TransportFortySixElksApi.md#apiTransportFortySixElksPost) | **POST** /api/transport-forty-six-elks | Creates a TransportFortySixElks resource.



## apiTransportFortySixElksGetCollection

> [TransportFortySixElksGet] apiTransportFortySixElksGetCollection(opts)

Retrieves the collection of TransportFortySixElks resources.

Retrieves the collection of TransportFortySixElks resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFortySixElksApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportFortySixElksGetCollection(opts, (error, data, response) => {
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

[**[TransportFortySixElksGet]**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFortySixElksIdDelete

> apiTransportFortySixElksIdDelete(id)

Removes the TransportFortySixElks resource.

Removes the TransportFortySixElks resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFortySixElksApi();
let id = "id_example"; // String | TransportFortySixElks identifier
apiInstance.apiTransportFortySixElksIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportFortySixElks identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportFortySixElksIdGet

> TransportFortySixElksGet apiTransportFortySixElksIdGet(id)

Retrieves a TransportFortySixElks resource.

Retrieves a TransportFortySixElks resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFortySixElksApi();
let id = "id_example"; // String | TransportFortySixElks identifier
apiInstance.apiTransportFortySixElksIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportFortySixElks identifier | 

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFortySixElksIdPatch

> TransportFortySixElksGet apiTransportFortySixElksIdPatch(id, transportFortySixElksPatch)

Updates the TransportFortySixElks resource.

Updates the TransportFortySixElks resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFortySixElksApi();
let id = "id_example"; // String | TransportFortySixElks identifier
let transportFortySixElksPatch = new AlerterSystemApi.TransportFortySixElksPatch(); // TransportFortySixElksPatch | The updated TransportFortySixElks resource
apiInstance.apiTransportFortySixElksIdPatch(id, transportFortySixElksPatch, (error, data, response) => {
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
 **id** | **String**| TransportFortySixElks identifier | 
 **transportFortySixElksPatch** | [**TransportFortySixElksPatch**](TransportFortySixElksPatch.md)| The updated TransportFortySixElks resource | 

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFortySixElksIdPut

> TransportFortySixElksGet apiTransportFortySixElksIdPut(id, transportFortySixElksPut)

Replaces the TransportFortySixElks resource.

Replaces the TransportFortySixElks resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFortySixElksApi();
let id = "id_example"; // String | TransportFortySixElks identifier
let transportFortySixElksPut = new AlerterSystemApi.TransportFortySixElksPut(); // TransportFortySixElksPut | The updated TransportFortySixElks resource
apiInstance.apiTransportFortySixElksIdPut(id, transportFortySixElksPut, (error, data, response) => {
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
 **id** | **String**| TransportFortySixElks identifier | 
 **transportFortySixElksPut** | [**TransportFortySixElksPut**](TransportFortySixElksPut.md)| The updated TransportFortySixElks resource | 

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportFortySixElksPost

> TransportFortySixElksGet apiTransportFortySixElksPost(transportFortySixElksPost)

Creates a TransportFortySixElks resource.

Creates a TransportFortySixElks resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportFortySixElksApi();
let transportFortySixElksPost = new AlerterSystemApi.TransportFortySixElksPost(); // TransportFortySixElksPost | The new TransportFortySixElks resource
apiInstance.apiTransportFortySixElksPost(transportFortySixElksPost, (error, data, response) => {
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
 **transportFortySixElksPost** | [**TransportFortySixElksPost**](TransportFortySixElksPost.md)| The new TransportFortySixElks resource | 

### Return type

[**TransportFortySixElksGet**](TransportFortySixElksGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

