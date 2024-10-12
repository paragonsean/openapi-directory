# GrowthServices.ReportingAndMonitoringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportPerformancePlanningLevelIdGet**](ReportingAndMonitoringApi.md#reportPerformancePlanningLevelIdGet) | **GET** /report/performance/{planningLevelId} | Month over month performance per planning level
[**reportPerformanceSkuRationalizationPlanningLevelIdGet**](ReportingAndMonitoringApi.md#reportPerformanceSkuRationalizationPlanningLevelIdGet) | **GET** /report/performance/sku-rationalization/{planningLevelId} | SKU rationalization report
[**reportPlanningLevelOrganizationGet**](ReportingAndMonitoringApi.md#reportPlanningLevelOrganizationGet) | **GET** /report/planning-level/organization | Get list of plannign levels by organization
[**reportPlanningLevelUserGet**](ReportingAndMonitoringApi.md#reportPlanningLevelUserGet) | **GET** /report/planning-level/user | Get list of plannign levels by user
[**reportUserGet**](ReportingAndMonitoringApi.md#reportUserGet) | **GET** /report/user | Get usage statistics per user



## reportPerformancePlanningLevelIdGet

> reportPerformancePlanningLevelIdGet(planningLevelId, opts)

Month over month performance per planning level

Month over month performance per planning level

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ReportingAndMonitoringApi();
let planningLevelId = "planningLevelId_example"; // String | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.reportPerformancePlanningLevelIdGet(planningLevelId, opts, (error, data, response) => {
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
 **planningLevelId** | **String**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reportPerformanceSkuRationalizationPlanningLevelIdGet

> [PortfolioModel] reportPerformanceSkuRationalizationPlanningLevelIdGet(planningLevelId, opts)

SKU rationalization report

SKU rationalization report

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ReportingAndMonitoringApi();
let planningLevelId = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.reportPerformanceSkuRationalizationPlanningLevelIdGet(planningLevelId, opts, (error, data, response) => {
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
 **planningLevelId** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

[**[PortfolioModel]**](PortfolioModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## reportPlanningLevelOrganizationGet

> reportPlanningLevelOrganizationGet(opts)

Get list of plannign levels by organization

Get list of plannign levels by organization

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ReportingAndMonitoringApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.reportPlanningLevelOrganizationGet(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reportPlanningLevelUserGet

> reportPlanningLevelUserGet(opts)

Get list of plannign levels by user

Get list of plannign levels by user

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ReportingAndMonitoringApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.reportPlanningLevelUserGet(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reportUserGet

> reportUserGet(opts)

Get usage statistics per user

Get usage statistics per user

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ReportingAndMonitoringApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.reportUserGet(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

