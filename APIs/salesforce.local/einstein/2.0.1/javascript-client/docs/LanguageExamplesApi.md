# EinsteinVisionAndEinsteinLanguage.LanguageExamplesApi

All URIs are relative to *http://salesforce.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getExamples**](LanguageExamplesApi.md#getExamples) | **GET** /v2/language/datasets/{datasetId}/examples | Get All Examples
[**getExamplesByLabel**](LanguageExamplesApi.md#getExamplesByLabel) | **GET** /v2/language/examples | Get All Examples for Label
[**provideFeedback**](LanguageExamplesApi.md#provideFeedback) | **POST** /v2/language/feedback | Create a Feedback Example
[**updateDatasetAsync**](LanguageExamplesApi.md#updateDatasetAsync) | **PUT** /v2/language/datasets/{datasetId}/upload | Create Examples From a File



## getExamples

> ExampleList getExamples(datasetId, opts)

Get All Examples

Returns all the examples for the specified dataset,

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageExamplesApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
let opts = {
  'offset': "'0'", // String | Index of the example from which you want to start paging.
  'count': "'100'", // String | Number of examples to return.
  'source': "source_example" // String | return examples that were created in the dataset as feedback
};
apiInstance.getExamples(datasetId, opts, (error, data, response) => {
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


## getExamplesByLabel

> ExampleList getExamplesByLabel(opts)

Get All Examples for Label

Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageExamplesApi();
let opts = {
  'labelId': "SomeLabelId", // String | Label Id
  'offset': "'0'", // String | Index of the example from which you want to start paging.
  'count': "'100'" // String | Number of examples to return.
};
apiInstance.getExamplesByLabel(opts, (error, data, response) => {
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


## provideFeedback

> Example provideFeedback(opts)

Create a Feedback Example

Adds a feedback example to the dataset associated with the specified model.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageExamplesApi();
let opts = {
  'document': "document_example", // String | Intent or sentiment string to add to the dataset.
  'expectedLabel': "expectedLabel_example", // String | Correct label for the example. Must be a label that exists in the dataset.
  'modelId': "modelId_example", // String | ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model.
  'name': "name_example" // String | Name of the example. Optional. Maximum length is 180 characters.
};
apiInstance.provideFeedback(opts, (error, data, response) => {
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
 **document** | **String**| Intent or sentiment string to add to the dataset. | [optional] 
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


## updateDatasetAsync

> Dataset updateDatasetAsync(datasetId, opts)

Create Examples From a File

Adds examples from a .csv, .tsv, or .json file to a dataset.

### Example

```javascript
import EinsteinVisionAndEinsteinLanguage from 'einstein_vision_and_einstein_language';
let defaultClient = EinsteinVisionAndEinsteinLanguage.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_token
let bearer_token = defaultClient.authentications['bearer_token'];
bearer_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EinsteinVisionAndEinsteinLanguage.LanguageExamplesApi();
let datasetId = "SomeDatasetId"; // String | Dataset Id
let opts = {
  'data': "data_example", // String | Path to the .csv, .tsv, or .json file on a local drive. 
  'type': "type_example" // String | URL of the .csv, .tsv, or .json file.
};
apiInstance.updateDatasetAsync(datasetId, opts, (error, data, response) => {
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
 **data** | **String**| Path to the .csv, .tsv, or .json file on a local drive.  | [optional] 
 **type** | **String**| URL of the .csv, .tsv, or .json file. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

