# TheConsumerFinancialProtectionBureau.DataApi

All URIs are relative to *https://api.consumerfinance.gov:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataset**](DataApi.md#getDataset) | **GET** /data/{dataset} | Get metadata about a dataset.
[**getDatasets**](DataApi.md#getDatasets) | **GET** /data | Get a list of all datasets.



## getDataset

> getDataset(dataset)

Get metadata about a dataset.

### Example

```javascript
import TheConsumerFinancialProtectionBureau from 'the_consumer_financial_protection_bureau';

let apiInstance = new TheConsumerFinancialProtectionBureau.DataApi();
let dataset = "dataset_example"; // String | Name of dataset
apiInstance.getDataset(dataset, (error, data, response) => {
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
 **dataset** | **String**| Name of dataset | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDatasets

> getDatasets()

Get a list of all datasets.

### Example

```javascript
import TheConsumerFinancialProtectionBureau from 'the_consumer_financial_protection_bureau';

let apiInstance = new TheConsumerFinancialProtectionBureau.DataApi();
apiInstance.getDatasets((error, data, response) => {
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

