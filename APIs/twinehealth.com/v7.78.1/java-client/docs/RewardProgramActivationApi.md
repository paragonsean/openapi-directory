# RewardProgramActivationApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRewardProgramActivation**](RewardProgramActivationApi.md#createRewardProgramActivation) | **POST** /reward_program_activation | Create a reward program activation |
| [**fetchRewardProgramActivation**](RewardProgramActivationApi.md#fetchRewardProgramActivation) | **GET** /reward_program_activation/{id} | Get a reward program activation |
| [**fetchRewardProgramActivations**](RewardProgramActivationApi.md#fetchRewardProgramActivations) | **GET** /reward_program_activation | List reward program activations |


<a id="createRewardProgramActivation"></a>
# **createRewardProgramActivation**
> CreateRewardProgramActivationResponse createRewardProgramActivation(createRewardProgramActivationRequest)

Create a reward program activation

Create a reward program activation for a patient. There can only be one activation for a patient for a given reward program.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramActivationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramActivationApi apiInstance = new RewardProgramActivationApi(defaultClient);
    CreateRewardProgramActivationRequest createRewardProgramActivationRequest = new CreateRewardProgramActivationRequest(); // CreateRewardProgramActivationRequest | 
    try {
      CreateRewardProgramActivationResponse result = apiInstance.createRewardProgramActivation(createRewardProgramActivationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramActivationApi#createRewardProgramActivation");
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
| **createRewardProgramActivationRequest** | [**CreateRewardProgramActivationRequest**](CreateRewardProgramActivationRequest.md)|  | |

### Return type

[**CreateRewardProgramActivationResponse**](CreateRewardProgramActivationResponse.md)

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

<a id="fetchRewardProgramActivation"></a>
# **fetchRewardProgramActivation**
> FetchRewardProgramActivationResponse fetchRewardProgramActivation(id)

Get a reward program activation

Get a reward program activationrecord by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramActivationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramActivationApi apiInstance = new RewardProgramActivationApi(defaultClient);
    String id = "id_example"; // String | Reward program activation identifier
    try {
      FetchRewardProgramActivationResponse result = apiInstance.fetchRewardProgramActivation(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramActivationApi#fetchRewardProgramActivation");
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
| **id** | **String**| Reward program activation identifier | |

### Return type

[**FetchRewardProgramActivationResponse**](FetchRewardProgramActivationResponse.md)

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

<a id="fetchRewardProgramActivations"></a>
# **fetchRewardProgramActivations**
> FetchRewardProgramActivationsResponse fetchRewardProgramActivations(filterPatient, filterGroups, filterOrganization)

List reward program activations

Get a list of reward program activations matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramActivationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramActivationApi apiInstance = new RewardProgramActivationApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient identifier. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[groups]`, `filter[organization]`. 
    try {
      FetchRewardProgramActivationsResponse result = apiInstance.fetchRewardProgramActivations(filterPatient, filterGroups, filterOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramActivationApi#fetchRewardProgramActivations");
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
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |

### Return type

[**FetchRewardProgramActivationsResponse**](FetchRewardProgramActivationsResponse.md)

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

