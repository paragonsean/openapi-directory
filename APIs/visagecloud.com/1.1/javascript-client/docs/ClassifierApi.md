# VisageCloud.ClassifierApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSVMClassifierUsingPOST**](ClassifierApi.md#addSVMClassifierUsingPOST) | **POST** /rest/v1.1/classifier/svm | Create new SVM classifier with given name
[**getClassiferFullUsingGET**](ClassifierApi.md#getClassiferFullUsingGET) | **GET** /rest/v1.1/classifier/svm | Get classifier full
[**getClassiferStatusUsingGET**](ClassifierApi.md#getClassiferStatusUsingGET) | **GET** /rest/v1.1/classifier/svm/status | Get classifer status
[**removeClassiferUsingDELETE**](ClassifierApi.md#removeClassiferUsingDELETE) | **DELETE** /rest/v1.1/classifier/svm | Delete existing classifier



## addSVMClassifierUsingPOST

> RestResponse addSVMClassifierUsingPOST(accessKey, secretKey, name, collectionIds, classificationAttributeName, opts)

Create new SVM classifier with given name

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ClassifierApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let name = "name_example"; // String | The name of the SVM classifier that will be created
let collectionIds = ["null"]; // [String] | Collection ids
let classificationAttributeName = "classificationAttributeName_example"; // String | Classification attribute name
let opts = {
  'preprocessor': "'FeaturePreprocessor'", // String | Preprocessor
  'considerViewPoints': false, // Boolean | Consider view point
  'seed': 179425537, // Number | Seed for divididing training and evaluation sets
  'trainingRatio': 0.8, // Number | Training ratio
  'probabilityParameter': 1, // Number | Probability parameter
  'gammaParameter': 0.5, // Number | Gamma parameter
  'nuParameter': 0.25, // Number | Nu parameter
  'cParameter': 1.0, // Number | c parameter
  'svmTypeParameter': 0, // Number | SVM type parameter
  'kernelTypeParameter': 0, // Number | Kernel type parameter
  'cacheSizeParameter': 500.0, // Number | Cache size parameter
  'epsParameter': 0.001 // Number | Eps parameter
};
apiInstance.addSVMClassifierUsingPOST(accessKey, secretKey, name, collectionIds, classificationAttributeName, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **name** | **String**| The name of the SVM classifier that will be created | 
 **collectionIds** | [**[String]**](String.md)| Collection ids | 
 **classificationAttributeName** | **String**| Classification attribute name | 
 **preprocessor** | **String**| Preprocessor | [optional] [default to &#39;FeaturePreprocessor&#39;]
 **considerViewPoints** | **Boolean**| Consider view point | [optional] [default to false]
 **seed** | **Number**| Seed for divididing training and evaluation sets | [optional] [default to 179425537]
 **trainingRatio** | **Number**| Training ratio | [optional] [default to 0.8]
 **probabilityParameter** | **Number**| Probability parameter | [optional] [default to 1]
 **gammaParameter** | **Number**| Gamma parameter | [optional] [default to 0.5]
 **nuParameter** | **Number**| Nu parameter | [optional] [default to 0.25]
 **cParameter** | **Number**| c parameter | [optional] [default to 1.0]
 **svmTypeParameter** | **Number**| SVM type parameter | [optional] [default to 0]
 **kernelTypeParameter** | **Number**| Kernel type parameter | [optional] [default to 0]
 **cacheSizeParameter** | **Number**| Cache size parameter | [optional] [default to 500.0]
 **epsParameter** | **Number**| Eps parameter | [optional] [default to 0.001]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClassiferFullUsingGET

> RestResponse getClassiferFullUsingGET(accessKey, secretKey, id)

Get classifier full

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ClassifierApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let id = "id_example"; // String | The id of the classifier that you want the status for
apiInstance.getClassiferFullUsingGET(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **id** | **String**| The id of the classifier that you want the status for | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClassiferStatusUsingGET

> RestResponse getClassiferStatusUsingGET(accessKey, secretKey, id)

Get classifer status

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ClassifierApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let id = "id_example"; // String | The id of the classifier that you want the status for
apiInstance.getClassiferStatusUsingGET(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **id** | **String**| The id of the classifier that you want the status for | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeClassiferUsingDELETE

> RestResponse removeClassiferUsingDELETE(accessKey, secretKey, id)

Delete existing classifier

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ClassifierApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let id = "id_example"; // String | The id of the classifier that will be removed
apiInstance.removeClassiferUsingDELETE(accessKey, secretKey, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **id** | **String**| The id of the classifier that will be removed | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

