# FactsApi.OnThisDayApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factOnthisdayBornGet**](OnThisDayApi.md#factOnthisdayBornGet) | **GET** /fact/onthisday/born | 
[**factOnthisdayDiedGet**](OnThisDayApi.md#factOnthisdayDiedGet) | **GET** /fact/onthisday/died | 
[**factOnthisdayEventGet**](OnThisDayApi.md#factOnthisdayEventGet) | **GET** /fact/onthisday/event | 



## factOnthisdayBornGet

> factOnthisdayBornGet(opts)



Returns a random ( famous/ relatively famous ) person born on a given day and month

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.OnThisDayApi();
let opts = {
  'month': "month_example", // String | Optional month (1-12). Defaults to current month
  'day': "day_example" // String | Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
};
apiInstance.factOnthisdayBornGet(opts, (error, data, response) => {
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
 **month** | **String**| Optional month (1-12). Defaults to current month | [optional] 
 **day** | **String**| Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factOnthisdayDiedGet

> factOnthisdayDiedGet(opts)



Returns a random ( famous/ relatively famous ) person died on a given day and month

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.OnThisDayApi();
let opts = {
  'month': "month_example", // String | Optional month (1-12). Defaults to current month
  'day': "day_example" // String | Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
};
apiInstance.factOnthisdayDiedGet(opts, (error, data, response) => {
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
 **month** | **String**| Optional month (1-12). Defaults to current month | [optional] 
 **day** | **String**| Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factOnthisdayEventGet

> factOnthisdayEventGet(opts)



Returns a random ( famous/ relatively famous ) historic event on a given day and month

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.OnThisDayApi();
let opts = {
  'month': "month_example", // String | Optional month (1-12). Defaults to current month
  'day': "day_example" // String | Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month.
};
apiInstance.factOnthisdayEventGet(opts, (error, data, response) => {
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
 **month** | **String**| Optional month (1-12). Defaults to current month | [optional] 
 **day** | **String**| Optional day of the month (1- 28/30/31 based on the month). Defaults to current day of the month. | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

