# RewardApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createReward**](RewardApi.md#createReward) | **POST** /reward | Create a reward |
| [**fetchReward**](RewardApi.md#fetchReward) | **GET** /reward/{id} | Get a reward |
| [**fetchRewards**](RewardApi.md#fetchRewards) | **GET** /reward | List rewards |


<a id="createReward"></a>
# **createReward**
> CreateRewardResponse createReward(createRewardRequest)

Create a reward

Create a reward for a patient.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardApi apiInstance = new RewardApi(defaultClient);
    CreateRewardRequest createRewardRequest = new CreateRewardRequest(); // CreateRewardRequest | 
    try {
      CreateRewardResponse result = apiInstance.createReward(createRewardRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardApi#createReward");
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
| **createRewardRequest** | [**CreateRewardRequest**](CreateRewardRequest.md)|  | |

### Return type

[**CreateRewardResponse**](CreateRewardResponse.md)

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

<a id="fetchReward"></a>
# **fetchReward**
> FetchRewardResponse fetchReward(id)

Get a reward

Get a reward record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardApi apiInstance = new RewardApi(defaultClient);
    String id = "id_example"; // String | Reward identifier
    try {
      FetchRewardResponse result = apiInstance.fetchReward(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardApi#fetchReward");
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
| **id** | **String**| Reward identifier | |

### Return type

[**FetchRewardResponse**](FetchRewardResponse.md)

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

<a id="fetchRewards"></a>
# **fetchRewards**
> FetchRewardsResponse fetchRewards(filterPatient, filterRewardProgramActivation, filterThread, filterGroups, filterOrganization)

List rewards

Get a list of rewards matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardApi apiInstance = new RewardApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient identifier. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterRewardProgramActivation = "filterRewardProgramActivation_example"; // String | Reward program activation identifier
    String filterThread = "filterThread_example"; // String | Thread identifier
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    try {
      FetchRewardsResponse result = apiInstance.fetchRewards(filterPatient, filterRewardProgramActivation, filterThread, filterGroups, filterOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardApi#fetchRewards");
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
| **filterPatient** | **String**| Patient identifier. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterRewardProgramActivation** | **String**| Reward program activation identifier | [optional] |
| **filterThread** | **String**| Thread identifier | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |

### Return type

[**FetchRewardsResponse**](FetchRewardsResponse.md)

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

