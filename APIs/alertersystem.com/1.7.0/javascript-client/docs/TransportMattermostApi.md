# AlerterSystemApi.TransportMattermostApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMattermostGetCollection**](TransportMattermostApi.md#apiTransportMattermostGetCollection) | **GET** /api/transport-mattermost | Retrieves the collection of TransportMattermost resources.
[**apiTransportMattermostIdDelete**](TransportMattermostApi.md#apiTransportMattermostIdDelete) | **DELETE** /api/transport-mattermost/{id} | Removes the TransportMattermost resource.
[**apiTransportMattermostIdGet**](TransportMattermostApi.md#apiTransportMattermostIdGet) | **GET** /api/transport-mattermost/{id} | Retrieves a TransportMattermost resource.
[**apiTransportMattermostIdPatch**](TransportMattermostApi.md#apiTransportMattermostIdPatch) | **PATCH** /api/transport-mattermost/{id} | Updates the TransportMattermost resource.
[**apiTransportMattermostIdPut**](TransportMattermostApi.md#apiTransportMattermostIdPut) | **PUT** /api/transport-mattermost/{id} | Replaces the TransportMattermost resource.
[**apiTransportMattermostPost**](TransportMattermostApi.md#apiTransportMattermostPost) | **POST** /api/transport-mattermost | Creates a TransportMattermost resource.



## apiTransportMattermostGetCollection

> [TransportMattermostGet] apiTransportMattermostGetCollection(opts)

Retrieves the collection of TransportMattermost resources.

Retrieves the collection of TransportMattermost resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMattermostApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMattermostGetCollection(opts, (error, data, response) => {
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

[**[TransportMattermostGet]**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMattermostIdDelete

> apiTransportMattermostIdDelete(id)

Removes the TransportMattermost resource.

Removes the TransportMattermost resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMattermostApi();
let id = "id_example"; // String | TransportMattermost identifier
apiInstance.apiTransportMattermostIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMattermost identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMattermostIdGet

> TransportMattermostGet apiTransportMattermostIdGet(id)

Retrieves a TransportMattermost resource.

Retrieves a TransportMattermost resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMattermostApi();
let id = "id_example"; // String | TransportMattermost identifier
apiInstance.apiTransportMattermostIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMattermost identifier | 

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMattermostIdPatch

> TransportMattermostGet apiTransportMattermostIdPatch(id, transportMattermostPatch)

Updates the TransportMattermost resource.

Updates the TransportMattermost resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMattermostApi();
let id = "id_example"; // String | TransportMattermost identifier
let transportMattermostPatch = new AlerterSystemApi.TransportMattermostPatch(); // TransportMattermostPatch | The updated TransportMattermost resource
apiInstance.apiTransportMattermostIdPatch(id, transportMattermostPatch, (error, data, response) => {
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
 **id** | **String**| TransportMattermost identifier | 
 **transportMattermostPatch** | [**TransportMattermostPatch**](TransportMattermostPatch.md)| The updated TransportMattermost resource | 

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMattermostIdPut

> TransportMattermostGet apiTransportMattermostIdPut(id, transportMattermostPut)

Replaces the TransportMattermost resource.

Replaces the TransportMattermost resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMattermostApi();
let id = "id_example"; // String | TransportMattermost identifier
let transportMattermostPut = new AlerterSystemApi.TransportMattermostPut(); // TransportMattermostPut | The updated TransportMattermost resource
apiInstance.apiTransportMattermostIdPut(id, transportMattermostPut, (error, data, response) => {
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
 **id** | **String**| TransportMattermost identifier | 
 **transportMattermostPut** | [**TransportMattermostPut**](TransportMattermostPut.md)| The updated TransportMattermost resource | 

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMattermostPost

> TransportMattermostGet apiTransportMattermostPost(transportMattermostPost)

Creates a TransportMattermost resource.

Creates a TransportMattermost resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMattermostApi();
let transportMattermostPost = new AlerterSystemApi.TransportMattermostPost(); // TransportMattermostPost | The new TransportMattermost resource
apiInstance.apiTransportMattermostPost(transportMattermostPost, (error, data, response) => {
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
 **transportMattermostPost** | [**TransportMattermostPost**](TransportMattermostPost.md)| The new TransportMattermost resource | 

### Return type

[**TransportMattermostGet**](TransportMattermostGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

