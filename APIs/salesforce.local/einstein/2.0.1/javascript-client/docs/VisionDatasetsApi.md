# EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDataset**](VisionDatasetsApi.md#createDataset) | **POST** /v2/vision/datasets | Create a Dataset
[**deleteDataset1**](VisionDatasetsApi.md#deleteDataset1) | **DELETE** /v2/vision/datasets/{datasetId} | Delete a Dataset
[**get1**](VisionDatasetsApi.md#get1) | **GET** /v2/vision/deletion/{id} | Get Deletion Status
[**getDataset1**](VisionDatasetsApi.md#getDataset1) | **GET** /v2/vision/datasets/{datasetId} | Get a Dataset
[**listDatasets1**](VisionDatasetsApi.md#listDatasets1) | **GET** /v2/vision/datasets | Get All Datasets
[**uploadDatasetAsync1**](VisionDatasetsApi.md#uploadDatasetAsync1) | **POST** /v2/vision/datasets/upload | Create a Dataset From a Zip File Asynchronously
[**uploadDatasetSync1**](VisionDatasetsApi.md#uploadDatasetSync1) | **POST** /v2/vision/datasets/upload/sync | Create a Dataset From a Zip File Synchronously



## createDataset

> Dataset createDataset(opts)

Create a Dataset

Creates a dataset and labels, if they&#39;re specified.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let opts = {
  'labels': "labels_example", // String | Optional comma-separated list of labels. If specified, creates the labels in the dataset. Maximum number of labels per dataset is 250.
  'name': "name_example", // String | Name of the dataset. Maximum length is 180 characters.
  'type': "type_example" // String | Type of dataset data
};
apiInstance.createDataset(opts, (error, data, response) => {
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
 **labels** | **String**| Optional comma-separated list of labels. If specified, creates the labels in the dataset. Maximum number of labels per dataset is 250. | [optional] 
 **name** | **String**| Name of the dataset. Maximum length is 180 characters. | [optional] 
 **type** | **String**| Type of dataset data | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## deleteDataset1

> DeletionResponse deleteDataset1(datasetId)

Delete a Dataset

Deletes the specified dataset and associated labels and examples.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
apiInstance.deleteDataset1(datasetId, (error, data, response) => {
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


## get1

> DeletionResponse get1(id)

Get Deletion Status

Returns the status of an image dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let id = "Z2JTFBF3A7XKIJC5QEJXMO4HSY"; // String | Deletion Id
apiInstance.get1(id, (error, data, response) => {
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


## getDataset1

> Dataset getDataset1(datasetId)

Get a Dataset

Returns a single dataset.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
apiInstance.getDataset1(datasetId, (error, data, response) => {
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


## listDatasets1

> DatasetList listDatasets1(opts)

Get All Datasets

Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let opts = {
  'offset': "'0'", // String | Index of the dataset from which you want to start paging
  'count': "'25'", // String | Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets.
  'global': false // Boolean | If true, returns all global datasets. Global datasets are public datasets that Salesforce provides.
};
apiInstance.listDatasets1(opts, (error, data, response) => {
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


## uploadDatasetAsync1

> Dataset uploadDatasetAsync1(opts)

Create a Dataset From a Zip File Asynchronously

Creates a dataset, labels, and examples from the specified .zip file. The call returns immediately and continues to upload the images in the background.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let opts = {
  'data': "data_example", // String | Path to the .zip file on the local drive (FilePart).
  'name': "name_example", // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name.
  'path': "path_example", // String | URL of the .zip file.
  'type': "type_example" // String | Type of dataset data.
};
apiInstance.uploadDatasetAsync1(opts, (error, data, response) => {
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
 **data** | **String**| Path to the .zip file on the local drive (FilePart). | [optional] 
 **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name. | [optional] 
 **path** | **String**| URL of the .zip file. | [optional] 
 **type** | **String**| Type of dataset data. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## uploadDatasetSync1

> Dataset uploadDatasetSync1(opts)

Create a Dataset From a Zip File Synchronously

Creates a dataset, labels, and examples from the specified .zip file. The call returns after the dataset is created and all of the images are uploaded.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionDatasetsApi();
let opts = {
  'data': "data_example", // String | Path to the .zip file on the local drive (FilePart).
  'name': "name_example", // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name.
  'path': "path_example", // String | URL of the .zip file.
  'type': "type_example" // String | Type of dataset data.
};
apiInstance.uploadDatasetSync1(opts, (error, data, response) => {
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
 **data** | **String**| Path to the .zip file on the local drive (FilePart). | [optional] 
 **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name. | [optional] 
 **path** | **String**| URL of the .zip file. | [optional] 
 **type** | **String**| Type of dataset data. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

