# CoachApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchCoach**](CoachApi.md#fetchCoach) | **GET** /coach/{id} | Get a coach |
| [**fetchCoaches**](CoachApi.md#fetchCoaches) | **GET** /coach | List coaches |


<a id="fetchCoach"></a>
# **fetchCoach**
> FetchCoachResponse fetchCoach(id)

Get a coach

Get a coach record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoachApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CoachApi apiInstance = new CoachApi(defaultClient);
    String id = "id_example"; // String | Coach identifier
    try {
      FetchCoachResponse result = apiInstance.fetchCoach(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoachApi#fetchCoach");
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
| **id** | **String**| Coach identifier | |

### Return type

[**FetchCoachResponse**](FetchCoachResponse.md)

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

<a id="fetchCoaches"></a>
# **fetchCoaches**
> FetchCoachesResponse fetchCoaches(filterGroups, filterOrganization)

List coaches

Get a list of coaches matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoachApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    CoachApi apiInstance = new CoachApi(defaultClient);
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[groups]`, `filter[organization]`. 
    try {
      FetchCoachesResponse result = apiInstance.fetchCoaches(filterGroups, filterOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoachApi#fetchCoaches");
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
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[groups]&#x60;, &#x60;filter[organization]&#x60;.  | [optional] |

### Return type

[**FetchCoachesResponse**](FetchCoachesResponse.md)

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

