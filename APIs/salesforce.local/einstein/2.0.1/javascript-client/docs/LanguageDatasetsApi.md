# EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDataset**](LanguageDatasetsApi.md#deleteDataset) | **DELETE** /v2/language/datasets/{datasetId} | Delete a Dataset
[**get**](LanguageDatasetsApi.md#get) | **GET** /v2/language/deletion/{id} | Get Deletion Status
[**getDataset**](LanguageDatasetsApi.md#getDataset) | **GET** /v2/language/datasets/{datasetId} | Get a Dataset
[**listDatasets**](LanguageDatasetsApi.md#listDatasets) | **GET** /v2/language/datasets | Get All Datasets
[**uploadDatasetAsync**](LanguageDatasetsApi.md#uploadDatasetAsync) | **POST** /v2/language/datasets/upload | Create a Dataset From a File Asynchronously
[**uploadDatasetSync**](LanguageDatasetsApi.md#uploadDatasetSync) | **POST** /v2/language/datasets/upload/sync | Create a Dataset From a File Synchronously



## deleteDataset

> DeletionResponse deleteDataset(datasetId)

Delete a Dataset

Deletes the specified dataset and associated labels and examples.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
apiInstance.deleteDataset(datasetId, (error, data, response) => {
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
 **datasetId** | **String**| Dataset Id | 

### Return type

[**DeletionResponse**](DeletionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get

> DeletionResponse get(id)

Get Deletion Status

Returns the status of a language dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi();
let id = "Z2JTFBF3A7XKIJC5QEJXMO4HSY"; // String | Deletion Id
apiInstance.get(id, (error, data, response) => {
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
 **id** | **String**| Deletion Id | 

### Return type

[**DeletionResponse**](DeletionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataset

> Dataset getDataset(datasetId)

Get a Dataset

Returns a single dataset.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
apiInstance.getDataset(datasetId, (error, data, response) => {
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
 **datasetId** | **String**| Dataset Id | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDatasets

> DatasetList listDatasets(opts)

Get All Datasets

Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi();
let opts = {
  'offset': "'0'", // String | Index of the dataset from which you want to start paging
  'count': "'25'", // String | Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets.
  'global': false // Boolean | If true, returns all global datasets. Global datasets are public datasets that Salesforce provides.
};
apiInstance.listDatasets(opts, (error, data, response) => {
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
 **offset** | **String**| Index of the dataset from which you want to start paging | [optional] [default to &#39;0&#39;]
 **count** | **String**| Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets. | [optional] [default to &#39;25&#39;]
 **global** | **Boolean**| If true, returns all global datasets. Global datasets are public datasets that Salesforce provides. | [optional] [default to false]

### Return type

[**DatasetList**](DatasetList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadDatasetAsync

> Dataset uploadDatasetAsync(opts)

Create a Dataset From a File Asynchronously

Creates a dataset, labels, and examples from the specified .csv, .tsv, or .json file. The call returns immediately and continues to upload data in the background.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi();
let opts = {
  'data': "data_example", // String | Path to the .csv, .tsv, or .json file on the local drive (FilePart).
  'name': "name_example", // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name.
  'path': "path_example", // String | URL of the .csv, .tsv, or .json file.
  'type': "type_example" // String | Type of dataset data.
};
apiInstance.uploadDatasetAsync(opts, (error, data, response) => {
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
 **data** | **String**| Path to the .csv, .tsv, or .json file on the local drive (FilePart). | [optional] 
 **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name. | [optional] 
 **path** | **String**| URL of the .csv, .tsv, or .json file. | [optional] 
 **type** | **String**| Type of dataset data. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## uploadDatasetSync

> Dataset uploadDatasetSync(opts)

Create a Dataset From a File Synchronously

Creates a dataset, labels, and examples from the specified .csv, .tsv, or .json file. The call returns after the dataset is created and all of the data is uploaded.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageDatasetsApi();
let opts = {
  'data': "data_example", // String | Path to the .csv, .tsv, or .json file on the local drive (FilePart).
  'name': "name_example", // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name.
  'path': "path_example", // String | URL of the .csv, .tsv, or .json file.
  'type': "type_example" // String | Type of dataset data.
};
apiInstance.uploadDatasetSync(opts, (error, data, response) => {
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
 **data** | **String**| Path to the .csv, .tsv, or .json file on the local drive (FilePart). | [optional] 
 **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name. | [optional] 
 **path** | **String**| URL of the .csv, .tsv, or .json file. | [optional] 
 **type** | **String**| Type of dataset data. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

