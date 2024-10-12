# DeleteApi

All URIs are relative to *https://6-dot-authentiqio.appspot.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyRevokeNosecret_0**](DeleteApi.md#keyRevokeNosecret_0) | **DELETE** /key |  |
| [**keyRevoke_0**](DeleteApi.md#keyRevoke_0) | **DELETE** /key/{PK} |  |
| [**signDelete_0**](DeleteApi.md#signDelete_0) | **DELETE** /scope/{job} |  |


<a id="keyRevokeNosecret_0"></a>
# **keyRevokeNosecret_0**
> KeyRevokeNosecret200Response keyRevokeNosecret_0(email, phone, code)



Revoke an Authentiq ID using email &amp; phone.  If called with &#x60;email&#x60; and &#x60;phone&#x60; only, a verification code  will be sent by email. Do a second call adding &#x60;code&#x60; to  complete the revocation. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String email = "email_example"; // String | primary email associated to Key (ID)
    String phone = "phone_example"; // String | primary phone number, international representation
    String code = "code_example"; // String | verification code sent by email
    try {
      KeyRevokeNosecret200Response result = apiInstance.keyRevokeNosecret_0(email, phone, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#keyRevokeNosecret_0");
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
| **email** | **String**| primary email associated to Key (ID) | |
| **phone** | **String**| primary phone number, international representation | |
| **code** | **String**| verification code sent by email | [optional] |

### Return type

[**KeyRevokeNosecret200Response**](KeyRevokeNosecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted |  -  |
| **401** | Authentication error &#x60;auth-error&#x60; |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **409** | Confirm with code sent &#x60;confirm-first&#x60; |  -  |
| **0** | Error response |  -  |

<a id="keyRevoke_0"></a>
# **keyRevoke_0**
> KeyRevoke200Response keyRevoke_0(PK, secret)



Revoke an Identity (Key) with a revocation secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String PK = "PK_example"; // String | Public Signing Key - Authentiq ID (43 chars)
    String secret = "secret_example"; // String | revokation secret
    try {
      KeyRevoke200Response result = apiInstance.keyRevoke_0(PK, secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#keyRevoke_0");
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
| **secret** | **String**| revokation secret | |

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
| **200** | Successful response |  -  |
| **401** | Key not found / wrong code &#x60;auth-error&#x60; |  -  |
| **404** | Unknown key &#x60;unknown-key&#x60; |  -  |
| **0** | Error response |  -  |

<a id="signDelete_0"></a>
# **signDelete_0**
> KeyRevoke200Response signDelete_0(job)



delete a verification job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://6-dot-authentiqio.appspot.com");

    DeleteApi apiInstance = new DeleteApi(defaultClient);
    String job = "job_example"; // String | Job ID (20 chars)
    try {
      KeyRevoke200Response result = apiInstance.signDelete_0(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteApi#signDelete_0");
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

