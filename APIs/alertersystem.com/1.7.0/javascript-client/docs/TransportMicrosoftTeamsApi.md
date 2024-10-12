# AlerterSystemApi.TransportMicrosoftTeamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTransportMicrosoftTeamsGetCollection**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsGetCollection) | **GET** /api/transport-microsoft-teams | Retrieves the collection of TransportMicrosoftTeams resources.
[**apiTransportMicrosoftTeamsIdDelete**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdDelete) | **DELETE** /api/transport-microsoft-teams/{id} | Removes the TransportMicrosoftTeams resource.
[**apiTransportMicrosoftTeamsIdGet**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdGet) | **GET** /api/transport-microsoft-teams/{id} | Retrieves a TransportMicrosoftTeams resource.
[**apiTransportMicrosoftTeamsIdPatch**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdPatch) | **PATCH** /api/transport-microsoft-teams/{id} | Updates the TransportMicrosoftTeams resource.
[**apiTransportMicrosoftTeamsIdPut**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsIdPut) | **PUT** /api/transport-microsoft-teams/{id} | Replaces the TransportMicrosoftTeams resource.
[**apiTransportMicrosoftTeamsPost**](TransportMicrosoftTeamsApi.md#apiTransportMicrosoftTeamsPost) | **POST** /api/transport-microsoft-teams | Creates a TransportMicrosoftTeams resource.



## apiTransportMicrosoftTeamsGetCollection

> [TransportMicrosoftTeamsGet] apiTransportMicrosoftTeamsGetCollection(opts)

Retrieves the collection of TransportMicrosoftTeams resources.

Retrieves the collection of TransportMicrosoftTeams resources.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMicrosoftTeamsApi();
let opts = {
  'page': 1, // Number | The collection page number
  'dataSegmentCode': "dataSegmentCode_example", // String | 
  'dataSegmentCode2': ["null"], // [String] | 
  'partition': "partition_example", // String | 
  'partition2': ["null"], // [String] | 
  'properties': ["null"] // [String] | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
};
apiInstance.apiTransportMicrosoftTeamsGetCollection(opts, (error, data, response) => {
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

[**[TransportMicrosoftTeamsGet]**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMicrosoftTeamsIdDelete

> apiTransportMicrosoftTeamsIdDelete(id)

Removes the TransportMicrosoftTeams resource.

Removes the TransportMicrosoftTeams resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMicrosoftTeamsApi();
let id = "id_example"; // String | TransportMicrosoftTeams identifier
apiInstance.apiTransportMicrosoftTeamsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| TransportMicrosoftTeams identifier | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTransportMicrosoftTeamsIdGet

> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsIdGet(id)

Retrieves a TransportMicrosoftTeams resource.

Retrieves a TransportMicrosoftTeams resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMicrosoftTeamsApi();
let id = "id_example"; // String | TransportMicrosoftTeams identifier
apiInstance.apiTransportMicrosoftTeamsIdGet(id, (error, data, response) => {
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
 **id** | **String**| TransportMicrosoftTeams identifier | 

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMicrosoftTeamsIdPatch

> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsIdPatch(id, transportMicrosoftTeamsPatch)

Updates the TransportMicrosoftTeams resource.

Updates the TransportMicrosoftTeams resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMicrosoftTeamsApi();
let id = "id_example"; // String | TransportMicrosoftTeams identifier
let transportMicrosoftTeamsPatch = new AlerterSystemApi.TransportMicrosoftTeamsPatch(); // TransportMicrosoftTeamsPatch | The updated TransportMicrosoftTeams resource
apiInstance.apiTransportMicrosoftTeamsIdPatch(id, transportMicrosoftTeamsPatch, (error, data, response) => {
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
 **id** | **String**| TransportMicrosoftTeams identifier | 
 **transportMicrosoftTeamsPatch** | [**TransportMicrosoftTeamsPatch**](TransportMicrosoftTeamsPatch.md)| The updated TransportMicrosoftTeams resource | 

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMicrosoftTeamsIdPut

> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsIdPut(id, transportMicrosoftTeamsPut)

Replaces the TransportMicrosoftTeams resource.

Replaces the TransportMicrosoftTeams resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMicrosoftTeamsApi();
let id = "id_example"; // String | TransportMicrosoftTeams identifier
let transportMicrosoftTeamsPut = new AlerterSystemApi.TransportMicrosoftTeamsPut(); // TransportMicrosoftTeamsPut | The updated TransportMicrosoftTeams resource
apiInstance.apiTransportMicrosoftTeamsIdPut(id, transportMicrosoftTeamsPut, (error, data, response) => {
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
 **id** | **String**| TransportMicrosoftTeams identifier | 
 **transportMicrosoftTeamsPut** | [**TransportMicrosoftTeamsPut**](TransportMicrosoftTeamsPut.md)| The updated TransportMicrosoftTeams resource | 

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html


## apiTransportMicrosoftTeamsPost

> TransportMicrosoftTeamsGet apiTransportMicrosoftTeamsPost(transportMicrosoftTeamsPost)

Creates a TransportMicrosoftTeams resource.

Creates a TransportMicrosoftTeams resource.

### Example

```javascript
import AlerterSystemApi from 'alerter_system_api';
let defaultClient = AlerterSystemApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AlerterSystemApi.TransportMicrosoftTeamsApi();
let transportMicrosoftTeamsPost = new AlerterSystemApi.TransportMicrosoftTeamsPost(); // TransportMicrosoftTeamsPost | The new TransportMicrosoftTeams resource
apiInstance.apiTransportMicrosoftTeamsPost(transportMicrosoftTeamsPost, (error, data, response) => {
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
 **transportMicrosoftTeamsPost** | [**TransportMicrosoftTeamsPost**](TransportMicrosoftTeamsPost.md)| The new TransportMicrosoftTeams resource | 

### Return type

[**TransportMicrosoftTeamsGet**](TransportMicrosoftTeamsGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json, application/ld+json, text/html
- **Accept**: application/json, application/ld+json, text/html

