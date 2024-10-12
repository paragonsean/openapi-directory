# HealthProfileApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchHealthProfile**](HealthProfileApi.md#fetchHealthProfile) | **GET** /health_profile/{id} | Get a health profile |
| [**fetchHealthProfiles**](HealthProfileApi.md#fetchHealthProfiles) | **GET** /health_profile | List health profiles |


<a id="fetchHealthProfile"></a>
# **fetchHealthProfile**
> FetchHealthProfileResponse fetchHealthProfile(id, include)

Get a health profile

Get a health profile by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthProfileApi apiInstance = new HealthProfileApi(defaultClient);
    String id = "id_example"; // String | Health profile identifier
    String include = "patient"; // String | List of related resources to include in the response
    try {
      FetchHealthProfileResponse result = apiInstance.fetchHealthProfile(id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthProfileApi#fetchHealthProfile");
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
| **id** | **String**| Health profile identifier | |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: patient, questions] |

### Return type

[**FetchHealthProfileResponse**](FetchHealthProfileResponse.md)

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

<a id="fetchHealthProfiles"></a>
# **fetchHealthProfiles**
> FetchHealthProfilesResponse fetchHealthProfiles(filterPatient, filterGroups, filterOrganization, pageNumber, pageSize, pageLimit, pageCursor, include)

List health profiles

Get a list of health profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthProfileApi apiInstance = new HealthProfileApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient id to fetch health profile. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    Integer pageNumber = 1; // Integer | Page number
    Integer pageSize = 10; // Integer | Page size
    Integer pageLimit = 50; // Integer | Page limit
    String pageCursor = "pageCursor_example"; // String | Page cursor
    String include = "patient"; // String | List of related resources to include in the response
    try {
      FetchHealthProfilesResponse result = apiInstance.fetchHealthProfiles(filterPatient, filterGroups, filterOrganization, pageNumber, pageSize, pageLimit, pageCursor, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthProfileApi#fetchHealthProfiles");
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
| **filterPatient** | **String**| Patient id to fetch health profile. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **pageNumber** | **Integer**| Page number | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size | [optional] [default to 10] |
| **pageLimit** | **Integer**| Page limit | [optional] [default to 50] |
| **pageCursor** | **String**| Page cursor | [optional] |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: patient, questions] |

### Return type

[**FetchHealthProfilesResponse**](FetchHealthProfilesResponse.md)

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
| **409** | Invalid Request |  -  |

