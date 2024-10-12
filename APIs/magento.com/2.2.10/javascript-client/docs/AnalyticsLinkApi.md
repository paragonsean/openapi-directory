# MagentoB2B.AnalyticsLinkApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyticsLinkProviderV1GetGet**](AnalyticsLinkApi.md#analyticsLinkProviderV1GetGet) | **GET** /V1/analytics/link | analytics/link



## analyticsLinkProviderV1GetGet

> AnalyticsDataLinkInterface analyticsLinkProviderV1GetGet()

analytics/link



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AnalyticsLinkApi();
apiInstance.analyticsLinkProviderV1GetGet((error, data, response) => {
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

[**AnalyticsDataLinkInterface**](AnalyticsDataLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

