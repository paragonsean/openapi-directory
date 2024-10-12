# RewardEarningApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRewardEarning**](RewardEarningApi.md#createRewardEarning) | **POST** /reward_earning | Create a reward earning |
| [**fetchRewardEarning**](RewardEarningApi.md#fetchRewardEarning) | **GET** /reward_earning/{id} | Get a reward earning |
| [**fetchRewardEarnings**](RewardEarningApi.md#fetchRewardEarnings) | **GET** /reward_earning | List reward earnings |


<a id="createRewardEarning"></a>
# **createRewardEarning**
> CreateRewardEarningResponse createRewardEarning(createRewardEarningRequest)

Create a reward earning

Create a reward earning for a reward. There can only be one earning for a reward. It is possilble to create multiple reward earnings simultaneously by providing and array of reward earnings in the data property.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardEarningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardEarningApi apiInstance = new RewardEarningApi(defaultClient);
    CreateRewardEarningRequest createRewardEarningRequest = new CreateRewardEarningRequest(); // CreateRewardEarningRequest | 
    try {
      CreateRewardEarningResponse result = apiInstance.createRewardEarning(createRewardEarningRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardEarningApi#createRewardEarning");
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
| **createRewardEarningRequest** | [**CreateRewardEarningRequest**](CreateRewardEarningRequest.md)|  | |

### Return type

[**CreateRewardEarningResponse**](CreateRewardEarningResponse.md)

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

<a id="fetchRewardEarning"></a>
# **fetchRewardEarning**
> FetchRewardEarningResponse fetchRewardEarning(id)

Get a reward earning

Get a reward earning record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardEarningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardEarningApi apiInstance = new RewardEarningApi(defaultClient);
    String id = "id_example"; // String | Reward earning identifier
    try {
      FetchRewardEarningResponse result = apiInstance.fetchRewardEarning(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardEarningApi#fetchRewardEarning");
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
| **id** | **String**| Reward earning identifier | |

### Return type

[**FetchRewardEarningResponse**](FetchRewardEarningResponse.md)

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

<a id="fetchRewardEarnings"></a>
# **fetchRewardEarnings**
> FetchRewardEarningsResponse fetchRewardEarnings(filterGroups, filterPatient, filterReadyForFulfillment)

List reward earnings

Get a list of reward earnings matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardEarningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardEarningApi apiInstance = new RewardEarningApi(defaultClient);
    String filterGroups = "filterGroups_example"; // String | Group identifiers
    String filterPatient = "filterPatient_example"; // String | Patient identifier
    Boolean filterReadyForFulfillment = true; // Boolean | If true, only returns those reward earnings for which ready_for_fulfillment is true and fulfilled_at is null. If false, only returns those reward earnings for which ready_for_fulfillment is false and fulfilled_at is null.
    try {
      FetchRewardEarningsResponse result = apiInstance.fetchRewardEarnings(filterGroups, filterPatient, filterReadyForFulfillment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardEarningApi#fetchRewardEarnings");
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
| **filterGroups** | **String**| Group identifiers | |
| **filterPatient** | **String**| Patient identifier | |
| **filterReadyForFulfillment** | **Boolean**| If true, only returns those reward earnings for which ready_for_fulfillment is true and fulfilled_at is null. If false, only returns those reward earnings for which ready_for_fulfillment is false and fulfilled_at is null. | [optional] |

### Return type

[**FetchRewardEarningsResponse**](FetchRewardEarningsResponse.md)

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

