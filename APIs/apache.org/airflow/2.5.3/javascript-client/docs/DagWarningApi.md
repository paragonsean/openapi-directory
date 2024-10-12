# AirflowApiStable.DagWarningApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDagWarnings**](DagWarningApi.md#getDagWarnings) | **GET** /dagWarnings | List dag warnings



## getDagWarnings

> DagWarningCollection getDagWarnings(opts)

List dag warnings

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.DagWarningApi();
let opts = {
  'dagId': "dagId_example", // String | If set, only return DAG warnings with this dag_id.
  'warningType': "warningType_example", // String | If set, only return DAG warnings with this type.
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getDagWarnings(opts, (error, data, response) => {
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
 **dagId** | **String**| If set, only return DAG warnings with this dag_id. | [optional] 
 **warningType** | **String**| If set, only return DAG warnings with this type. | [optional] 
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**DagWarningCollection**](DagWarningCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

