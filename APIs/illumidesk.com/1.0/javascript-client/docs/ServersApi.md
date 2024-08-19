# IllumiDesk.ServersApi

All URIs are relative to *https://api.illumidesk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serversOptionsResourcesRead**](ServersApi.md#serversOptionsResourcesRead) | **GET** /v1/servers/options/server-size/{size}/ | Get a server size by id
[**serversOptionsServerSizeCreate**](ServersApi.md#serversOptionsServerSizeCreate) | **POST** /v1/servers/options/server-size/ | Create a new server size item
[**serversOptionsServerSizeDelete**](ServersApi.md#serversOptionsServerSizeDelete) | **DELETE** /v1/servers/options/server-size/{size}/ | Delete a server size by id
[**serversOptionsServerSizeReplace**](ServersApi.md#serversOptionsServerSizeReplace) | **PUT** /v1/servers/options/server-size/{size}/ | Replace a server size by id
[**serversOptionsServerSizeUpdate**](ServersApi.md#serversOptionsServerSizeUpdate) | **PATCH** /v1/servers/options/server-size/{size}/ | Update a server size by id
[**serversOptionsSizesList**](ServersApi.md#serversOptionsSizesList) | **GET** /v1/servers/options/server-size/ | Retrieve available server sizes



## serversOptionsResourcesRead

> ServerSize serversOptionsResourcesRead(size)

Get a server size by id

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ServersApi();
let size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
apiInstance.serversOptionsResourcesRead(size, (error, data, response) => {
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
 **size** | **String**| Server size unique identifier expressed as UUID or name. | 

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## serversOptionsServerSizeCreate

> ServerSize serversOptionsServerSizeCreate(opts)

Create a new server size item

Only super users with on-premises version have acceess to this endpoint.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ServersApi();
let opts = {
  'serversizeData': new IllumiDesk.ServerSizeData() // ServerSizeData | 
};
apiInstance.serversOptionsServerSizeCreate(opts, (error, data, response) => {
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
 **serversizeData** | [**ServerSizeData**](ServerSizeData.md)|  | [optional] 

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## serversOptionsServerSizeDelete

> serversOptionsServerSizeDelete(size)

Delete a server size by id

Only super users with on-premises version have acceess to this endpoint.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ServersApi();
let size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
apiInstance.serversOptionsServerSizeDelete(size, (error, data, response) => {
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
 **size** | **String**| Server size unique identifier expressed as UUID or name. | 

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html


## serversOptionsServerSizeReplace

> ServerSize serversOptionsServerSizeReplace(size, opts)

Replace a server size by id

Only super users with on-premises version have acceess to this endpoint.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ServersApi();
let size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
let opts = {
  'serversizeData': new IllumiDesk.ServerSizeData() // ServerSizeData | 
};
apiInstance.serversOptionsServerSizeReplace(size, opts, (error, data, response) => {
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
 **size** | **String**| Server size unique identifier expressed as UUID or name. | 
 **serversizeData** | [**ServerSizeData**](ServerSizeData.md)|  | [optional] 

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## serversOptionsServerSizeUpdate

> ServerSize serversOptionsServerSizeUpdate(size, opts)

Update a server size by id

Only super users with on-premises version have acceess to this endpoint.

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ServersApi();
let size = "size_example"; // String | Server size unique identifier expressed as UUID or name.
let opts = {
  'serversizeData': new IllumiDesk.ServerSizeData() // ServerSizeData | 
};
apiInstance.serversOptionsServerSizeUpdate(size, opts, (error, data, response) => {
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
 **size** | **String**| Server size unique identifier expressed as UUID or name. | 
 **serversizeData** | [**ServerSizeData**](ServerSizeData.md)|  | [optional] 

### Return type

[**ServerSize**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/html


## serversOptionsSizesList

> [ServerSize] serversOptionsSizesList(opts)

Retrieve available server sizes

### Example

```javascript
import IllumiDesk from 'illumi_desk';
let defaultClient = IllumiDesk.ApiClient.instance;
// Configure API key authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//jwt.apiKeyPrefix = 'Token';

let apiInstance = new IllumiDesk.ServersApi();
let opts = {
  'limit': "limit_example", // String | Set limit when retrieving items.
  'offset': "offset_example", // String | Offset when retrieving items.
  'ordering': "ordering_example" // String | Set order when retrieving items.
};
apiInstance.serversOptionsSizesList(opts, (error, data, response) => {
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
 **limit** | **String**| Set limit when retrieving items. | [optional] 
 **offset** | **String**| Offset when retrieving items. | [optional] 
 **ordering** | **String**| Set order when retrieving items. | [optional] 

### Return type

[**[ServerSize]**](ServerSize.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html

