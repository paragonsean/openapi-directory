# EinsteinVisionAndEinsteinLanguage.VisionExamplesApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addExample**](VisionExamplesApi.md#addExample) | **POST** /v2/vision/datasets/{datasetId}/examples | Create an Example
[**getExamples1**](VisionExamplesApi.md#getExamples1) | **GET** /v2/vision/datasets/{datasetId}/examples | Get All Examples
[**getExamplesByLabel1**](VisionExamplesApi.md#getExamplesByLabel1) | **GET** /v2/vision/examples | Get All Examples for Label
[**provideFeedback1**](VisionExamplesApi.md#provideFeedback1) | **POST** /v2/vision/feedback | Create a Feedback Example
[**updateDatasetAsync1**](VisionExamplesApi.md#updateDatasetAsync1) | **PUT** /v2/vision/bulkfeedback | Create Feedback Examples From a Zip File
[**updateDatasetAsync2**](VisionExamplesApi.md#updateDatasetAsync2) | **PUT** /v2/vision/datasets/{datasetId}/upload | Create Examples From a Zip File



## addExample

> Example addExample(datasetId, opts)

Create an Example

Adds an example with the specified label to a dataset.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionExamplesApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
let opts = {
  'data': "data_example", // String | Location of the local image file to upload.
  'labelId': 789, // Number | ID of the label to add to the example.
  'name': "name_example" // String | Name of the example. Maximum length is 180 characters.
};
apiInstance.addExample(datasetId, opts, (error, data, response) => {
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
 **data** | **String**| Location of the local image file to upload. | [optional] 
 **labelId** | **Number**| ID of the label to add to the example. | [optional] 
 **name** | **String**| Name of the example. Maximum length is 180 characters. | [optional] 

### Return type

[**Example**](Example.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## getExamples1

> ExampleList getExamples1(datasetId, opts)

Get All Examples

Returns all the examples for the specified dataset. By default, returns examples created by uploading them from a .zip file.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionExamplesApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
let opts = {
  'offset': "'0'", // String | Index of the example from which you want to start paging.
  'count': "'100'", // String | Number of examples to return.
  'source': "source_example" // String | return examples that were created in the dataset as feedback
};
apiInstance.getExamples1(datasetId, opts, (error, data, response) => {
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
 **offset** | **String**| Index of the example from which you want to start paging. | [optional] [default to &#39;0&#39;]
 **count** | **String**| Number of examples to return. | [optional] [default to &#39;100&#39;]
 **source** | **String**| return examples that were created in the dataset as feedback | [optional] 

### Return type

[**ExampleList**](ExampleList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExamplesByLabel1

> ExampleList getExamplesByLabel1(opts)

Get All Examples for Label

Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionExamplesApi();
let opts = {
  'labelId': "SomeLabelId", // String | Label Id
  'offset': "'0'", // String | Index of the example from which you want to start paging.
  'count': "'100'" // String | Number of examples to return.
};
apiInstance.getExamplesByLabel1(opts, (error, data, response) => {
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
 **labelId** | **String**| Label Id | [optional] 
 **offset** | **String**| Index of the example from which you want to start paging. | [optional] [default to &#39;0&#39;]
 **count** | **String**| Number of examples to return. | [optional] [default to &#39;100&#39;]

### Return type

[**ExampleList**](ExampleList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## provideFeedback1

> Example provideFeedback1(opts)

Create a Feedback Example

Adds a feedback example to the dataset associated with the specified model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionExamplesApi();
let opts = {
  'data': "data_example", // String | Local image file to upload.
  'expectedLabel': "expectedLabel_example", // String | Correct label for the example. Must be a label that exists in the dataset.
  'modelId': "modelId_example", // String | ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model.
  'name': "name_example" // String | Name of the example. Optional. Maximum length is 180 characters.
};
apiInstance.provideFeedback1(opts, (error, data, response) => {
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
 **data** | **String**| Local image file to upload. | [optional] 
 **expectedLabel** | **String**| Correct label for the example. Must be a label that exists in the dataset. | [optional] 
 **modelId** | **String**| ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model. | [optional] 
 **name** | **String**| Name of the example. Optional. Maximum length is 180 characters. | [optional] 

### Return type

[**Example**](Example.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## updateDatasetAsync1

> Dataset updateDatasetAsync1(opts)

Create Feedback Examples From a Zip File

Adds feedback examples to the dataset associated with the specified object detection model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionExamplesApi();
let opts = {
  'data': "data_example", // String | Local .zip file to upload. The maximum .zip file size you can upload from a local drive is 50 MB.
  'modelId': "modelId_example" // String | ID of the model that misclassified the images. The feedback examples are added to the dataset associated with this model.
};
apiInstance.updateDatasetAsync1(opts, (error, data, response) => {
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
 **data** | **String**| Local .zip file to upload. The maximum .zip file size you can upload from a local drive is 50 MB. | [optional] 
 **modelId** | **String**| ID of the model that misclassified the images. The feedback examples are added to the dataset associated with this model. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## updateDatasetAsync2

> Dataset updateDatasetAsync2(datasetId, opts)

Create Examples From a Zip File

Adds examples from a .zip file to a dataset. You can use this call only with a dataset that was created from a .zip file.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.VisionExamplesApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
let opts = {
  'data': "data_example", // String | Location of the local image file to upload.
  'path': "path_example" // String | URL of the .zip file.
};
apiInstance.updateDatasetAsync2(datasetId, opts, (error, data, response) => {
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
 **data** | **String**| Location of the local image file to upload. | [optional] 
 **path** | **String**| URL of the .zip file. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

