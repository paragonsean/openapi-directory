# TheConsumerFinancialProtectionBureau.HmdaApi

All URIs are relative to *https://api.consumerfinance.gov:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConceptHmda**](HmdaApi.md#getConceptHmda) | **GET** /data/hmda/concept/{concept} | Get information about a particular concept in this dataset.
[**getDatasetHmda**](HmdaApi.md#getDatasetHmda) | **GET** /data/hmda | Get metadata for this dataset.
[**getSliceMetadataHmda**](HmdaApi.md#getSliceMetadataHmda) | **GET** /data/hmda/slice/{slice}/metadata | Get the metadata for a slice in this dataset.
[**querySliceHmda**](HmdaApi.md#querySliceHmda) | **GET** /data/hmda/slice/{slice} | Query a slice in this dataset.



## getConceptHmda

> getConceptHmda(concept)

Get information about a particular concept in this dataset.

### Example

```javascript
import TheConsumerFinancialProtectionBureau from 'the_consumer_financial_protection_bureau';

let apiInstance = new TheConsumerFinancialProtectionBureau.HmdaApi();
let concept = "concept_example"; // String | Name of concept
apiInstance.getConceptHmda(concept, (error, data, response) => {
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
 **concept** | **String**| Name of concept | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDatasetHmda

> getDatasetHmda()

Get metadata for this dataset.

### Example

```javascript
import TheConsumerFinancialProtectionBureau from 'the_consumer_financial_protection_bureau';

let apiInstance = new TheConsumerFinancialProtectionBureau.HmdaApi();
apiInstance.getDatasetHmda((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSliceMetadataHmda

> getSliceMetadataHmda(slice)

Get the metadata for a slice in this dataset.

### Example

```javascript
import TheConsumerFinancialProtectionBureau from 'the_consumer_financial_protection_bureau';

let apiInstance = new TheConsumerFinancialProtectionBureau.HmdaApi();
let slice = "slice_example"; // String | Name of slice
apiInstance.getSliceMetadataHmda(slice, (error, data, response) => {
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
 **slice** | **String**| Name of slice | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## querySliceHmda

> QueryResponse querySliceHmda(slice, opts)

Query a slice in this dataset.

### Example

```javascript
import TheConsumerFinancialProtectionBureau from 'the_consumer_financial_protection_bureau';

let apiInstance = new TheConsumerFinancialProtectionBureau.HmdaApi();
let slice = "slice_example"; // String | Name of slice
let opts = {
  'select': "select_example", // String | Fields to return, separated by commas.
  'where': "where_example", // String | Conditions to search for in the slice, in SQL WHERE style.
  'group': "group_example", // String | Fields to group by, summarizing the data, separated by commas.
  'limit': 56, // Number | Number of records to return, 100 by default. Enter 0 for no limit.
  'offset': 56, // Number | Number of records to skip.
  'orderBy': "orderBy_example", // String | Fields to order by, separated by commas. ASC and DESC can be used to modify the order.
  'callback': "callback_example" // String | JavaScript callback to invoke. Only useful with JSONP requests.
};
apiInstance.querySliceHmda(slice, opts, (error, data, response) => {
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
 **slice** | **String**| Name of slice | 
 **select** | **String**| Fields to return, separated by commas. | [optional] 
 **where** | **String**| Conditions to search for in the slice, in SQL WHERE style. | [optional] 
 **group** | **String**| Fields to group by, summarizing the data, separated by commas. | [optional] 
 **limit** | **Number**| Number of records to return, 100 by default. Enter 0 for no limit. | [optional] 
 **offset** | **Number**| Number of records to skip. | [optional] 
 **orderBy** | **String**| Fields to order by, separated by commas. ASC and DESC can be used to modify the order. | [optional] 
 **callback** | **String**| JavaScript callback to invoke. Only useful with JSONP requests. | [optional] 

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/javascript, text/csv

