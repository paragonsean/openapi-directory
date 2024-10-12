# AudiencesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**audiencesGet**](AudiencesApi.md#audiencesGet) | **GET** /audiences |  |
| [**audiencesIDGet**](AudiencesApi.md#audiencesIDGet) | **GET** /audiences/{ID} |  |
| [**audiencesIDMembershipsPost**](AudiencesApi.md#audiencesIDMembershipsPost) | **POST** /audiences/{ID}/memberships |  |


<a id="audiencesGet"></a>
# **audiencesGet**
> EndpointGetAudiences audiencesGet(offset, limit)



Fetch all Daniapp audience segments that comprise the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudiencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    AudiencesApi apiInstance = new AudiencesApi(defaultClient);
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetAudiences result = apiInstance.audiencesGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudiencesApi#audiencesGet");
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
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetAudiences**](EndpointGetAudiences.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="audiencesIDGet"></a>
# **audiencesIDGet**
> EndpointGetAudiencesID audiencesIDGet(ID)



Fetch an array of Daniapp audience segments that comprise the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudiencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    AudiencesApi apiInstance = new AudiencesApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetAudiencesID result = apiInstance.audiencesIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudiencesApi#audiencesIDGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetAudiencesID**](EndpointGetAudiencesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="audiencesIDMembershipsPost"></a>
# **audiencesIDMembershipsPost**
> EndpointPostAudiencesIDMemberships audiencesIDMembershipsPost(ID)



Create a membership record for the OAuth&#39;ed end-user based on the current audience segment/bubble combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AudiencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    AudiencesApi apiInstance = new AudiencesApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointPostAudiencesIDMemberships result = apiInstance.audiencesIDMembershipsPost(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AudiencesApi#audiencesIDMembershipsPost");
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
| **ID** | **Integer**|  | |

### Return type

[**EndpointPostAudiencesIDMemberships**](EndpointPostAudiencesIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

