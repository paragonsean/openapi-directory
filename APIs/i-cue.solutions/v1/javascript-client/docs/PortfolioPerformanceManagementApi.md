# GrowthServices.PortfolioPerformanceManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**portfolioAbcPost**](PortfolioPerformanceManagementApi.md#portfolioAbcPost) | **POST** /portfolio/abc | ABC Analysis
[**portfolioFileToPortfolioPost**](PortfolioPerformanceManagementApi.md#portfolioFileToPortfolioPost) | **POST** /portfolio/file-to-portfolio | ABCxyz Analysis
[**portfolioForecastPerformanceRewindPost**](PortfolioPerformanceManagementApi.md#portfolioForecastPerformanceRewindPost) | **POST** /portfolio/forecast-performance-rewind | Planning level rewind to calculate and measure performance potential (internal versus iCUE).
[**portfolioPost**](PortfolioPerformanceManagementApi.md#portfolioPost) | **POST** /portfolio | ABCxyz Analysis
[**portfolioXyzPost**](PortfolioPerformanceManagementApi.md#portfolioXyzPost) | **POST** /portfolio/xyz | xyz Analysis



## portfolioAbcPost

> [PortfolioAbcModel] portfolioAbcPost(opts)

ABC Analysis

Calculate and retrieve results of ABC (pareto analysis) per timeseries and planning level.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.PortfolioPerformanceManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'portfolioRequest': new GrowthServices.PortfolioRequest() // PortfolioRequest | 
};
apiInstance.portfolioAbcPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **portfolioRequest** | [**PortfolioRequest**](PortfolioRequest.md)|  | [optional] 

### Return type

[**[PortfolioAbcModel]**](PortfolioAbcModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## portfolioFileToPortfolioPost

> portfolioFileToPortfolioPost(file, opts)

ABCxyz Analysis

Calculate and retrieve results of ABC (pareto analysis) and xyz (Coefficient of variation) per timeseries and planning level. This analysis is a powerful means to estbalish a proper planning cadence, best accuracy messures and optimal hyperparameters for the organization. It provides a balanced and actionable overview of the entire product portfolio.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.PortfolioPerformanceManagementApi();
let file = "/path/to/file"; // File | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.portfolioFileToPortfolioPost(file, opts, (error, data, response) => {
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
 **file** | **File**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## portfolioForecastPerformanceRewindPost

> RewindResponse portfolioForecastPerformanceRewindPost(opts)

Planning level rewind to calculate and measure performance potential (internal versus iCUE).

Planning level rewind to calculate and measure performance potential (internal versus iCUE).

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.PortfolioPerformanceManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'forecastPerformanceRequest': new GrowthServices.ForecastPerformanceRequest() // ForecastPerformanceRequest | 
};
apiInstance.portfolioForecastPerformanceRewindPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **forecastPerformanceRequest** | [**ForecastPerformanceRequest**](ForecastPerformanceRequest.md)|  | [optional] 

### Return type

[**RewindResponse**](RewindResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## portfolioPost

> [PortfolioModel] portfolioPost(opts)

ABCxyz Analysis

Calculate and retrieve results of ABC (pareto analysis) and xyz (Coefficient of variation) per timeseries and planning level. This analysis is a powerful means to estbalish a proper planning cadence, best accuracy messures and optimal hyperparameters for the organization. It provides a balanced and actionable overview of the entire product portfolio.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.PortfolioPerformanceManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'portfolioRequest': new GrowthServices.PortfolioRequest() // PortfolioRequest | 
};
apiInstance.portfolioPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **portfolioRequest** | [**PortfolioRequest**](PortfolioRequest.md)|  | [optional] 

### Return type

[**[PortfolioModel]**](PortfolioModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## portfolioXyzPost

> [PortfolioXyzModel] portfolioXyzPost(opts)

xyz Analysis

Calculate and retrieve results of xyz (Coefficient of variation) per timeseries and planning level.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.PortfolioPerformanceManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'portfolioRequest': new GrowthServices.PortfolioRequest() // PortfolioRequest | 
};
apiInstance.portfolioXyzPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **portfolioRequest** | [**PortfolioRequest**](PortfolioRequest.md)|  | [optional] 

### Return type

[**[PortfolioXyzModel]**](PortfolioXyzModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain

