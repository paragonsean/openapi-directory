# NearMissesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adminNearMissesRequestPatternPost**](NearMissesApi.md#adminNearMissesRequestPatternPost) | **POST** /__admin/near-misses/request-pattern | Find near misses matching request pattern |
| [**adminNearMissesRequestPost**](NearMissesApi.md#adminNearMissesRequestPost) | **POST** /__admin/near-misses/request | Find near misses matching specific request |
| [**adminRequestsUnmatchedNearMissesGet**](NearMissesApi.md#adminRequestsUnmatchedNearMissesGet) | **GET** /__admin/requests/unmatched/near-misses |  |


<a id="adminNearMissesRequestPatternPost"></a>
# **adminNearMissesRequestPatternPost**
> AdminNearMissesRequestPost200Response adminNearMissesRequestPatternPost(adminMappingsGet200ResponseMappingsInnerRequest)

Find near misses matching request pattern

Find at most 3 near misses for closest logged requests to the specified request pattern

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NearMissesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NearMissesApi apiInstance = new NearMissesApi(defaultClient);
    AdminMappingsGet200ResponseMappingsInnerRequest adminMappingsGet200ResponseMappingsInnerRequest = new AdminMappingsGet200ResponseMappingsInnerRequest(); // AdminMappingsGet200ResponseMappingsInnerRequest | 
    try {
      AdminNearMissesRequestPost200Response result = apiInstance.adminNearMissesRequestPatternPost(adminMappingsGet200ResponseMappingsInnerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NearMissesApi#adminNearMissesRequestPatternPost");
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
| **adminMappingsGet200ResponseMappingsInnerRequest** | [**AdminMappingsGet200ResponseMappingsInnerRequest**](AdminMappingsGet200ResponseMappingsInnerRequest.md)|  | |

### Return type

[**AdminNearMissesRequestPost200Response**](AdminNearMissesRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Near misses matching criteria |  -  |

<a id="adminNearMissesRequestPost"></a>
# **adminNearMissesRequestPost**
> AdminNearMissesRequestPost200Response adminNearMissesRequestPost(adminNearMissesRequestPostRequest)

Find near misses matching specific request

Find at most 3 near misses for closest stub mappings to the specified request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NearMissesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NearMissesApi apiInstance = new NearMissesApi(defaultClient);
    AdminNearMissesRequestPostRequest adminNearMissesRequestPostRequest = new AdminNearMissesRequestPostRequest(); // AdminNearMissesRequestPostRequest | 
    try {
      AdminNearMissesRequestPost200Response result = apiInstance.adminNearMissesRequestPost(adminNearMissesRequestPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NearMissesApi#adminNearMissesRequestPost");
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
| **adminNearMissesRequestPostRequest** | [**AdminNearMissesRequestPostRequest**](AdminNearMissesRequestPostRequest.md)|  | |

### Return type

[**AdminNearMissesRequestPost200Response**](AdminNearMissesRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Near misses matching criteria |  -  |

<a id="adminRequestsUnmatchedNearMissesGet"></a>
# **adminRequestsUnmatchedNearMissesGet**
> AdminNearMissesRequestPost200Response adminRequestsUnmatchedNearMissesGet()



Retrieve near-misses for all unmatched requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NearMissesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    NearMissesApi apiInstance = new NearMissesApi(defaultClient);
    try {
      AdminNearMissesRequestPost200Response result = apiInstance.adminRequestsUnmatchedNearMissesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NearMissesApi#adminRequestsUnmatchedNearMissesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminNearMissesRequestPost200Response**](AdminNearMissesRequestPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Near misses matching criteria |  -  |

