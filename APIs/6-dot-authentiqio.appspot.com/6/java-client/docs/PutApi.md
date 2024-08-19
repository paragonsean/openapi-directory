# PutApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyBind_0**](PutApi.md#keyBind_0) | **PUT** /key/{PK} |  |
| [**signUpdate_0**](PutApi.md#signUpdate_0) | **PUT** /scope/{job} |  |


<a id="keyBind_0"></a>
# **keyBind_0**
> KeyBind200Response keyBind_0(PK, authentiqID)



Update Authentiq ID by replacing the object.  v4: &#x60;JWT(sub,email,phone)&#x60; to bind email/phone hash;   v5: POST issuer-signed email &amp; phone scopes and PUT to update registration &#x60;JWT(sub, pk, devtoken, ...)&#x60;  See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PutApi apiInstance = new PutApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    AuthentiqID authentiqID = new AuthentiqID(); // AuthentiqID | Authentiq ID to register
    try {
      KeyBind200Response result = apiInstance.keyBind_0(PK, authentiqID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#keyBind_0");
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
| **authentiqID** | [**AuthentiqID**](AuthentiqID.md)| Authentiq ID to register | |

### Return type

[**KeyBind200Response**](KeyBind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/jwt
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **409** | Already bound to another key &#x60;duplicate-hash&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signUpdate_0"></a>
# **signUpdate_0**
> SignUpdate200Response signUpdate_0(job)



authority updates a JWT with its signature See: https://github.com/skion/authentiq/wiki/JWT-Examples 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    PutApi apiInstance = new PutApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      SignUpdate200Response result = apiInstance.signUpdate_0(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PutApi#signUpdate_0");
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

