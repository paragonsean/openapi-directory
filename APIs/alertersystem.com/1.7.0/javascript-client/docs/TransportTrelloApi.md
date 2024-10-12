# AlerterSystemApi.TransportTrelloApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportTrelloGetCollection**](TransportTrelloApi.md#apiTransportTrelloGetCollection) | **GET** /api/transport-trello | Retrieves the collection of TransportTrello resources.
[**apiTransportTrelloIdDelete**](TransportTrelloApi.md#apiTransportTrelloIdDelete) | **DELETE** /api/transport-trello/{id} | Removes the TransportTrello resource.
[**apiTransportTrelloIdGet**](TransportTrelloApi.md#apiTransportTrelloIdGet) | **GET** /api/transport-trello/{id} | Retrieves a TransportTrello resource.
[**apiTransportTrelloIdPatch**](TransportTrelloApi.md#apiTransportTrelloIdPatch) | **PATCH** /api/transport-trello/{id} | Updates the TransportTrello resource.
[**apiTransportTrelloIdPut**](TransportTrelloApi.md#apiTransportTrelloIdPut) | **PUT** /api/transport-trello/{id} | Replaces the TransportTrello resource.
[**apiTransportTrelloPost**](TransportTrelloApi.md#apiTransportTrelloPost) | **POST** /api/transport-trello | Creates a TransportTrello resource.



## apiTransportTrelloGetCollection

> [TransportTrelloGet] apiTransportTrelloGetCollection(opts)

Retrieves the collection of TransportTrello resources.

Retrieves the collection of TransportTrello resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTrelloApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportTrelloGetCollection(opts, (error, data, response) => {
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

[**[TransportTrelloGet]**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTrelloIdDelete

> apiTransportTrelloIdDelete(id)

Removes the TransportTrello resource.

Removes the TransportTrello resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTrelloApi();
let id = "id_example"; // String | TransportTrello identifier
apiInstance.apiTransportTrelloIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportTrello identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportTrelloIdGet

> TransportTrelloGet apiTransportTrelloIdGet(id)

Retrieves a TransportTrello resource.

Retrieves a TransportTrello resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTrelloApi();
let id = "id_example"; // String | TransportTrello identifier
apiInstance.apiTransportTrelloIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportTrello identifier | 

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTrelloIdPatch

> TransportTrelloGet apiTransportTrelloIdPatch(id, transportTrelloPatch)

Updates the TransportTrello resource.

Updates the TransportTrello resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTrelloApi();
let id = "id_example"; // String | TransportTrello identifier
let transportTrelloPatch = new AlerterSystemApi.TransportTrelloPatch(); // TransportTrelloPatch | The updated TransportTrello resource
apiInstance.apiTransportTrelloIdPatch(id, transportTrelloPatch, (error, data, response) => {
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
 **id** | **String**| TransportTrello identifier | 
 **transportTrelloPatch** | [**TransportTrelloPatch**](TransportTrelloPatch.md)| The updated TransportTrello resource | 

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTrelloIdPut

> TransportTrelloGet apiTransportTrelloIdPut(id, transportTrelloPut)

Replaces the TransportTrello resource.

Replaces the TransportTrello resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTrelloApi();
let id = "id_example"; // String | TransportTrello identifier
let transportTrelloPut = new AlerterSystemApi.TransportTrelloPut(); // TransportTrelloPut | The updated TransportTrello resource
apiInstance.apiTransportTrelloIdPut(id, transportTrelloPut, (error, data, response) => {
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
 **id** | **String**| TransportTrello identifier | 
 **transportTrelloPut** | [**TransportTrelloPut**](TransportTrelloPut.md)| The updated TransportTrello resource | 

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportTrelloPost

> TransportTrelloGet apiTransportTrelloPost(transportTrelloPost)

Creates a TransportTrello resource.

Creates a TransportTrello resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportTrelloApi();
let transportTrelloPost = new AlerterSystemApi.TransportTrelloPost(); // TransportTrelloPost | The new TransportTrello resource
apiInstance.apiTransportTrelloPost(transportTrelloPost, (error, data, response) => {
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
 **transportTrelloPost** | [**TransportTrelloPost**](TransportTrelloPost.md)| The new TransportTrello resource | 

### Return type

[**TransportTrelloGet**](TransportTrelloGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

