# EtherpadApi.GroupApi

All URIs are relative to *http://etherpad.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroupIfNotExistsForUsingGET**](GroupApi.md#createGroupIfNotExistsForUsingGET) | **GET** /createGroupIfNotExistsFor | this functions helps you to map your application group ids to Etherpad group ids
[**createGroupIfNotExistsForUsingPOST**](GroupApi.md#createGroupIfNotExistsForUsingPOST) | **POST** /createGroupIfNotExistsFor | this functions helps you to map your application group ids to Etherpad group ids
[**createGroupPadUsingGET**](GroupApi.md#createGroupPadUsingGET) | **GET** /createGroupPad | creates a new pad in this group
[**createGroupPadUsingPOST**](GroupApi.md#createGroupPadUsingPOST) | **POST** /createGroupPad | creates a new pad in this group
[**createGroupUsingGET**](GroupApi.md#createGroupUsingGET) | **GET** /createGroup | creates a new group
[**createGroupUsingPOST**](GroupApi.md#createGroupUsingPOST) | **POST** /createGroup | creates a new group
[**deleteGroupUsingGET**](GroupApi.md#deleteGroupUsingGET) | **GET** /deleteGroup | deletes a group
[**deleteGroupUsingPOST**](GroupApi.md#deleteGroupUsingPOST) | **POST** /deleteGroup | deletes a group
[**listAllGroupsUsingGET**](GroupApi.md#listAllGroupsUsingGET) | **GET** /listAllGroups | 
[**listAllGroupsUsingPOST**](GroupApi.md#listAllGroupsUsingPOST) | **POST** /listAllGroups | 
[**listPadsUsingGET**](GroupApi.md#listPadsUsingGET) | **GET** /listPads | returns all pads of this group
[**listPadsUsingPOST**](GroupApi.md#listPadsUsingPOST) | **POST** /listPads | returns all pads of this group
[**listSessionsOfGroupUsingGET**](GroupApi.md#listSessionsOfGroupUsingGET) | **GET** /listSessionsOfGroup | 
[**listSessionsOfGroupUsingPOST**](GroupApi.md#listSessionsOfGroupUsingPOST) | **POST** /listSessionsOfGroup | 



## createGroupIfNotExistsForUsingGET

> CreateGroupUsingGET200Response createGroupIfNotExistsForUsingGET(opts)

this functions helps you to map your application group ids to Etherpad group ids

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupMapper': "groupMapper_example" // String | 
};
apiInstance.createGroupIfNotExistsForUsingGET(opts, (error, data, response) => {
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
 **groupMapper** | **String**|  | [optional] 

### Return type

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createGroupIfNotExistsForUsingPOST

> CreateGroupUsingGET200Response createGroupIfNotExistsForUsingPOST(opts)

this functions helps you to map your application group ids to Etherpad group ids

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupMapper': "groupMapper_example" // String | 
};
apiInstance.createGroupIfNotExistsForUsingPOST(opts, (error, data, response) => {
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
 **groupMapper** | **String**|  | [optional] 

### Return type

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createGroupPadUsingGET

> AppendChatMessageUsingGET200Response createGroupPadUsingGET(opts)

creates a new pad in this group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example", // String | 
  'padName': "padName_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.createGroupPadUsingGET(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 
 **padName** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createGroupPadUsingPOST

> AppendChatMessageUsingGET200Response createGroupPadUsingPOST(opts)

creates a new pad in this group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example", // String | 
  'padName': "padName_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.createGroupPadUsingPOST(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 
 **padName** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createGroupUsingGET

> CreateGroupUsingGET200Response createGroupUsingGET()

creates a new group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
apiInstance.createGroupUsingGET((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createGroupUsingPOST

> CreateGroupUsingGET200Response createGroupUsingPOST()

creates a new group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
apiInstance.createGroupUsingPOST((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CreateGroupUsingGET200Response**](CreateGroupUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGroupUsingGET

> AppendChatMessageUsingGET200Response deleteGroupUsingGET(opts)

deletes a group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example" // String | 
};
apiInstance.deleteGroupUsingGET(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGroupUsingPOST

> AppendChatMessageUsingGET200Response deleteGroupUsingPOST(opts)

deletes a group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example" // String | 
};
apiInstance.deleteGroupUsingPOST(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAllGroupsUsingGET

> ListAllGroupsUsingGET200Response listAllGroupsUsingGET()



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
apiInstance.listAllGroupsUsingGET((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAllGroupsUsingGET200Response**](ListAllGroupsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAllGroupsUsingPOST

> ListAllGroupsUsingGET200Response listAllGroupsUsingPOST()



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
apiInstance.listAllGroupsUsingPOST((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAllGroupsUsingGET200Response**](ListAllGroupsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPadsUsingGET

> ListAllPadsUsingGET200Response listPadsUsingGET(opts)

returns all pads of this group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example" // String | 
};
apiInstance.listPadsUsingGET(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 

### Return type

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPadsUsingPOST

> ListAllPadsUsingGET200Response listPadsUsingPOST(opts)

returns all pads of this group

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example" // String | 
};
apiInstance.listPadsUsingPOST(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 

### Return type

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSessionsOfGroupUsingGET

> ListSessionsOfAuthorUsingGET200Response listSessionsOfGroupUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example" // String | 
};
apiInstance.listSessionsOfGroupUsingGET(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 

### Return type

[**ListSessionsOfAuthorUsingGET200Response**](ListSessionsOfAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSessionsOfGroupUsingPOST

> ListSessionsOfAuthorUsingGET200Response listSessionsOfGroupUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.GroupApi();
let opts = {
  'groupID': "groupID_example" // String | 
};
apiInstance.listSessionsOfGroupUsingPOST(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 

### Return type

[**ListSessionsOfAuthorUsingGET200Response**](ListSessionsOfAuthorUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

