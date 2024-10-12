# InfluxOssApiService.SetupApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSetup**](SetupApi.md#getSetup) | **GET** /setup | Check if database has default user, org, bucket
[**postSetup**](SetupApi.md#postSetup) | **POST** /setup | Set up initial user, org and bucket



## getSetup

> IsOnboarding getSetup(opts)

Check if database has default user, org, bucket

Returns &#x60;true&#x60; if no default user, organization, or bucket has been created.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SetupApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getSetup(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**IsOnboarding**](IsOnboarding.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postSetup

> OnboardingResponse postSetup(onboardingRequest, opts)

Set up initial user, org and bucket

Post an onboarding request to set up initial user, org and bucket.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SetupApi();
let onboardingRequest = new InfluxOssApiService.OnboardingRequest(); // OnboardingRequest | Source to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postSetup(onboardingRequest, opts, (error, data, response) => {
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
 **onboardingRequest** | [**OnboardingRequest**](OnboardingRequest.md)| Source to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**OnboardingResponse**](OnboardingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

