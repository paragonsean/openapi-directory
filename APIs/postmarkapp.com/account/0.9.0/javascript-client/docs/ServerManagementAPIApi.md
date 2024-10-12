# PostmarkAccountLevelApi.ServerManagementAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createServer**](ServerManagementAPIApi.md#createServer) | **POST** /servers | Create a Server
[**deleteServer**](ServerManagementAPIApi.md#deleteServer) | **DELETE** /servers/{serverid} | Delete a Server
[**editServerInformation**](ServerManagementAPIApi.md#editServerInformation) | **PUT** /servers/{serverid} | Edit a Server
[**getServerInformation**](ServerManagementAPIApi.md#getServerInformation) | **GET** /servers/{serverid} | Get a Server
[**listServers**](ServerManagementAPIApi.md#listServers) | **GET** /servers | List servers



## createServer

> ExtendedServerInfo createServer(xPostmarkAccountToken, opts)

Create a Server

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.ServerManagementAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let opts = {
  'body': new PostmarkAccountLevelApi.CreateServerPayload() // CreateServerPayload | 
};
apiInstance.createServer(xPostmarkAccountToken, opts, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **body** | [**CreateServerPayload**](CreateServerPayload.md)|  | [optional] 

### Return type

[**ExtendedServerInfo**](ExtendedServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteServer

> deleteServer(xPostmarkAccountToken, serverid)

Delete a Server

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.ServerManagementAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let serverid = 56; // Number | The ID of the Server that should be deleted.
apiInstance.deleteServer(xPostmarkAccountToken, serverid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **serverid** | **Number**| The ID of the Server that should be deleted. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editServerInformation

> ExtendedServerInfo editServerInformation(xPostmarkAccountToken, serverid, opts)

Edit a Server

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.ServerManagementAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let serverid = 56; // Number | The ID of the Server to update.
let opts = {
  'body': new PostmarkAccountLevelApi.EditServerPayload() // EditServerPayload | 
};
apiInstance.editServerInformation(xPostmarkAccountToken, serverid, opts, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **serverid** | **Number**| The ID of the Server to update. | 
 **body** | [**EditServerPayload**](EditServerPayload.md)|  | [optional] 

### Return type

[**ExtendedServerInfo**](ExtendedServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getServerInformation

> ExtendedServerInfo getServerInformation(xPostmarkAccountToken, serverid)

Get a Server

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.ServerManagementAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let serverid = 56; // Number | The ID of the Server to get.
apiInstance.getServerInformation(xPostmarkAccountToken, serverid, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **serverid** | **Number**| The ID of the Server to get. | 

### Return type

[**ExtendedServerInfo**](ExtendedServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServers

> ServerListingResponse listServers(xPostmarkAccountToken, count, offset, opts)

List servers

### Example

```javascript
import PostmarkAccountLevelApi from 'postmark_account_level_api';

let apiInstance = new PostmarkAccountLevelApi.ServerManagementAPIApi();
let xPostmarkAccountToken = "xPostmarkAccountToken_example"; // String | The token associated with the Account on which this request will operate.
let count = 56; // Number | Number of servers to return per request.
let offset = 56; // Number | Number of servers to skip.
let opts = {
  'name': "name_example" // String | Filter by a specific server name
};
apiInstance.listServers(xPostmarkAccountToken, count, offset, opts, (error, data, response) => {
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
 **xPostmarkAccountToken** | **String**| The token associated with the Account on which this request will operate. | 
 **count** | **Number**| Number of servers to return per request. | 
 **offset** | **Number**| Number of servers to skip. | 
 **name** | **String**| Filter by a specific server name | [optional] 

### Return type

[**ServerListingResponse**](ServerListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

