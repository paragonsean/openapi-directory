# GrowthServices.InsightDrivenPlanningForecastOptimizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastAIHistoryAndForecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastAIHistoryAndForecastPost) | **POST** /forecast/AI/history-and-forecast | History and forecast utilizing advanced machine learning models
[**forecastAIPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastAIPost) | **POST** /forecast/AI | Forecast utilizing advanced machine learning models
[**forecastFileToForecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastFileToForecastPost) | **POST** /forecast/file-to-forecast | Forecast from file
[**forecastForecastBottomUpPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastForecastBottomUpPost) | **POST** /forecast/forecast-bottom-up | Bottom up forecasting
[**forecastForecastTopDownPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastForecastTopDownPost) | **POST** /forecast/forecast-top-down | Top down forecasting
[**forecastFullDetailPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastFullDetailPost) | **POST** /forecast/full-detail | Full forecast result details, including error, trend seasonality and outlier
[**forecastHistoryAndForecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastHistoryAndForecastPost) | **POST** /forecast/history-and-forecast | History and forecast for fast timeseries view
[**forecastOptimalParameterPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastOptimalParameterPost) | **POST** /forecast/optimal-parameter | Get optimal parameter per method
[**forecastPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastPost) | **POST** /forecast | Forecasts only, for faster results
[**forecastRerunPost**](InsightDrivenPlanningForecastOptimizationApi.md#forecastRerunPost) | **POST** /forecast/rerun | Rerun previously uploaded planning level
[**forecastResultJobIdGet**](InsightDrivenPlanningForecastOptimizationApi.md#forecastResultJobIdGet) | **GET** /forecast/result/{jobId} | Forecast result
[**forecastStatusJobIdGet**](InsightDrivenPlanningForecastOptimizationApi.md#forecastStatusJobIdGet) | **GET** /forecast/status/{jobId} | Forecast status
[**outlierPost**](InsightDrivenPlanningForecastOptimizationApi.md#outlierPost) | **POST** /outlier | Get outlier



## forecastAIHistoryAndForecastPost

> JobResponse forecastAIHistoryAndForecastPost(opts)

History and forecast utilizing advanced machine learning models

History and forecast utilizing advanced machine learning models. Please be mindful of enhanced execution times (~1-2s per timeseries).

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'aiPlanningLevelRequest': new GrowthServices.AiPlanningLevelRequest() // AiPlanningLevelRequest | 
};
apiInstance.forecastAIHistoryAndForecastPost(opts, (error, data, response) => {
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
 **aiPlanningLevelRequest** | [**AiPlanningLevelRequest**](AiPlanningLevelRequest.md)|  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastAIPost

> JobResponse forecastAIPost(opts)

Forecast utilizing advanced machine learning models

Forecast AI is utilizing advanced machine learning models. Please be mindful of enhanced execution times (~1-2s per timeseries).

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'aiPlanningLevelRequest': new GrowthServices.AiPlanningLevelRequest() // AiPlanningLevelRequest | 
};
apiInstance.forecastAIPost(opts, (error, data, response) => {
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
 **aiPlanningLevelRequest** | [**AiPlanningLevelRequest**](AiPlanningLevelRequest.md)|  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastFileToForecastPost

> JobResponse forecastFileToForecastPost(file, method, opts)

Forecast from file

Forecast from file allows for quick analysis via Microsoft Excel and CSV file format. Please check documentation link for help.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let file = "/path/to/file"; // File | 
let method = "method_example"; // String | 
let opts = {
  'token': "token_example", // String | User Authentication Token
  'discardData': true, // Boolean | 
  'errorType': "errorType_example", // String | 
  'holdOutPeriod': 56, // Number | 
  'noFcst': 56, // Number | 
  'outlierDetection': true, // Boolean | 
  'periodicity': 56 // Number | 
};
apiInstance.forecastFileToForecastPost(file, method, opts, (error, data, response) => {
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
 **file** | **File**|  | 
 **method** | **String**|  | 
 **token** | **String**| User Authentication Token | [optional] 
 **discardData** | **Boolean**|  | [optional] 
 **errorType** | **String**|  | [optional] 
 **holdOutPeriod** | **Number**|  | [optional] 
 **noFcst** | **Number**|  | [optional] 
 **outlierDetection** | **Boolean**|  | [optional] 
 **periodicity** | **Number**|  | [optional] 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, text/json, text/plain


## forecastForecastBottomUpPost

> ForecastBottomUpResponse forecastForecastBottomUpPost(opts)

Bottom up forecasting

Calculate forecast by timeseries and sum results up to establish forecast for top level timeseries.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelRequest': new GrowthServices.PlanningLevelRequest() // PlanningLevelRequest | 
};
apiInstance.forecastForecastBottomUpPost(opts, (error, data, response) => {
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
 **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] 

### Return type

[**ForecastBottomUpResponse**](ForecastBottomUpResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastForecastTopDownPost

> forecastForecastTopDownPost(opts)

Top down forecasting

Calculate forecast based on sum of of lower level timeseries and distribute forecast down based on ratios. Great feature for planning levels with dynamic timeseries.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelRequest': new GrowthServices.PlanningLevelRequest() // PlanningLevelRequest | 
};
apiInstance.forecastForecastTopDownPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## forecastFullDetailPost

> FullDetailsForecastResponse forecastFullDetailPost(opts)

Full forecast result details, including error, trend seasonality and outlier

Response provides full forecast result details, including error, trend seasonality and outlier. Great for advanced analysis.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelRequest': new GrowthServices.PlanningLevelRequest() // PlanningLevelRequest | 
};
apiInstance.forecastFullDetailPost(opts, (error, data, response) => {
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
 **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] 

### Return type

[**FullDetailsForecastResponse**](FullDetailsForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastHistoryAndForecastPost

> HistoryAndForecastResponse forecastHistoryAndForecastPost(opts)

History and forecast for fast timeseries view

Reponse provides history and forecast per timeseries. Great for visualizing results.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelRequest': new GrowthServices.PlanningLevelRequest() // PlanningLevelRequest | 
};
apiInstance.forecastHistoryAndForecastPost(opts, (error, data, response) => {
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
 **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] 

### Return type

[**HistoryAndForecastResponse**](HistoryAndForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastOptimalParameterPost

> OptimalParameterResponse forecastOptimalParameterPost(opts)

Get optimal parameter per method

Use the optimal parameter sets created by iCUE to set the method parameters of your internal planning system.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelRequest': new GrowthServices.PlanningLevelRequest() // PlanningLevelRequest | 
};
apiInstance.forecastOptimalParameterPost(opts, (error, data, response) => {
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
 **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] 

### Return type

[**OptimalParameterResponse**](OptimalParameterResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastPost

> ForecastResponse forecastPost(opts)

Forecasts only, for faster results

To support maximum operation and integration speed, this endpoint only returns the calculated forecast.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelRequest': new GrowthServices.PlanningLevelRequest() // PlanningLevelRequest | 
};
apiInstance.forecastPost(opts, (error, data, response) => {
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
 **planningLevelRequest** | [**PlanningLevelRequest**](PlanningLevelRequest.md)|  | [optional] 

### Return type

[**ForecastResponse**](ForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastRerunPost

> ForecastResponse forecastRerunPost(opts)

Rerun previously uploaded planning level

Rerun previously uploaded planning level.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'planningLevelReRunRequest': new GrowthServices.PlanningLevelReRunRequest() // PlanningLevelReRunRequest | 
};
apiInstance.forecastRerunPost(opts, (error, data, response) => {
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
 **planningLevelReRunRequest** | [**PlanningLevelReRunRequest**](PlanningLevelReRunRequest.md)|  | [optional] 

### Return type

[**ForecastResponse**](ForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## forecastResultJobIdGet

> forecastResultJobIdGet(jobId, opts)

Forecast result

Get result for forecast job

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let jobId = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.forecastResultJobIdGet(jobId, opts, (error, data, response) => {
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
 **jobId** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## forecastStatusJobIdGet

> forecastStatusJobIdGet(jobId, opts)

Forecast status

Get status for forecast job

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let jobId = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.forecastStatusJobIdGet(jobId, opts, (error, data, response) => {
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
 **jobId** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## outlierPost

> [TimeSeriesOutliersResponse] outlierPost(opts)

Get outlier

Identify outliers (single and repetitive spikes, seasonality, masked outliers, trend and level jumps, amongst other topics) and use for cleansing of the history stream prior to forecast claculation. Depending on math model used, this approach often improves results dramatically, as it removes disturbances.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.InsightDrivenPlanningForecastOptimizationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'outliersRequest': new GrowthServices.OutliersRequest() // OutliersRequest | 
};
apiInstance.outlierPost(opts, (error, data, response) => {
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
 **outliersRequest** | [**OutliersRequest**](OutliersRequest.md)|  | [optional] 

### Return type

[**[TimeSeriesOutliersResponse]**](TimeSeriesOutliersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain

