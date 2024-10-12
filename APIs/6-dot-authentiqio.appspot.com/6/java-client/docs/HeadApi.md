# HeadApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyPKHead_0**](HeadApi.md#keyPKHead_0) | **HEAD** /key/{PK} |  |
| [**signRetrieveHead_0**](HeadApi.md#signRetrieveHead_0) | **HEAD** /scope/{job} |  |


<a id="keyPKHead_0"></a>
# **keyPKHead_0**
> keyPKHead_0(PK)



HEAD info on Authentiq ID 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    HeadApi apiInstance = new HeadApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    try {
      apiInstance.keyPKHead_0(PK);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeadApi#keyPKHead_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Key exists |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **410** | Key is revoked &#x60;revoked-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signRetrieveHead_0"></a>
# **signRetrieveHead_0**
> signRetrieveHead_0(job)



HEAD to get the status of a verification job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    HeadApi apiInstance = new HeadApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      apiInstance.signRetrieveHead_0(job);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeadApi#signRetrieveHead_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Confirmed and signed |  -  |
| **204** | Confirmed, waiting for signing |  -  |
| **404** | Job not found &#x60;unknown-job&#x60; |  -  |
| **0** | Error response |  -  |

