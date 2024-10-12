# QnAMakerClient.KnowledgebasesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**knowledgebaseCreate**](KnowledgebasesApi.md#knowledgebaseCreate) | **POST** /knowledgebases/create | Asynchronous operation to create a new knowledgebase.
[**knowledgebaseDelete**](KnowledgebasesApi.md#knowledgebaseDelete) | **DELETE** /knowledgebases/{kbId} | Deletes the knowledgebase and all its data.
[**knowledgebaseDownload**](KnowledgebasesApi.md#knowledgebaseDownload) | **GET** /knowledgebases/{kbId}/{environment}/qna | Download the knowledgebase.
[**knowledgebaseGetDetails**](KnowledgebasesApi.md#knowledgebaseGetDetails) | **GET** /knowledgebases/{kbId} | Gets details of a specific knowledgebase.
[**knowledgebaseListAll**](KnowledgebasesApi.md#knowledgebaseListAll) | **GET** /knowledgebases | Gets all knowledgebases for a user.
[**knowledgebasePublish**](KnowledgebasesApi.md#knowledgebasePublish) | **POST** /knowledgebases/{kbId} | Publishes all changes in test index of a knowledgebase to its prod index.
[**knowledgebaseReplace**](KnowledgebasesApi.md#knowledgebaseReplace) | **PUT** /knowledgebases/{kbId} | Replace knowledgebase contents.
[**knowledgebaseUpdate**](KnowledgebasesApi.md#knowledgebaseUpdate) | **PATCH** /knowledgebases/{kbId} | Asynchronous operation to modify a knowledgebase.



## knowledgebaseCreate

> Operation knowledgebaseCreate(createKbPayload)

Asynchronous operation to create a new knowledgebase.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let createKbPayload = new QnAMakerClient.CreateKbDTO(); // CreateKbDTO | Post body of the request.
apiInstance.knowledgebaseCreate(createKbPayload, (error, data, response) => {
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
 **createKbPayload** | [**CreateKbDTO**](CreateKbDTO.md)| Post body of the request. | 

### Return type

[**Operation**](Operation.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## knowledgebaseDelete

> knowledgebaseDelete(kbId)

Deletes the knowledgebase and all its data.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
apiInstance.knowledgebaseDelete(kbId, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## knowledgebaseDownload

> QnADocumentsDTO knowledgebaseDownload(kbId, environment)

Download the knowledgebase.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
let environment = "environment_example"; // String | Specifies whether environment is Test or Prod.
apiInstance.knowledgebaseDownload(kbId, environment, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 
 **environment** | **String**| Specifies whether environment is Test or Prod. | 

### Return type

[**QnADocumentsDTO**](QnADocumentsDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## knowledgebaseGetDetails

> KnowledgebaseDTO knowledgebaseGetDetails(kbId)

Gets details of a specific knowledgebase.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
apiInstance.knowledgebaseGetDetails(kbId, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 

### Return type

[**KnowledgebaseDTO**](KnowledgebaseDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## knowledgebaseListAll

> KnowledgebasesDTO knowledgebaseListAll()

Gets all knowledgebases for a user.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
apiInstance.knowledgebaseListAll((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**KnowledgebasesDTO**](KnowledgebasesDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## knowledgebasePublish

> knowledgebasePublish(kbId)

Publishes all changes in test index of a knowledgebase to its prod index.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
apiInstance.knowledgebasePublish(kbId, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## knowledgebaseReplace

> knowledgebaseReplace(kbId, replaceKb)

Replace knowledgebase contents.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
let replaceKb = new QnAMakerClient.ReplaceKbDTO(); // ReplaceKbDTO | An instance of ReplaceKbDTO which contains list of qnas to be uploaded
apiInstance.knowledgebaseReplace(kbId, replaceKb, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 
 **replaceKb** | [**ReplaceKbDTO**](ReplaceKbDTO.md)| An instance of ReplaceKbDTO which contains list of qnas to be uploaded | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## knowledgebaseUpdate

> Operation knowledgebaseUpdate(kbId, updateKb)

Asynchronous operation to modify a knowledgebase.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.KnowledgebasesApi();
let kbId = "kbId_example"; // String | Knowledgebase id.
let updateKb = new QnAMakerClient.UpdateKbOperationDTO(); // UpdateKbOperationDTO | Post body of the request.
apiInstance.knowledgebaseUpdate(kbId, updateKb, (error, data, response) => {
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
 **kbId** | **String**| Knowledgebase id. | 
 **updateKb** | [**UpdateKbOperationDTO**](UpdateKbOperationDTO.md)| Post body of the request. | 

### Return type

[**Operation**](Operation.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

