# CustomerServiceMetricApi

All URIs are relative to *https://api.ebay.com/sell/analytics/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCustomerServiceMetric**](CustomerServiceMetricApi.md#getCustomerServiceMetric) | **GET** /customer_service_metric/{customer_service_metric_type}/{evaluation_type} |  |


<a id="getCustomerServiceMetric"></a>
# **getCustomerServiceMetric**
> GetCustomerServiceMetricResponse getCustomerServiceMetric(customerServiceMetricType, evaluationMarketplaceId, evaluationType)



Use this method to retrieve a seller&#39;s performance and rating for the customer service metric. Control the response from the getCustomerServiceMetric method using the following path and query parameters: customer_service_metric_type controls the type of customer service transactions evaluated for the metric rating. evaluation_type controls the period you want to review. evaluation_marketplace_id specifies the target marketplace for the evaluation. Currently, metric data is returned for only peer benchmarking. For more detail on the workings of peer benchmarking, see Service metrics policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerServiceMetricApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/analytics/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomerServiceMetricApi apiInstance = new CustomerServiceMetricApi(defaultClient);
    String customerServiceMetricType = "customerServiceMetricType_example"; // String | Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED
    String evaluationMarketplaceId = "evaluationMarketplaceId_example"; // String | Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/devzone/rest/api-ref/analytics/types/MarketplaceIdEnum.html
    String evaluationType = "evaluationType_example"; // String | Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period.
    try {
      GetCustomerServiceMetricResponse result = apiInstance.getCustomerServiceMetric(customerServiceMetricType, evaluationMarketplaceId, evaluationType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerServiceMetricApi#getCustomerServiceMetric");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **customerServiceMetricType** | **String**| Use this path parameter to specify the type of customer service metrics and benchmark data you want returned for the seller. Supported types are: ITEM_NOT_AS_DESCRIBED ITEM_NOT_RECEIVED | |
| **evaluationMarketplaceId** | **String**| Use this query parameter to specify the Marketplace ID to evaluate for the customer service metrics and benchmark data. For the list of supported marketplaces, see Analytics API requirements and restrictions. For implementation help, refer to eBay API documentation at https://developer.ebay.com/devzone/rest/api-ref/analytics/types/MarketplaceIdEnum.html | |
| **evaluationType** | **String**| Use this path parameter to specify the type of the seller evaluation you want returned, either: CURRENT &amp;ndash; A monthly evaluation that occurs on the 20th of every month. PROJECTED &amp;ndash; A daily evaluation that provides a projection of how the seller is currently performing with regards to the upcoming evaluation period. | |

### Return type

[**GetCustomerServiceMetricResponse**](GetCustomerServiceMetricResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Resource not found. Invalid path parameters.  |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Server Error |  -  |

