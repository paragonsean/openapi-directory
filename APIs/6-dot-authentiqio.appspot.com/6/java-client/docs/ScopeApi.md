# ScopeApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**signConfirm**](ScopeApi.md#signConfirm) | **POST** /scope/{job} |  |
| [**signDelete**](ScopeApi.md#signDelete) | **DELETE** /scope/{job} |  |
| [**signRequest**](ScopeApi.md#signRequest) | **POST** /scope |  |
| [**signRetrieve**](ScopeApi.md#signRetrieve) | **GET** /scope/{job} |  |
| [**signRetrieveHead**](ScopeApi.md#signRetrieveHead) | **HEAD** /scope/{job} |  |
| [**signUpdate**](ScopeApi.md#signUpdate) | **PUT** /scope/{job} |  |


<a id="signConfirm"></a>
# **signConfirm**
> KeyBind200Response signConfirm(job)



this is a scope confirmation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    ScopeApi apiInstance = new ScopeApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      KeyBind200Response result = apiInstance.signConfirm(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeApi#signConfirm");
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

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successfully confirmed |  -  |
| **401** | Confirmation error &#x60;auth-error&#x60; |  -  |
| **404** | Job not found &#x60;unknown-job&#x60; |  -  |
| **405** | JWT POSTed to scope &#x60;not-supported&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signDelete"></a>
# **signDelete**
> KeyRevoke200Response signDelete(job)



delete a verification job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    ScopeApi apiInstance = new ScopeApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      KeyRevoke200Response result = apiInstance.signDelete(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeApi#signDelete");
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

[**KeyRevoke200Response**](KeyRevoke200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted |  -  |
| **404** | Job not found &#x60;unknown-job&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signRequest"></a>
# **signRequest**
> SignRequest201Response signRequest(claims, test)



scope verification request See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    ScopeApi apiInstance = new ScopeApi(defaultClient);
    Claims claims = new Claims(); // Claims | Claims of scope
    Integer test = 56; // Integer | test only mode, using test issuer
    try {
      SignRequest201Response result = apiInstance.signRequest(claims, test);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeApi#signRequest");
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
| **claims** | [**Claims**](Claims.md)| Claims of scope | |
| **test** | **Integer**| test only mode, using test issuer | [optional] |

### Return type

[**SignRequest201Response**](SignRequest201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful response |  -  |
| **429** | Too Many Requests on same address / number &#x60;rate-limit&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signRetrieve"></a>
# **signRetrieve**
> JWT1 signRetrieve(job)



get the status / current content of a verification job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    ScopeApi apiInstance = new ScopeApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      JWT1 result = apiInstance.signRetrieve(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeApi#signRetrieve");
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

<a id="signRetrieveHead"></a>
# **signRetrieveHead**
> signRetrieveHead(job)



HEAD to get the status of a verification job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    ScopeApi apiInstance = new ScopeApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      apiInstance.signRetrieveHead(job);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeApi#signRetrieveHead");
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

<a id="signUpdate"></a>
# **signUpdate**
> SignUpdate200Response signUpdate(job)



authority updates a JWT with its signature See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    ScopeApi apiInstance = new ScopeApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      SignUpdate200Response result = apiInstance.signUpdate(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeApi#signUpdate");
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

[**SignUpdate200Response**](SignUpdate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwt, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated |  -  |
| **404** | Job not found &#x60;unknown-job&#x60; |  -  |
| **409** | Job not confirmed yet &#x60;confirm-first&#x60; |  -  |
| **0** | Error response |  -  |

