# RewardProgramApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRewardProgram**](RewardProgramApi.md#createRewardProgram) | **POST** /reward_program | Create a reward program |
| [**fetchRewardProgram**](RewardProgramApi.md#fetchRewardProgram) | **GET** /reward_program/{id} | Get a reward program |
| [**fetchRewardProgramGroup**](RewardProgramApi.md#fetchRewardProgramGroup) | **GET** /reward_program/{id}/group | Get group for a reward program |
| [**fetchRewardPrograms**](RewardProgramApi.md#fetchRewardPrograms) | **GET** /reward_program | List reward programs |


<a id="createRewardProgram"></a>
# **createRewardProgram**
> CreateRewardProgramResponse createRewardProgram(createRewardProgramRequest)

Create a reward program

Create a reward program for a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramApi apiInstance = new RewardProgramApi(defaultClient);
    CreateRewardProgramRequest createRewardProgramRequest = new CreateRewardProgramRequest(); // CreateRewardProgramRequest | 
    try {
      CreateRewardProgramResponse result = apiInstance.createRewardProgram(createRewardProgramRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramApi#createRewardProgram");
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
| **createRewardProgramRequest** | [**CreateRewardProgramRequest**](CreateRewardProgramRequest.md)|  | |

### Return type

[**CreateRewardProgramResponse**](CreateRewardProgramResponse.md)

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

<a id="fetchRewardProgram"></a>
# **fetchRewardProgram**
> FetchRewardProgramResponse fetchRewardProgram(id)

Get a reward program

Get a reward program record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramApi apiInstance = new RewardProgramApi(defaultClient);
    String id = "id_example"; // String | Reward program identifier
    try {
      FetchRewardProgramResponse result = apiInstance.fetchRewardProgram(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramApi#fetchRewardProgram");
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
| **id** | **String**| Reward program identifier | |

### Return type

[**FetchRewardProgramResponse**](FetchRewardProgramResponse.md)

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

<a id="fetchRewardProgramGroup"></a>
# **fetchRewardProgramGroup**
> FetchGroupsResponse fetchRewardProgramGroup(id)

Get group for a reward program

Get the group related to a reward program.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramApi apiInstance = new RewardProgramApi(defaultClient);
    String id = "id_example"; // String | Reward program identifier
    try {
      FetchGroupsResponse result = apiInstance.fetchRewardProgramGroup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramApi#fetchRewardProgramGroup");
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
| **id** | **String**| Reward program identifier | |

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

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

<a id="fetchRewardPrograms"></a>
# **fetchRewardPrograms**
> FetchRewardProgramsResponse fetchRewardPrograms(filterGroups, filterOrganization)

List reward programs

Get a list of reward programs matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    RewardProgramApi apiInstance = new RewardProgramApi(defaultClient);
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group identifiers. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
    try {
      FetchRewardProgramsResponse result = apiInstance.fetchRewardPrograms(filterGroups, filterOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardProgramApi#fetchRewardPrograms");
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
| **filterGroups** | **String**| Comma-separated list of group identifiers. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |

### Return type

[**FetchRewardProgramsResponse**](FetchRewardProgramsResponse.md)

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

