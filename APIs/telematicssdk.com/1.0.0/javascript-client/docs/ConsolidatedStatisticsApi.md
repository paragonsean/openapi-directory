# QuickStartTelematicsSdk.ConsolidatedStatisticsApi

All URIs are relative to *https://api.telematicssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1StatisticsConsolidatedDaily_0**](ConsolidatedStatisticsApi.md#v1StatisticsConsolidatedDaily_0) | **GET** /statistics/v1/Statistics/consolidated/daily | /v1/Statistics/consolidated/daily
[**v1StatisticsConsolidated_0**](ConsolidatedStatisticsApi.md#v1StatisticsConsolidated_0) | **GET** /statistics/v1/Statistics/consolidated | /v1/Statistics/consolidated



## v1StatisticsConsolidatedDaily_0

> v1StatisticsConsolidatedDaily_0(opts)

/v1/Statistics/consolidated/daily

/v1/Statistics/consolidated/daily

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.ConsolidatedStatisticsApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-17", // String | 
  'endDate': "2021-01-18", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1StatisticsConsolidatedDaily_0(opts, (error, data, response) => {
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
 **deviceToken** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **instanceId** | **String**|  | [optional] 
 **appId** | **String**|  | [optional] 
 **companyId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## v1StatisticsConsolidated_0

> v1StatisticsConsolidated_0(opts)

/v1/Statistics/consolidated

/v1/Statistics/consolidated

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.ConsolidatedStatisticsApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-18", // String | 
  'endDate': "2021-03-18", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1StatisticsConsolidated_0(opts, (error, data, response) => {
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
 **deviceToken** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **instanceId** | **String**|  | [optional] 
 **appId** | **String**|  | [optional] 
 **companyId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

