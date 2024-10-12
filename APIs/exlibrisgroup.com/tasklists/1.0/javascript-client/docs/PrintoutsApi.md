# ExLibrisApis.PrintoutsApi

All URIs are relative to *https://api-eu.hosted.exlibrisgroup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAlmawsV1TaskListsPrintouts**](PrintoutsApi.md#getAlmawsV1TaskListsPrintouts) | **GET** /almaws/v1/task-lists/printouts | Retrieve Printouts
[**getAlmawsV1TaskListsPrintoutsPrintoutId**](PrintoutsApi.md#getAlmawsV1TaskListsPrintoutsPrintoutId) | **GET** /almaws/v1/task-lists/printouts/{printout_id} | Retrieve a Printout
[**postAlmawsV1TaskListsPrintouts**](PrintoutsApi.md#postAlmawsV1TaskListsPrintouts) | **POST** /almaws/v1/task-lists/printouts | Act on Printouts
[**postAlmawsV1TaskListsPrintoutsPrintoutId**](PrintoutsApi.md#postAlmawsV1TaskListsPrintoutsPrintoutId) | **POST** /almaws/v1/task-lists/printouts/{printout_id} | Printout Service



## getAlmawsV1TaskListsPrintouts

> GetAlmawsV1TaskListsPrintouts200Response getAlmawsV1TaskListsPrintouts(opts)

Retrieve Printouts

This API returns a list of Printouts.

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.PrintoutsApi();
let opts = {
  'letter': "'ALL'", // String | Printout Name. Optional. 
  'status': "'ALL'", // String | Printout status. Optional. Valid values are: Printed, Pending, Canceled.
  'printerId': "'ALL'", // String | Printout Printer
  'printoutId': "'ALL'", // String | A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters
  'limit': 56, // Number | Limits the number of results. Optional. Valid values are 0-100. Default value: 10.
  'offset': 56 // Number | Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned.
};
apiInstance.getAlmawsV1TaskListsPrintouts(opts, (error, data, response) => {
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
 **letter** | **String**| Printout Name. Optional.  | [optional] [default to &#39;ALL&#39;]
 **status** | **String**| Printout status. Optional. Valid values are: Printed, Pending, Canceled. | [optional] [default to &#39;ALL&#39;]
 **printerId** | **String**| Printout Printer | [optional] [default to &#39;ALL&#39;]
 **printoutId** | **String**| A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters | [optional] [default to &#39;ALL&#39;]
 **limit** | **Number**| Limits the number of results. Optional. Valid values are 0-100. Default value: 10. | [optional] 
 **offset** | **Number**| Offset of the results returned. Optional. Default value: 0, which means that the first results will be returned. | [optional] 

### Return type

[**GetAlmawsV1TaskListsPrintouts200Response**](GetAlmawsV1TaskListsPrintouts200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getAlmawsV1TaskListsPrintoutsPrintoutId

> Object getAlmawsV1TaskListsPrintoutsPrintoutId(printoutId)

Retrieve a Printout

This Web service returns a Printout given a Printout ID.

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.PrintoutsApi();
let printoutId = "printoutId_example"; // String | The Printout ID
apiInstance.getAlmawsV1TaskListsPrintoutsPrintoutId(printoutId, (error, data, response) => {
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
 **printoutId** | **String**| The Printout ID | 

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## postAlmawsV1TaskListsPrintouts

> Object postAlmawsV1TaskListsPrintouts(op, opts)

Act on Printouts

This API performs an action on printouts: mark as printed or canceled. 10,000 records can be handled in one requests. Only printouts which were updated will be returned.

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.PrintoutsApi();
let op = "op_example"; // String | The operation to perform on the printout. Currently, the options are: 'mark_as_printed','mark_as_canceled'
let opts = {
  'letter': "'ALL'", // String | Printout Name. Optional. 
  'status': "'ALL'", // String | Printout status. Optional. Valid values are: Printed, Pending, Canceled.
  'printerId': "'ALL'", // String | Printout Printer
  'printoutId': "'ALL'" // String | A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters
};
apiInstance.postAlmawsV1TaskListsPrintouts(op, opts, (error, data, response) => {
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
 **op** | **String**| The operation to perform on the printout. Currently, the options are: &#39;mark_as_printed&#39;,&#39;mark_as_canceled&#39; | 
 **letter** | **String**| Printout Name. Optional.  | [optional] [default to &#39;ALL&#39;]
 **status** | **String**| Printout status. Optional. Valid values are: Printed, Pending, Canceled. | [optional] [default to &#39;ALL&#39;]
 **printerId** | **String**| Printout Printer | [optional] [default to &#39;ALL&#39;]
 **printoutId** | **String**| A list of Printout IDs (for example: 123,456,778) from 1 to the limit of 100 Optional. Use of this option overrides all of the filtering parameters | [optional] [default to &#39;ALL&#39;]

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## postAlmawsV1TaskListsPrintoutsPrintoutId

> Object postAlmawsV1TaskListsPrintoutsPrintoutId(printoutId, op)

Printout Service

This API operates on an printout. given a Printout ID.

### Example

```javascript
import ExLibrisApis from 'ex_libris_apis';
let defaultClient = ExLibrisApis.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ExLibrisApis.PrintoutsApi();
let printoutId = "printoutId_example"; // String | The Printout ID
let op = "op_example"; // String | The operation to perform on the printout. Currently, the options are 'mark_as_printed','mark_as_canceled'
apiInstance.postAlmawsV1TaskListsPrintoutsPrintoutId(printoutId, op, (error, data, response) => {
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
 **printoutId** | **String**| The Printout ID | 
 **op** | **String**| The operation to perform on the printout. Currently, the options are &#39;mark_as_printed&#39;,&#39;mark_as_canceled&#39; | 

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

