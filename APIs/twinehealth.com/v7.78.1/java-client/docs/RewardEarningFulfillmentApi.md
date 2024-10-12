# RewardEarningFulfillmentApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRewardEarningFulfillment**](RewardEarningFulfillmentApi.md#createRewardEarningFulfillment) | **POST** /reward_earning_fulfillment | Create a reward earning fulfillment |
| [**fetchRewardEarningFulfillment**](RewardEarningFulfillmentApi.md#fetchRewardEarningFulfillment) | **GET** /reward_earning_fulfillment/{id} | Get a reward earning fulfillment |
| [**fetchRewardEarningFulfillments**](RewardEarningFulfillmentApi.md#fetchRewardEarningFulfillments) | **GET** /reward_earning_fulfillment | List reward earning fulfillments |


<a id="createRewardEarningFulfillment"></a>
# **createRewardEarningFulfillment**
> CreateRewardEarningFulfillmentResponse createRewardEarningFulfillment(createRewardEarningFulfillmentRequest)

Create a reward earning fulfillment

Create a reward earning fulfillment for a reward earning. There can only be one fulfillment for each earning.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardEarningFulfillmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardEarningFulfillmentApi apiInstance = new RewardEarningFulfillmentApi(defaultClient);
    CreateRewardEarningFulfillmentRequest createRewardEarningFulfillmentRequest = new CreateRewardEarningFulfillmentRequest(); // CreateRewardEarningFulfillmentRequest | 
    try {
      CreateRewardEarningFulfillmentResponse result = apiInstance.createRewardEarningFulfillment(createRewardEarningFulfillmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardEarningFulfillmentApi#createRewardEarningFulfillment");
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
| **createRewardEarningFulfillmentRequest** | [**CreateRewardEarningFulfillmentRequest**](CreateRewardEarningFulfillmentRequest.md)|  | |

### Return type

[**CreateRewardEarningFulfillmentResponse**](CreateRewardEarningFulfillmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchRewardEarningFulfillment"></a>
# **fetchRewardEarningFulfillment**
> FetchRewardEarningFulfillmentResponse fetchRewardEarningFulfillment(id)

Get a reward earning fulfillment

Get a reward earning fulfillment record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardEarningFulfillmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardEarningFulfillmentApi apiInstance = new RewardEarningFulfillmentApi(defaultClient);
    String id = "id_example"; // String | Reward earning fulfillment identifier
    try {
      FetchRewardEarningFulfillmentResponse result = apiInstance.fetchRewardEarningFulfillment(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardEarningFulfillmentApi#fetchRewardEarningFulfillment");
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
| **id** | **String**| Reward earning fulfillment identifier | |

### Return type

[**FetchRewardEarningFulfillmentResponse**](FetchRewardEarningFulfillmentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchRewardEarningFulfillments"></a>
# **fetchRewardEarningFulfillments**
> FetchRewardEarningFulfillmentsResponse fetchRewardEarningFulfillments(filterPatient)

List reward earning fulfillments

Get a list of reward earning fulfillments matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardEarningFulfillmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardEarningFulfillmentApi apiInstance = new RewardEarningFulfillmentApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient identifier
    try {
      FetchRewardEarningFulfillmentsResponse result = apiInstance.fetchRewardEarningFulfillments(filterPatient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardEarningFulfillmentApi#fetchRewardEarningFulfillments");
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
| **filterPatient** | **String**| Patient identifier | |

### Return type

[**FetchRewardEarningFulfillmentsResponse**](FetchRewardEarningFulfillmentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

