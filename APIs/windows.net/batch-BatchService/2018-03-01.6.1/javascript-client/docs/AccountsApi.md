# BatchService.AccountsApi

All URIs are relative to *https://batch.core.windows.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountListNodeAgentSkus**](AccountsApi.md#accountListNodeAgentSkus) | **GET** /nodeagentskus | Lists all node agent SKUs supported by the Azure Batch service.
[**accountListPoolNodeCounts**](AccountsApi.md#accountListPoolNodeCounts) | **GET** /nodecounts | 



## accountListNodeAgentSkus

> AccountListNodeAgentSkusResult accountListNodeAgentSkus(apiVersion, opts)

Lists all node agent SKUs supported by the Azure Batch service.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.AccountsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-node-agent-skus.
  'maxresults': 1000, // Number | The maximum number of items to return in the response. A maximum of 1000 results will be returned.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.accountListNodeAgentSkus(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-node-agent-skus. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. A maximum of 1000 results will be returned. | [optional] [default to 1000]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**AccountListNodeAgentSkusResult**](AccountListNodeAgentSkusResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountListPoolNodeCounts

> PoolNodeCountsListResult accountListPoolNodeCounts(apiVersion, opts)



Gets the number of nodes in each state, grouped by pool.

### Example

```javascript
import BatchService from 'batch_service';

let apiInstance = new BatchService.AccountsApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let opts = {
  'filter': "filter_example", // String | An OData $filter clause.
  'maxresults': 10, // Number | The maximum number of items to return in the response.
  'timeout': 30, // Number | The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
  'clientRequestId': "clientRequestId_example", // String | The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
  'returnClientRequestId': false, // Boolean | Whether the server should return the client-request-id in the response.
  'ocpDate': "ocpDate_example" // String | The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
};
apiInstance.accountListPoolNodeCounts(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **filter** | **String**| An OData $filter clause. | [optional] 
 **maxresults** | **Number**| The maximum number of items to return in the response. | [optional] [default to 10]
 **timeout** | **Number**| The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. | [optional] [default to 30]
 **clientRequestId** | **String**| The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0. | [optional] 
 **returnClientRequestId** | **Boolean**| Whether the server should return the client-request-id in the response. | [optional] [default to false]
 **ocpDate** | **String**| The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. | [optional] 

### Return type

[**PoolNodeCountsListResult**](PoolNodeCountsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

