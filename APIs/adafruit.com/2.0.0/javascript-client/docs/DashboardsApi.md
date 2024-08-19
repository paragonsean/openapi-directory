# AdafruitIoRestApi.DashboardsApi

All URIs are relative to *https://io.adafruit.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allDashboards**](DashboardsApi.md#allDashboards) | **GET** /{username}/dashboards | All dashboards for current user
[**createDashboard**](DashboardsApi.md#createDashboard) | **POST** /{username}/dashboards | Create a new Dashboard
[**destroyDashboard**](DashboardsApi.md#destroyDashboard) | **DELETE** /{username}/dashboards/{id} | Delete an existing Dashboard
[**getDashboard**](DashboardsApi.md#getDashboard) | **GET** /{username}/dashboards/{id} | Returns Dashboard based on ID
[**replaceDashboard**](DashboardsApi.md#replaceDashboard) | **PUT** /{username}/dashboards/{id} | Replace an existing Dashboard
[**updateDashboard**](DashboardsApi.md#updateDashboard) | **PATCH** /{username}/dashboards/{id} | Update properties of an existing Dashboard



## allDashboards

> [Dashboard] allDashboards(username)

All dashboards for current user

The Dashboards endpoint returns information about the user&#39;s dashboards. 

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.DashboardsApi();
let username = "username_example"; // String | a valid username string
apiInstance.allDashboards(username, (error, data, response) => {
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
 **username** | **String**| a valid username string | 

### Return type

[**[Dashboard]**](Dashboard.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## createDashboard

> Dashboard createDashboard(username, dashboard)

Create a new Dashboard

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.DashboardsApi();
let username = "username_example"; // String | a valid username string
let dashboard = new AdafruitIoRestApi.CreateDashboardRequest(); // CreateDashboardRequest | 
apiInstance.createDashboard(username, dashboard, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **dashboard** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## destroyDashboard

> String destroyDashboard(username, id)

Delete an existing Dashboard

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.DashboardsApi();
let username = "username_example"; // String | a valid username string
let id = "id_example"; // String | 
apiInstance.destroyDashboard(username, id, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **id** | **String**|  | 

### Return type

**String**

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## getDashboard

> Dashboard getDashboard(username, id)

Returns Dashboard based on ID

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.DashboardsApi();
let username = "username_example"; // String | a valid username string
let id = "id_example"; // String | 
apiInstance.getDashboard(username, id, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **id** | **String**|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## replaceDashboard

> Dashboard replaceDashboard(username, id, dashboard)

Replace an existing Dashboard

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.DashboardsApi();
let username = "username_example"; // String | a valid username string
let id = "id_example"; // String | 
let dashboard = new AdafruitIoRestApi.CreateDashboardRequest(); // CreateDashboardRequest | 
apiInstance.replaceDashboard(username, id, dashboard, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **id** | **String**|  | 
 **dashboard** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv


## updateDashboard

> Dashboard updateDashboard(username, id, dashboard)

Update properties of an existing Dashboard

### Example

```javascript
import AdafruitIoRestApi from 'adafruit_io_rest_api';
let defaultClient = AdafruitIoRestApi.ApiClient.instance;
// Configure API key authorization: HeaderSignature
let HeaderSignature = defaultClient.authentications['HeaderSignature'];
HeaderSignature.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderSignature.apiKeyPrefix = 'Token';
// Configure API key authorization: QueryKey
let QueryKey = defaultClient.authentications['QueryKey'];
QueryKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryKey.apiKeyPrefix = 'Token';
// Configure API key authorization: HeaderKey
let HeaderKey = defaultClient.authentications['HeaderKey'];
HeaderKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderKey.apiKeyPrefix = 'Token';

let apiInstance = new AdafruitIoRestApi.DashboardsApi();
let username = "username_example"; // String | a valid username string
let id = "id_example"; // String | 
let dashboard = new AdafruitIoRestApi.CreateDashboardRequest(); // CreateDashboardRequest | 
apiInstance.updateDashboard(username, id, dashboard, (error, data, response) => {
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
 **username** | **String**| a valid username string | 
 **id** | **String**|  | 
 **dashboard** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | 

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[HeaderSignature](../README.md#HeaderSignature), [QueryKey](../README.md#QueryKey), [HeaderKey](../README.md#HeaderKey)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/csv

