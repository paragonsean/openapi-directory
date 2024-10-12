# AlerterSystemApi.TransportGatewayApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportGatewayApiGetCollection**](TransportGatewayApiApi.md#apiTransportGatewayApiGetCollection) | **GET** /api/transport-gateway-api | Retrieves the collection of TransportGatewayApi resources.
[**apiTransportGatewayApiIdDelete**](TransportGatewayApiApi.md#apiTransportGatewayApiIdDelete) | **DELETE** /api/transport-gateway-api/{id} | Removes the TransportGatewayApi resource.
[**apiTransportGatewayApiIdGet**](TransportGatewayApiApi.md#apiTransportGatewayApiIdGet) | **GET** /api/transport-gateway-api/{id} | Retrieves a TransportGatewayApi resource.
[**apiTransportGatewayApiIdPatch**](TransportGatewayApiApi.md#apiTransportGatewayApiIdPatch) | **PATCH** /api/transport-gateway-api/{id} | Updates the TransportGatewayApi resource.
[**apiTransportGatewayApiIdPut**](TransportGatewayApiApi.md#apiTransportGatewayApiIdPut) | **PUT** /api/transport-gateway-api/{id} | Replaces the TransportGatewayApi resource.
[**apiTransportGatewayApiPost**](TransportGatewayApiApi.md#apiTransportGatewayApiPost) | **POST** /api/transport-gateway-api | Creates a TransportGatewayApi resource.



## apiTransportGatewayApiGetCollection

> [TransportGatewayApiGet] apiTransportGatewayApiGetCollection(opts)

Retrieves the collection of TransportGatewayApi resources.

Retrieves the collection of TransportGatewayApi resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGatewayApiApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportGatewayApiGetCollection(opts, (error, data, response) => {
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

[**[TransportGatewayApiGet]**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGatewayApiIdDelete

> apiTransportGatewayApiIdDelete(id)

Removes the TransportGatewayApi resource.

Removes the TransportGatewayApi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGatewayApiApi();
let id = "id_example"; // String | TransportGatewayApi identifier
apiInstance.apiTransportGatewayApiIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportGatewayApi identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportGatewayApiIdGet

> TransportGatewayApiGet apiTransportGatewayApiIdGet(id)

Retrieves a TransportGatewayApi resource.

Retrieves a TransportGatewayApi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGatewayApiApi();
let id = "id_example"; // String | TransportGatewayApi identifier
apiInstance.apiTransportGatewayApiIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportGatewayApi identifier | 

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGatewayApiIdPatch

> TransportGatewayApiGet apiTransportGatewayApiIdPatch(id, transportGatewayApiPatch)

Updates the TransportGatewayApi resource.

Updates the TransportGatewayApi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGatewayApiApi();
let id = "id_example"; // String | TransportGatewayApi identifier
let transportGatewayApiPatch = new AlerterSystemApi.TransportGatewayApiPatch(); // TransportGatewayApiPatch | The updated TransportGatewayApi resource
apiInstance.apiTransportGatewayApiIdPatch(id, transportGatewayApiPatch, (error, data, response) => {
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
 **id** | **String**| TransportGatewayApi identifier | 
 **transportGatewayApiPatch** | [**TransportGatewayApiPatch**](TransportGatewayApiPatch.md)| The updated TransportGatewayApi resource | 

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGatewayApiIdPut

> TransportGatewayApiGet apiTransportGatewayApiIdPut(id, transportGatewayApiPut)

Replaces the TransportGatewayApi resource.

Replaces the TransportGatewayApi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGatewayApiApi();
let id = "id_example"; // String | TransportGatewayApi identifier
let transportGatewayApiPut = new AlerterSystemApi.TransportGatewayApiPut(); // TransportGatewayApiPut | The updated TransportGatewayApi resource
apiInstance.apiTransportGatewayApiIdPut(id, transportGatewayApiPut, (error, data, response) => {
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
 **id** | **String**| TransportGatewayApi identifier | 
 **transportGatewayApiPut** | [**TransportGatewayApiPut**](TransportGatewayApiPut.md)| The updated TransportGatewayApi resource | 

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportGatewayApiPost

> TransportGatewayApiGet apiTransportGatewayApiPost(transportGatewayApiPost)

Creates a TransportGatewayApi resource.

Creates a TransportGatewayApi resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportGatewayApiApi();
let transportGatewayApiPost = new AlerterSystemApi.TransportGatewayApiPost(); // TransportGatewayApiPost | The new TransportGatewayApi resource
apiInstance.apiTransportGatewayApiPost(transportGatewayApiPost, (error, data, response) => {
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
 **transportGatewayApiPost** | [**TransportGatewayApiPost**](TransportGatewayApiPost.md)| The new TransportGatewayApi resource | 

### Return type

[**TransportGatewayApiGet**](TransportGatewayApiGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

