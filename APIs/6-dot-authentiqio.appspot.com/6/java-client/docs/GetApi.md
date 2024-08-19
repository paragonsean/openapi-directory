# GetApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyRetrieve_0**](GetApi.md#keyRetrieve_0) | **GET** /key/{PK} |  |
| [**signRetrieve_0**](GetApi.md#signRetrieve_0) | **GET** /scope/{job} |  |


<a id="keyRetrieve_0"></a>
# **keyRetrieve_0**
> JWT keyRetrieve_0(PK)



Get public details of an Authentiq ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    try {
      JWT result = apiInstance.keyRetrieve_0(PK);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#keyRetrieve_0");
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
| **PK** | **String**| Public Signing Key - Authentiq ID (43 chars) | |

### Return type

[**JWT**](JWT.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **410** | Key is revoked (gone). &#x60;revoked-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signRetrieve_0"></a>
# **signRetrieve_0**
> JWT1 signRetrieve_0(job)



get the status / current content of a verification job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    GetApi apiInstance = new GetApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      JWT1 result = apiInstance.signRetrieve_0(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#signRetrieve_0");
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
| **job** | **String**| Job ID (20 chars) | |

### Return type

[**JWT1**](JWT1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/jwt, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response (JWT) |  -  |
| **204** | Confirmed, waiting for signing |  -  |
| **404** | Job not found &#x60;unknown-job&#x60; |  -  |
| **0** | Error response |  -  |

