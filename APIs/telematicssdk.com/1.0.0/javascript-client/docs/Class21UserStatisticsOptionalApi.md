# QuickStartTelematicsSdk.Class21UserStatisticsOptionalApi

All URIs are relative to *https://api.telematicssdk.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userStatisticeDailyValueV1StatisticsIndividualDaily_0**](Class21UserStatisticsOptionalApi.md#userStatisticeDailyValueV1StatisticsIndividualDaily_0) | **GET** /statistics/v1/Statistics/individual/daily/ | User statistice - Daily value - v1/Statistics/individual/daily
[**userStatisticsAccumulatedValueV1StatisticsIndividual_0**](Class21UserStatisticsOptionalApi.md#userStatisticsAccumulatedValueV1StatisticsIndividual_0) | **GET** /statistics/v1/Statistics/individual/ | User statistics - Accumulated value - /v1/Statistics/individual



## userStatisticeDailyValueV1StatisticsIndividualDaily_0

> UserStatisticeDailyValueV1StatisticsIndividualDaily200Response userStatisticeDailyValueV1StatisticsIndividualDaily_0(opts)

User statistice - Daily value - v1/Statistics/individual/daily

User statistice - Daily value - v1/Statistics/individual/daily

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class21UserStatisticsOptionalApi();
let opts = {
  'startDate': "2021-03-30", // String | 
  'endDate': "2021-03-30" // String | 
};
apiInstance.userStatisticeDailyValueV1StatisticsIndividualDaily_0(opts, (error, data, response) => {
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
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 

### Return type

[**UserStatisticeDailyValueV1StatisticsIndividualDaily200Response**](UserStatisticeDailyValueV1StatisticsIndividualDaily200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userStatisticsAccumulatedValueV1StatisticsIndividual_0

> UserStatisticsAccumulatedValueV1StatisticsIndividual200Response userStatisticsAccumulatedValueV1StatisticsIndividual_0(opts)

User statistics - Accumulated value - /v1/Statistics/individual

User statistics - Accumulated value - /v1/Statistics/individual

### Example

```javascript
import QuickStartTelematicsSdk from 'quick_start_telematics_sdk';

let apiInstance = new QuickStartTelematicsSdk.Class21UserStatisticsOptionalApi();
let opts = {
  'startDate': "2021-01-01", // String | 
  'endDate': "2021-01-30" // String | 
};
apiInstance.userStatisticsAccumulatedValueV1StatisticsIndividual_0(opts, (error, data, response) => {
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
 **startDate** | **String**|  | [optional] 
 **endDate** | **String**|  | [optional] 

### Return type

[**UserStatisticsAccumulatedValueV1StatisticsIndividual200Response**](UserStatisticsAccumulatedValueV1StatisticsIndividual200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

