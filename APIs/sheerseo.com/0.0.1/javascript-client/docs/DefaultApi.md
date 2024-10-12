# SheerSeoApi.DefaultApi

All URIs are relative to *https://www.sheerseo.com/seo/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rankCollect**](DefaultApi.md#rankCollect) | **POST** /rank-collect | 
[**rankSubmit**](DefaultApi.md#rankSubmit) | **POST** /rank-submit | 
[**serpCollect**](DefaultApi.md#serpCollect) | **POST** /serp-collect | 
[**serpSubmit**](DefaultApi.md#serpSubmit) | **POST** /serp-submit | 



## rankCollect

> RankCollectResponse rankCollect(body)



Submit serp jobs

### Example

```javascript
import SheerSeoApi from 'sheer_seo_api';
let defaultClient = SheerSeoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SheerSeoApi.DefaultApi();
let body = new SheerSeoApi.CollectRequest(); // CollectRequest | The body of the reqest to collect SERPs
apiInstance.rankCollect(body, (error, data, response) => {
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
 **body** | [**CollectRequest**](CollectRequest.md)| The body of the reqest to collect SERPs | 

### Return type

[**RankCollectResponse**](RankCollectResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8


## rankSubmit

> RankSubmitResponse rankSubmit(body)



Submit rank jobs

### Example

```javascript
import SheerSeoApi from 'sheer_seo_api';
let defaultClient = SheerSeoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SheerSeoApi.DefaultApi();
let body = new SheerSeoApi.RankSubmitRequest(); // RankSubmitRequest | The body of the reqest to submit SERPs
apiInstance.rankSubmit(body, (error, data, response) => {
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
 **body** | [**RankSubmitRequest**](RankSubmitRequest.md)| The body of the reqest to submit SERPs | 

### Return type

[**RankSubmitResponse**](RankSubmitResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8


## serpCollect

> SerpCollectResponse serpCollect(body)



Submit serp jobs

### Example

```javascript
import SheerSeoApi from 'sheer_seo_api';
let defaultClient = SheerSeoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SheerSeoApi.DefaultApi();
let body = new SheerSeoApi.CollectRequest(); // CollectRequest | The body of the reqest to collect SERPs
apiInstance.serpCollect(body, (error, data, response) => {
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
 **body** | [**CollectRequest**](CollectRequest.md)| The body of the reqest to collect SERPs | 

### Return type

[**SerpCollectResponse**](SerpCollectResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8


## serpSubmit

> SerpSubmitResponse serpSubmit(body)



Submit serp jobs

### Example

```javascript
import SheerSeoApi from 'sheer_seo_api';
let defaultClient = SheerSeoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SheerSeoApi.DefaultApi();
let body = new SheerSeoApi.SerpSubmitRequest(); // SerpSubmitRequest | The body of the reqest to submit SERPs
apiInstance.serpSubmit(body, (error, data, response) => {
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
 **body** | [**SerpSubmitRequest**](SerpSubmitRequest.md)| The body of the reqest to submit SERPs | 

### Return type

[**SerpSubmitResponse**](SerpSubmitResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8

