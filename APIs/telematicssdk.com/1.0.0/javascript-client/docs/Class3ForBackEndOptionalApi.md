# QuickStartTelematicsSdk.Class3ForBackEndOptionalApi

All URIs are relative to *https://api.telematicssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1ScoringsConsolidated**](Class3ForBackEndOptionalApi.md#v1ScoringsConsolidated) | **GET** /statistics/v1/Scorings/consolidated | /v1/Scorings/consolidated
[**v1ScoringsConsolidatedDaily**](Class3ForBackEndOptionalApi.md#v1ScoringsConsolidatedDaily) | **GET** /statistics/v1/Scorings/consolidated/daily | /v1/Scorings/consolidated/daily
[**v1StatisticsConsolidated**](Class3ForBackEndOptionalApi.md#v1StatisticsConsolidated) | **GET** /statistics/v1/Statistics/consolidated | /v1/Statistics/consolidated
[**v1StatisticsConsolidatedDaily**](Class3ForBackEndOptionalApi.md#v1StatisticsConsolidatedDaily) | **GET** /statistics/v1/Statistics/consolidated/daily | /v1/Statistics/consolidated/daily



## v1ScoringsConsolidated

> v1ScoringsConsolidated(opts)

/v1/Scorings/consolidated

/v1/Scorings/consolidated

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class3ForBackEndOptionalApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-17T01:04:22.840Z", // String | 
  'endDate': "2021-01-18T01:04:22.840Z", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1ScoringsConsolidated(opts, (error, data, response) => {
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


## v1ScoringsConsolidatedDaily

> V1ScoringsConsolidatedDaily200Response v1ScoringsConsolidatedDaily(opts)

/v1/Scorings/consolidated/daily

/v1/Scorings/consolidated/daily

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class3ForBackEndOptionalApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-17T01:04:22.840Z", // String | 
  'endDate': "2021-01-18T01:04:22.840Z", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1ScoringsConsolidatedDaily(opts, (error, data, response) => {
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
 **deviceToken** | **String**|  | [optional] 
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **instanceId** | **String**|  | [optional] 
 **appId** | **String**|  | [optional] 
 **companyId** | **String**|  | [optional] 

### Return type

[**V1ScoringsConsolidatedDaily200Response**](V1ScoringsConsolidatedDaily200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## v1StatisticsConsolidated

> v1StatisticsConsolidated(opts)

/v1/Statistics/consolidated

/v1/Statistics/consolidated

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class3ForBackEndOptionalApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-18", // String | 
  'endDate': "2021-03-18", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1StatisticsConsolidated(opts, (error, data, response) => {
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


## v1StatisticsConsolidatedDaily

> v1StatisticsConsolidatedDaily(opts)

/v1/Statistics/consolidated/daily

/v1/Statistics/consolidated/daily

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class3ForBackEndOptionalApi();
let opts = {
  'deviceToken': "", // String | 
  'startDate': "2021-01-17", // String | 
  'endDate': "2021-01-18", // String | 
  'tag': "", // String | 
  'instanceId': "", // String | 
  'appId': "", // String | 
  'companyId': "" // String | 
};
apiInstance.v1StatisticsConsolidatedDaily(opts, (error, data, response) => {
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

