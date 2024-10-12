# SellerServiceMetricsApi.CustomerServiceMetricApi

All URIs are relative to *https://api.ebay.com/sell/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCustomerServiceMetric**](CustomerServiceMetricApi.md#getCustomerServiceMetric) | **GET** /customer_service_metric/{customer_service_metric_type}/{evaluation_type} | 



## getCustomerServiceMetric

> GetCustomerServiceMetricResponse getCustomerServiceMetric(customerServiceMetricType, evaluationMarketplaceId, evaluationType)



Use this method to retrieve a seller&#39;s performance and rating for the customer service metric. Control the response from the getCustomerServiceMetric method using the following path and query parameters: customer_service_metric_type controls the type of customer service transactions evaluated for the metric rating. evaluation_type controls the period you want to review. evaluation_marketplace_id specifies the target marketplace for the evaluation. Currently, metric data is returned for only peer benchmarking. For more detail on the workings of peer benchmarking, see Service metrics policy.

### Example

```javascript
import SellerServiceMetricsApi from '_seller_service_metrics_api_';
let defaultClient = SellerServiceMetricsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SellerServiceMetricsApi.CustomerServiceMetricApi();
let customerServiceMetricType = "customerServiceMetricType_example"; // String | Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED
let evaluationMarketplaceId = "evaluationMarketplaceId_example"; // String | Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/devzone/rest/api-ref/analytics/types/MarketplaceIdEnum.html
let evaluationType = "evaluationType_example"; // String | Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period.
apiInstance.getCustomerServiceMetric(customerServiceMetricType, evaluationMarketplaceId, evaluationType, (error, data, response) => {
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
 **customerServiceMetricType** | **String**| Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED | 
 **evaluationMarketplaceId** | **String**| Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/devzone/rest/api-ref/analytics/types/MarketplaceIdEnum.html | 
 **evaluationType** | **String**| Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &amp;ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &amp;ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period. | 

### Return type

[**GetCustomerServiceMetricResponse**](GetCustomerServiceMetricResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

