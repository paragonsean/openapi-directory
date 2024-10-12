# TradematicCloudApi.NewsAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newsNewsGet**](NewsAPIApi.md#newsNewsGet) | **GET** /news/news | Get news list
[**newsNewsNewsidGet**](NewsAPIApi.md#newsNewsNewsidGet) | **GET** /news/news/{newsid} | Get news by ID



## newsNewsGet

> [News] newsNewsGet()

Get news list

Get news list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.NewsAPIApi();
apiInstance.newsNewsGet((error, data, response) => {
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

[**[News]**](News.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newsNewsNewsidGet

> News newsNewsNewsidGet(newsid)

Get news by ID

Get news by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.NewsAPIApi();
let newsid = 789; // Number | 
apiInstance.newsNewsNewsidGet(newsid, (error, data, response) => {
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
 **newsid** | **Number**|  | 

### Return type

[**News**](News.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

