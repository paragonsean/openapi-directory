# RedirectionIo.LogApi

All URIs are relative to *https://api.redirection.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLogCollection**](LogApi.md#getLogCollection) | **GET** /logs | Retrieves the collection of Log resources.
[**getLogItem**](LogApi.md#getLogItem) | **GET** /logs/{id} | Retrieves a Log resource.



## getLogCollection

> [LogRead] getLogCollection(opts)

Retrieves the collection of Log resources.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.LogApi();
let opts = {
  'page': 56, // Number | The collection page number
  'projectId': "projectId_example", // String | 
  'createdAt': "createdAt_example", // String | 
  'source': "source_example", // String | 
  'target': "target_example", // String | 
  'statusCode': "statusCode_example", // String | 
  'referrer': "referrer_example", // String | 
  'userAgent': "userAgent_example", // String | 
  'userAgentType': "userAgentType_example", // String | 
  'simplifiedUserAgent': "simplifiedUserAgent_example", // String | 
  'ruleId': "ruleId_example", // String | 
  'instanceName': "instanceName_example", // String | 
  'excludeUrls': "excludeUrls_example", // String | 
  'excludeEmptyReferrer': "excludeEmptyReferrer_example", // String | 
  'createdAtGt': "createdAtGt_example", // String | 
  'createdAtGte': "createdAtGte_example", // String | 
  'createdAtLt': "createdAtLt_example", // String | 
  'createdAtLte': "createdAtLte_example", // String | 
  'statusCodeGt': "statusCodeGt_example", // String | 
  'statusCodeGte': "statusCodeGte_example", // String | 
  'statusCodeLt': "statusCodeLt_example", // String | 
  'statusCodeLte': "statusCodeLte_example" // String | 
};
apiInstance.getLogCollection(opts, (error, data, response) => {
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
 **page** | **Number**| The collection page number | [optional] 
 **projectId** | **String**|  | [optional] 
 **createdAt** | **String**|  | [optional] 
 **source** | **String**|  | [optional] 
 **target** | **String**|  | [optional] 
 **statusCode** | **String**|  | [optional] 
 **referrer** | **String**|  | [optional] 
 **userAgent** | **String**|  | [optional] 
 **userAgentType** | **String**|  | [optional] 
 **simplifiedUserAgent** | **String**|  | [optional] 
 **ruleId** | **String**|  | [optional] 
 **instanceName** | **String**|  | [optional] 
 **excludeUrls** | **String**|  | [optional] 
 **excludeEmptyReferrer** | **String**|  | [optional] 
 **createdAtGt** | **String**|  | [optional] 
 **createdAtGte** | **String**|  | [optional] 
 **createdAtLt** | **String**|  | [optional] 
 **createdAtLte** | **String**|  | [optional] 
 **statusCodeGt** | **String**|  | [optional] 
 **statusCodeGte** | **String**|  | [optional] 
 **statusCodeLt** | **String**|  | [optional] 
 **statusCodeLte** | **String**|  | [optional] 

### Return type

[**[LogRead]**](LogRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv


## getLogItem

> LogRead getLogItem(id)

Retrieves a Log resource.

### Example

```javascript
import RedirectionIo from 'redirection_io';
let defaultClient = RedirectionIo.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new RedirectionIo.LogApi();
let id = "id_example"; // String | 
apiInstance.getLogItem(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**LogRead**](LogRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json, application/json, text/html, text/csv

