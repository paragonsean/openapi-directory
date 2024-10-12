# VectaraRestApi.AdminServiceApi

All URIs are relative to *https://api.vectara.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCorpus**](AdminServiceApi.md#createCorpus) | **POST** /v1/create-corpus | 
[**deleteCorpus**](AdminServiceApi.md#deleteCorpus) | **POST** /v1/delete-corpus | 
[**listCorpora**](AdminServiceApi.md#listCorpora) | **POST** /v1/list-corpora | 
[**resetCorpus**](AdminServiceApi.md#resetCorpus) | **POST** /v1/reset-corpus | 



## createCorpus

> AdminCreateCorpusResponse createCorpus(customerId, adminCreateCorpusRequest)



Create Corpus

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.AdminServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let adminCreateCorpusRequest = new VectaraRestApi.AdminCreateCorpusRequest(); // AdminCreateCorpusRequest | 
apiInstance.createCorpus(customerId, adminCreateCorpusRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **adminCreateCorpusRequest** | [**AdminCreateCorpusRequest**](AdminCreateCorpusRequest.md)|  | 

### Return type

[**AdminCreateCorpusResponse**](AdminCreateCorpusResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCorpus

> AdminDeleteCorpusResponse deleteCorpus(customerId, adminDeleteCorpusRequest)



Delete Corpus

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.AdminServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let adminDeleteCorpusRequest = new VectaraRestApi.AdminDeleteCorpusRequest(); // AdminDeleteCorpusRequest | 
apiInstance.deleteCorpus(customerId, adminDeleteCorpusRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **adminDeleteCorpusRequest** | [**AdminDeleteCorpusRequest**](AdminDeleteCorpusRequest.md)|  | 

### Return type

[**AdminDeleteCorpusResponse**](AdminDeleteCorpusResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCorpora

> AdminListCorporaResponse listCorpora(customerId, adminListCorporaRequest)



List Corpora

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.AdminServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let adminListCorporaRequest = new VectaraRestApi.AdminListCorporaRequest(); // AdminListCorporaRequest | 
apiInstance.listCorpora(customerId, adminListCorporaRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **adminListCorporaRequest** | [**AdminListCorporaRequest**](AdminListCorporaRequest.md)|  | 

### Return type

[**AdminListCorporaResponse**](AdminListCorporaResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetCorpus

> AdminResetCorpusResponse resetCorpus(customerId, adminResetCorpusRequest)



Reset Corpus

### Example

```javascript
import VectaraRestApi from 'vectara_rest_api';
let defaultClient = VectaraRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oAuth
let oAuth = defaultClient.authentications['oAuth'];
oAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VectaraRestApi.AdminServiceApi();
let customerId = 56; // Number | The Customer ID to use for the request.
let adminResetCorpusRequest = new VectaraRestApi.AdminResetCorpusRequest(); // AdminResetCorpusRequest | 
apiInstance.resetCorpus(customerId, adminResetCorpusRequest, (error, data, response) => {
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
 **customerId** | **Number**| The Customer ID to use for the request. | 
 **adminResetCorpusRequest** | [**AdminResetCorpusRequest**](AdminResetCorpusRequest.md)|  | 

### Return type

[**AdminResetCorpusResponse**](AdminResetCorpusResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

