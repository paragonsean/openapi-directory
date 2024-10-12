# EtherpadApi.PadApi

All URIs are relative to *http://etherpad.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appendChatMessageUsingGET**](PadApi.md#appendChatMessageUsingGET) | **GET** /appendChatMessage | appends a chat message
[**appendChatMessageUsingPOST**](PadApi.md#appendChatMessageUsingPOST) | **POST** /appendChatMessage | appends a chat message
[**checkTokenUsingGET**](PadApi.md#checkTokenUsingGET) | **GET** /checkToken | returns ok when the current api token is valid
[**checkTokenUsingPOST**](PadApi.md#checkTokenUsingPOST) | **POST** /checkToken | returns ok when the current api token is valid
[**createDiffHTMLUsingGET**](PadApi.md#createDiffHTMLUsingGET) | **GET** /createDiffHTML | 
[**createDiffHTMLUsingPOST**](PadApi.md#createDiffHTMLUsingPOST) | **POST** /createDiffHTML | 
[**createPadUsingGET**](PadApi.md#createPadUsingGET) | **GET** /createPad | 
[**createPadUsingPOST**](PadApi.md#createPadUsingPOST) | **POST** /createPad | 
[**deletePadUsingGET**](PadApi.md#deletePadUsingGET) | **GET** /deletePad | deletes a pad
[**deletePadUsingPOST**](PadApi.md#deletePadUsingPOST) | **POST** /deletePad | deletes a pad
[**getChatHeadUsingGET**](PadApi.md#getChatHeadUsingGET) | **GET** /getChatHead | returns the chatHead (chat-message) of the pad
[**getChatHeadUsingPOST**](PadApi.md#getChatHeadUsingPOST) | **POST** /getChatHead | returns the chatHead (chat-message) of the pad
[**getChatHistoryUsingGET**](PadApi.md#getChatHistoryUsingGET) | **GET** /getChatHistory | returns the chat history
[**getChatHistoryUsingPOST**](PadApi.md#getChatHistoryUsingPOST) | **POST** /getChatHistory | returns the chat history
[**getHTMLUsingGET**](PadApi.md#getHTMLUsingGET) | **GET** /getHTML | returns the text of a pad formatted as HTML
[**getHTMLUsingPOST**](PadApi.md#getHTMLUsingPOST) | **POST** /getHTML | returns the text of a pad formatted as HTML
[**getLastEditedUsingGET**](PadApi.md#getLastEditedUsingGET) | **GET** /getLastEdited | returns the timestamp of the last revision of the pad
[**getLastEditedUsingPOST**](PadApi.md#getLastEditedUsingPOST) | **POST** /getLastEdited | returns the timestamp of the last revision of the pad
[**getPublicStatusUsingGET**](PadApi.md#getPublicStatusUsingGET) | **GET** /getPublicStatus | return true of false
[**getPublicStatusUsingPOST**](PadApi.md#getPublicStatusUsingPOST) | **POST** /getPublicStatus | return true of false
[**getReadOnlyIDUsingGET**](PadApi.md#getReadOnlyIDUsingGET) | **GET** /getReadOnlyID | returns the read only link of a pad
[**getReadOnlyIDUsingPOST**](PadApi.md#getReadOnlyIDUsingPOST) | **POST** /getReadOnlyID | returns the read only link of a pad
[**getRevisionsCountUsingGET**](PadApi.md#getRevisionsCountUsingGET) | **GET** /getRevisionsCount | returns the number of revisions of this pad
[**getRevisionsCountUsingPOST**](PadApi.md#getRevisionsCountUsingPOST) | **POST** /getRevisionsCount | returns the number of revisions of this pad
[**getTextUsingGET**](PadApi.md#getTextUsingGET) | **GET** /getText | returns the text of a pad
[**getTextUsingPOST**](PadApi.md#getTextUsingPOST) | **POST** /getText | returns the text of a pad
[**listAllPadsUsingGET**](PadApi.md#listAllPadsUsingGET) | **GET** /listAllPads | list all the pads
[**listAllPadsUsingPOST**](PadApi.md#listAllPadsUsingPOST) | **POST** /listAllPads | list all the pads
[**listAuthorsOfPadUsingGET**](PadApi.md#listAuthorsOfPadUsingGET) | **GET** /listAuthorsOfPad | returns an array of authors who contributed to this pad
[**listAuthorsOfPadUsingPOST**](PadApi.md#listAuthorsOfPadUsingPOST) | **POST** /listAuthorsOfPad | returns an array of authors who contributed to this pad
[**padUsersCountUsingGET**](PadApi.md#padUsersCountUsingGET) | **GET** /padUsersCount | returns the number of user that are currently editing this pad
[**padUsersCountUsingPOST**](PadApi.md#padUsersCountUsingPOST) | **POST** /padUsersCount | returns the number of user that are currently editing this pad
[**padUsersUsingGET**](PadApi.md#padUsersUsingGET) | **GET** /padUsers | returns the list of users that are currently editing this pad
[**padUsersUsingPOST**](PadApi.md#padUsersUsingPOST) | **POST** /padUsers | returns the list of users that are currently editing this pad
[**sendClientsMessageUsingGET**](PadApi.md#sendClientsMessageUsingGET) | **GET** /sendClientsMessage | sends a custom message of type msg to the pad
[**sendClientsMessageUsingPOST**](PadApi.md#sendClientsMessageUsingPOST) | **POST** /sendClientsMessage | sends a custom message of type msg to the pad
[**setHTMLUsingGET**](PadApi.md#setHTMLUsingGET) | **GET** /setHTML | sets the text of a pad with HTML
[**setHTMLUsingPOST**](PadApi.md#setHTMLUsingPOST) | **POST** /setHTML | sets the text of a pad with HTML
[**setPublicStatusUsingGET**](PadApi.md#setPublicStatusUsingGET) | **GET** /setPublicStatus | sets a boolean for the public status of a pad
[**setPublicStatusUsingPOST**](PadApi.md#setPublicStatusUsingPOST) | **POST** /setPublicStatus | sets a boolean for the public status of a pad
[**setTextUsingGET**](PadApi.md#setTextUsingGET) | **GET** /setText | sets the text of a pad
[**setTextUsingPOST**](PadApi.md#setTextUsingPOST) | **POST** /setText | sets the text of a pad



## appendChatMessageUsingGET

> AppendChatMessageUsingGET200Response appendChatMessageUsingGET(opts)

appends a chat message

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example", // String | 
  'authorID': "authorID_example", // String | 
  'time': "time_example" // String | 
};
apiInstance.appendChatMessageUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 
 **authorID** | **String**|  | [optional] 
 **time** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appendChatMessageUsingPOST

> AppendChatMessageUsingGET200Response appendChatMessageUsingPOST(opts)

appends a chat message

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example", // String | 
  'authorID': "authorID_example", // String | 
  'time': "time_example" // String | 
};
apiInstance.appendChatMessageUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 
 **authorID** | **String**|  | [optional] 
 **time** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkTokenUsingGET

> AppendChatMessageUsingGET200Response checkTokenUsingGET()

returns ok when the current api token is valid

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
apiInstance.checkTokenUsingGET((error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkTokenUsingPOST

> AppendChatMessageUsingGET200Response checkTokenUsingPOST()

returns ok when the current api token is valid

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
apiInstance.checkTokenUsingPOST((error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDiffHTMLUsingGET

> CreateDiffHTMLUsingGET200Response createDiffHTMLUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'startRev': "startRev_example", // String | 
  'endRev': "endRev_example" // String | 
};
apiInstance.createDiffHTMLUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **startRev** | **String**|  | [optional] 
 **endRev** | **String**|  | [optional] 

### Return type

[**CreateDiffHTMLUsingGET200Response**](CreateDiffHTMLUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDiffHTMLUsingPOST

> CreateDiffHTMLUsingGET200Response createDiffHTMLUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'startRev': "startRev_example", // String | 
  'endRev': "endRev_example" // String | 
};
apiInstance.createDiffHTMLUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **startRev** | **String**|  | [optional] 
 **endRev** | **String**|  | [optional] 

### Return type

[**CreateDiffHTMLUsingGET200Response**](CreateDiffHTMLUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPadUsingGET

> AppendChatMessageUsingGET200Response createPadUsingGET(opts)



creates a new (non-group) pad. Note that if you need to create a group Pad, you should call createGroupPad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.createPadUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPadUsingPOST

> AppendChatMessageUsingGET200Response createPadUsingPOST(opts)



creates a new (non-group) pad. Note that if you need to create a group Pad, you should call createGroupPad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.createPadUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePadUsingGET

> AppendChatMessageUsingGET200Response deletePadUsingGET(opts)

deletes a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.deletePadUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePadUsingPOST

> AppendChatMessageUsingGET200Response deletePadUsingPOST(opts)

deletes a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.deletePadUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChatHeadUsingGET

> GetChatHeadUsingGET200Response getChatHeadUsingGET(opts)

returns the chatHead (chat-message) of the pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getChatHeadUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetChatHeadUsingGET200Response**](GetChatHeadUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChatHeadUsingPOST

> GetChatHeadUsingGET200Response getChatHeadUsingPOST(opts)

returns the chatHead (chat-message) of the pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getChatHeadUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetChatHeadUsingGET200Response**](GetChatHeadUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChatHistoryUsingGET

> GetChatHistoryUsingGET200Response getChatHistoryUsingGET(opts)

returns the chat history

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'start': "start_example", // String | 
  'end': "end_example" // String | 
};
apiInstance.getChatHistoryUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **start** | **String**|  | [optional] 
 **end** | **String**|  | [optional] 

### Return type

[**GetChatHistoryUsingGET200Response**](GetChatHistoryUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChatHistoryUsingPOST

> GetChatHistoryUsingGET200Response getChatHistoryUsingPOST(opts)

returns the chat history

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'start': "start_example", // String | 
  'end': "end_example" // String | 
};
apiInstance.getChatHistoryUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **start** | **String**|  | [optional] 
 **end** | **String**|  | [optional] 

### Return type

[**GetChatHistoryUsingGET200Response**](GetChatHistoryUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHTMLUsingGET

> GetHTMLUsingGET200Response getHTMLUsingGET(opts)

returns the text of a pad formatted as HTML

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.getHTMLUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **rev** | **String**|  | [optional] 

### Return type

[**GetHTMLUsingGET200Response**](GetHTMLUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHTMLUsingPOST

> GetHTMLUsingGET200Response getHTMLUsingPOST(opts)

returns the text of a pad formatted as HTML

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.getHTMLUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **rev** | **String**|  | [optional] 

### Return type

[**GetHTMLUsingGET200Response**](GetHTMLUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLastEditedUsingGET

> GetLastEditedUsingGET200Response getLastEditedUsingGET(opts)

returns the timestamp of the last revision of the pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getLastEditedUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetLastEditedUsingGET200Response**](GetLastEditedUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLastEditedUsingPOST

> GetLastEditedUsingGET200Response getLastEditedUsingPOST(opts)

returns the timestamp of the last revision of the pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getLastEditedUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetLastEditedUsingGET200Response**](GetLastEditedUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicStatusUsingGET

> GetPublicStatusUsingGET200Response getPublicStatusUsingGET(opts)

return true of false

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getPublicStatusUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetPublicStatusUsingGET200Response**](GetPublicStatusUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicStatusUsingPOST

> GetPublicStatusUsingGET200Response getPublicStatusUsingPOST(opts)

return true of false

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getPublicStatusUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetPublicStatusUsingGET200Response**](GetPublicStatusUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadOnlyIDUsingGET

> GetReadOnlyIDUsingGET200Response getReadOnlyIDUsingGET(opts)

returns the read only link of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getReadOnlyIDUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetReadOnlyIDUsingGET200Response**](GetReadOnlyIDUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReadOnlyIDUsingPOST

> GetReadOnlyIDUsingGET200Response getReadOnlyIDUsingPOST(opts)

returns the read only link of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getReadOnlyIDUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetReadOnlyIDUsingGET200Response**](GetReadOnlyIDUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRevisionsCountUsingGET

> GetRevisionsCountUsingGET200Response getRevisionsCountUsingGET(opts)

returns the number of revisions of this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getRevisionsCountUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetRevisionsCountUsingGET200Response**](GetRevisionsCountUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRevisionsCountUsingPOST

> GetRevisionsCountUsingGET200Response getRevisionsCountUsingPOST(opts)

returns the number of revisions of this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getRevisionsCountUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**GetRevisionsCountUsingGET200Response**](GetRevisionsCountUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextUsingGET

> GetTextUsingGET200Response getTextUsingGET(opts)

returns the text of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.getTextUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **rev** | **String**|  | [optional] 

### Return type

[**GetTextUsingGET200Response**](GetTextUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextUsingPOST

> GetTextUsingGET200Response getTextUsingPOST(opts)

returns the text of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.getTextUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **rev** | **String**|  | [optional] 

### Return type

[**GetTextUsingGET200Response**](GetTextUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAllPadsUsingGET

> ListAllPadsUsingGET200Response listAllPadsUsingGET()

list all the pads

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
apiInstance.listAllPadsUsingGET((error, data, response) => {
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

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAllPadsUsingPOST

> ListAllPadsUsingGET200Response listAllPadsUsingPOST()

list all the pads

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
apiInstance.listAllPadsUsingPOST((error, data, response) => {
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

[**ListAllPadsUsingGET200Response**](ListAllPadsUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAuthorsOfPadUsingGET

> ListAuthorsOfPadUsingGET200Response listAuthorsOfPadUsingGET(opts)

returns an array of authors who contributed to this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.listAuthorsOfPadUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**ListAuthorsOfPadUsingGET200Response**](ListAuthorsOfPadUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAuthorsOfPadUsingPOST

> ListAuthorsOfPadUsingGET200Response listAuthorsOfPadUsingPOST(opts)

returns an array of authors who contributed to this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.listAuthorsOfPadUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**ListAuthorsOfPadUsingGET200Response**](ListAuthorsOfPadUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## padUsersCountUsingGET

> PadUsersCountUsingGET200Response padUsersCountUsingGET(opts)

returns the number of user that are currently editing this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.padUsersCountUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**PadUsersCountUsingGET200Response**](PadUsersCountUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## padUsersCountUsingPOST

> PadUsersCountUsingGET200Response padUsersCountUsingPOST(opts)

returns the number of user that are currently editing this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.padUsersCountUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**PadUsersCountUsingGET200Response**](PadUsersCountUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## padUsersUsingGET

> PadUsersUsingGET200Response padUsersUsingGET(opts)

returns the list of users that are currently editing this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.padUsersUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**PadUsersUsingGET200Response**](PadUsersUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## padUsersUsingPOST

> PadUsersUsingGET200Response padUsersUsingPOST(opts)

returns the list of users that are currently editing this pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.padUsersUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 

### Return type

[**PadUsersUsingGET200Response**](PadUsersUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendClientsMessageUsingGET

> AppendChatMessageUsingGET200Response sendClientsMessageUsingGET(opts)

sends a custom message of type msg to the pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'msg': "msg_example" // String | 
};
apiInstance.sendClientsMessageUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **msg** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendClientsMessageUsingPOST

> AppendChatMessageUsingGET200Response sendClientsMessageUsingPOST(opts)

sends a custom message of type msg to the pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'msg': "msg_example" // String | 
};
apiInstance.sendClientsMessageUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **msg** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setHTMLUsingGET

> AppendChatMessageUsingGET200Response setHTMLUsingGET(opts)

sets the text of a pad with HTML

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'html': "html_example" // String | 
};
apiInstance.setHTMLUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **html** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setHTMLUsingPOST

> AppendChatMessageUsingGET200Response setHTMLUsingPOST(opts)

sets the text of a pad with HTML

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'html': "html_example" // String | 
};
apiInstance.setHTMLUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **html** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setPublicStatusUsingGET

> AppendChatMessageUsingGET200Response setPublicStatusUsingGET(opts)

sets a boolean for the public status of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'publicStatus': "publicStatus_example" // String | 
};
apiInstance.setPublicStatusUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **publicStatus** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setPublicStatusUsingPOST

> AppendChatMessageUsingGET200Response setPublicStatusUsingPOST(opts)

sets a boolean for the public status of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'publicStatus': "publicStatus_example" // String | 
};
apiInstance.setPublicStatusUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **publicStatus** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setTextUsingGET

> AppendChatMessageUsingGET200Response setTextUsingGET(opts)

sets the text of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.setTextUsingGET(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setTextUsingPOST

> AppendChatMessageUsingGET200Response setTextUsingPOST(opts)

sets the text of a pad

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.PadApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.setTextUsingPOST(opts, (error, data, response) => {
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
 **padID** | **String**|  | [optional] 
 **text** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

