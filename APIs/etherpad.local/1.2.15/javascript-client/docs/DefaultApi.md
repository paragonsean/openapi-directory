# EtherpadApi.DefaultApi

All URIs are relative to *http://etherpad.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appendTextUsingGET**](DefaultApi.md#appendTextUsingGET) | **GET** /appendText | 
[**appendTextUsingPOST**](DefaultApi.md#appendTextUsingPOST) | **POST** /appendText | 
[**copyPadUsingGET**](DefaultApi.md#copyPadUsingGET) | **GET** /copyPad | 
[**copyPadUsingPOST**](DefaultApi.md#copyPadUsingPOST) | **POST** /copyPad | 
[**copyPadWithoutHistoryUsingGET**](DefaultApi.md#copyPadWithoutHistoryUsingGET) | **GET** /copyPadWithoutHistory | 
[**copyPadWithoutHistoryUsingPOST**](DefaultApi.md#copyPadWithoutHistoryUsingPOST) | **POST** /copyPadWithoutHistory | 
[**getAttributePoolUsingGET**](DefaultApi.md#getAttributePoolUsingGET) | **GET** /getAttributePool | 
[**getAttributePoolUsingPOST**](DefaultApi.md#getAttributePoolUsingPOST) | **POST** /getAttributePool | 
[**getPadIDUsingGET**](DefaultApi.md#getPadIDUsingGET) | **GET** /getPadID | 
[**getPadIDUsingPOST**](DefaultApi.md#getPadIDUsingPOST) | **POST** /getPadID | 
[**getRevisionChangesetUsingGET**](DefaultApi.md#getRevisionChangesetUsingGET) | **GET** /getRevisionChangeset | 
[**getRevisionChangesetUsingPOST**](DefaultApi.md#getRevisionChangesetUsingPOST) | **POST** /getRevisionChangeset | 
[**getSavedRevisionsCountUsingGET**](DefaultApi.md#getSavedRevisionsCountUsingGET) | **GET** /getSavedRevisionsCount | 
[**getSavedRevisionsCountUsingPOST**](DefaultApi.md#getSavedRevisionsCountUsingPOST) | **POST** /getSavedRevisionsCount | 
[**getStatsUsingGET**](DefaultApi.md#getStatsUsingGET) | **GET** /getStats | 
[**getStatsUsingPOST**](DefaultApi.md#getStatsUsingPOST) | **POST** /getStats | 
[**listSavedRevisionsUsingGET**](DefaultApi.md#listSavedRevisionsUsingGET) | **GET** /listSavedRevisions | 
[**listSavedRevisionsUsingPOST**](DefaultApi.md#listSavedRevisionsUsingPOST) | **POST** /listSavedRevisions | 
[**movePadUsingGET**](DefaultApi.md#movePadUsingGET) | **GET** /movePad | 
[**movePadUsingPOST**](DefaultApi.md#movePadUsingPOST) | **POST** /movePad | 
[**restoreRevisionUsingGET**](DefaultApi.md#restoreRevisionUsingGET) | **GET** /restoreRevision | 
[**restoreRevisionUsingPOST**](DefaultApi.md#restoreRevisionUsingPOST) | **POST** /restoreRevision | 
[**saveRevisionUsingGET**](DefaultApi.md#saveRevisionUsingGET) | **GET** /saveRevision | 
[**saveRevisionUsingPOST**](DefaultApi.md#saveRevisionUsingPOST) | **POST** /saveRevision | 



## appendTextUsingGET

> AppendChatMessageUsingGET200Response appendTextUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.appendTextUsingGET(opts, (error, data, response) => {
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


## appendTextUsingPOST

> AppendChatMessageUsingGET200Response appendTextUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'text': "text_example" // String | 
};
apiInstance.appendTextUsingPOST(opts, (error, data, response) => {
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


## copyPadUsingGET

> AppendChatMessageUsingGET200Response copyPadUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'sourceID': "sourceID_example", // String | 
  'destinationID': "destinationID_example", // String | 
  'force': "force_example" // String | 
};
apiInstance.copyPadUsingGET(opts, (error, data, response) => {
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
 **sourceID** | **String**|  | [optional] 
 **destinationID** | **String**|  | [optional] 
 **force** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## copyPadUsingPOST

> AppendChatMessageUsingGET200Response copyPadUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'sourceID': "sourceID_example", // String | 
  'destinationID': "destinationID_example", // String | 
  'force': "force_example" // String | 
};
apiInstance.copyPadUsingPOST(opts, (error, data, response) => {
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
 **sourceID** | **String**|  | [optional] 
 **destinationID** | **String**|  | [optional] 
 **force** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## copyPadWithoutHistoryUsingGET

> AppendChatMessageUsingGET200Response copyPadWithoutHistoryUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'sourceID': "sourceID_example", // String | 
  'destinationID': "destinationID_example", // String | 
  'force': "force_example" // String | 
};
apiInstance.copyPadWithoutHistoryUsingGET(opts, (error, data, response) => {
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
 **sourceID** | **String**|  | [optional] 
 **destinationID** | **String**|  | [optional] 
 **force** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## copyPadWithoutHistoryUsingPOST

> AppendChatMessageUsingGET200Response copyPadWithoutHistoryUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'sourceID': "sourceID_example", // String | 
  'destinationID': "destinationID_example", // String | 
  'force': "force_example" // String | 
};
apiInstance.copyPadWithoutHistoryUsingPOST(opts, (error, data, response) => {
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
 **sourceID** | **String**|  | [optional] 
 **destinationID** | **String**|  | [optional] 
 **force** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttributePoolUsingGET

> AppendChatMessageUsingGET200Response getAttributePoolUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getAttributePoolUsingGET(opts, (error, data, response) => {
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


## getAttributePoolUsingPOST

> AppendChatMessageUsingGET200Response getAttributePoolUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getAttributePoolUsingPOST(opts, (error, data, response) => {
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


## getPadIDUsingGET

> AppendChatMessageUsingGET200Response getPadIDUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'roID': "roID_example" // String | 
};
apiInstance.getPadIDUsingGET(opts, (error, data, response) => {
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
 **roID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPadIDUsingPOST

> AppendChatMessageUsingGET200Response getPadIDUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'roID': "roID_example" // String | 
};
apiInstance.getPadIDUsingPOST(opts, (error, data, response) => {
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
 **roID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRevisionChangesetUsingGET

> AppendChatMessageUsingGET200Response getRevisionChangesetUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.getRevisionChangesetUsingGET(opts, (error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRevisionChangesetUsingPOST

> AppendChatMessageUsingGET200Response getRevisionChangesetUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.getRevisionChangesetUsingPOST(opts, (error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSavedRevisionsCountUsingGET

> AppendChatMessageUsingGET200Response getSavedRevisionsCountUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getSavedRevisionsCountUsingGET(opts, (error, data, response) => {
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


## getSavedRevisionsCountUsingPOST

> AppendChatMessageUsingGET200Response getSavedRevisionsCountUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.getSavedRevisionsCountUsingPOST(opts, (error, data, response) => {
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


## getStatsUsingGET

> AppendChatMessageUsingGET200Response getStatsUsingGET()



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
apiInstance.getStatsUsingGET((error, data, response) => {
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


## getStatsUsingPOST

> AppendChatMessageUsingGET200Response getStatsUsingPOST()



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
apiInstance.getStatsUsingPOST((error, data, response) => {
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


## listSavedRevisionsUsingGET

> AppendChatMessageUsingGET200Response listSavedRevisionsUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.listSavedRevisionsUsingGET(opts, (error, data, response) => {
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


## listSavedRevisionsUsingPOST

> AppendChatMessageUsingGET200Response listSavedRevisionsUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example" // String | 
};
apiInstance.listSavedRevisionsUsingPOST(opts, (error, data, response) => {
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


## movePadUsingGET

> AppendChatMessageUsingGET200Response movePadUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'sourceID': "sourceID_example", // String | 
  'destinationID': "destinationID_example", // String | 
  'force': "force_example" // String | 
};
apiInstance.movePadUsingGET(opts, (error, data, response) => {
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
 **sourceID** | **String**|  | [optional] 
 **destinationID** | **String**|  | [optional] 
 **force** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## movePadUsingPOST

> AppendChatMessageUsingGET200Response movePadUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'sourceID': "sourceID_example", // String | 
  'destinationID': "destinationID_example", // String | 
  'force': "force_example" // String | 
};
apiInstance.movePadUsingPOST(opts, (error, data, response) => {
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
 **sourceID** | **String**|  | [optional] 
 **destinationID** | **String**|  | [optional] 
 **force** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restoreRevisionUsingGET

> AppendChatMessageUsingGET200Response restoreRevisionUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.restoreRevisionUsingGET(opts, (error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restoreRevisionUsingPOST

> AppendChatMessageUsingGET200Response restoreRevisionUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.restoreRevisionUsingPOST(opts, (error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveRevisionUsingGET

> AppendChatMessageUsingGET200Response saveRevisionUsingGET(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.saveRevisionUsingGET(opts, (error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveRevisionUsingPOST

> AppendChatMessageUsingGET200Response saveRevisionUsingPOST(opts)



### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.DefaultApi();
let opts = {
  'padID': "padID_example", // String | 
  'rev': "rev_example" // String | 
};
apiInstance.saveRevisionUsingPOST(opts, (error, data, response) => {
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

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

