# AuthApi

All URIs are relative to *https://httpbin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**basicAuthUserPasswdGet**](AuthApi.md#basicAuthUserPasswdGet) | **GET** /basic-auth/{user}/{passwd} | Prompts the user for authorization using HTTP Basic Auth. |
| [**bearerGet**](AuthApi.md#bearerGet) | **GET** /bearer | Prompts the user for authorization using bearer authentication. |
| [**digestAuthQopUserPasswdAlgorithmGet**](AuthApi.md#digestAuthQopUserPasswdAlgorithmGet) | **GET** /digest-auth/{qop}/{user}/{passwd}/{algorithm} | Prompts the user for authorization using Digest Auth + Algorithm. |
| [**digestAuthQopUserPasswdAlgorithmStaleAfterGet**](AuthApi.md#digestAuthQopUserPasswdAlgorithmStaleAfterGet) | **GET** /digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after} | Prompts the user for authorization using Digest Auth + Algorithm. |
| [**digestAuthQopUserPasswdGet**](AuthApi.md#digestAuthQopUserPasswdGet) | **GET** /digest-auth/{qop}/{user}/{passwd} | Prompts the user for authorization using Digest Auth. |
| [**hiddenBasicAuthUserPasswdGet**](AuthApi.md#hiddenBasicAuthUserPasswdGet) | **GET** /hidden-basic-auth/{user}/{passwd} | Prompts the user for authorization using HTTP Basic Auth. |


<a id="basicAuthUserPasswdGet"></a>
# **basicAuthUserPasswdGet**
> basicAuthUserPasswdGet(user, passwd)

Prompts the user for authorization using HTTP Basic Auth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String user = "user_example"; // String | 
    String passwd = "passwd_example"; // String | 
    try {
      apiInstance.basicAuthUserPasswdGet(user, passwd);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#basicAuthUserPasswdGet");
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
| **user** | **String**|  | |
| **passwd** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful authentication. |  -  |
| **401** | Unsuccessful authentication. |  -  |

<a id="bearerGet"></a>
# **bearerGet**
> bearerGet(authorization)

Prompts the user for authorization using bearer authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String authorization = "authorization_example"; // String | 
    try {
      apiInstance.bearerGet(authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#bearerGet");
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
| **authorization** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful authentication. |  -  |
| **401** | Unsuccessful authentication. |  -  |

<a id="digestAuthQopUserPasswdAlgorithmGet"></a>
# **digestAuthQopUserPasswdAlgorithmGet**
> digestAuthQopUserPasswdAlgorithmGet(qop, user, passwd, algorithm)

Prompts the user for authorization using Digest Auth + Algorithm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String qop = "qop_example"; // String | auth or auth-int
    String user = "user_example"; // String | 
    String passwd = "passwd_example"; // String | 
    String algorithm = "MD5"; // String | MD5, SHA-256, SHA-512
    try {
      apiInstance.digestAuthQopUserPasswdAlgorithmGet(qop, user, passwd, algorithm);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#digestAuthQopUserPasswdAlgorithmGet");
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
| **qop** | **String**| auth or auth-int | |
| **user** | **String**|  | |
| **passwd** | **String**|  | |
| **algorithm** | **String**| MD5, SHA-256, SHA-512 | [default to MD5] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful authentication. |  -  |
| **401** | Unsuccessful authentication. |  -  |

<a id="digestAuthQopUserPasswdAlgorithmStaleAfterGet"></a>
# **digestAuthQopUserPasswdAlgorithmStaleAfterGet**
> digestAuthQopUserPasswdAlgorithmStaleAfterGet(qop, user, passwd, algorithm, staleAfter)

Prompts the user for authorization using Digest Auth + Algorithm.

allow settings the stale_after argument. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String qop = "qop_example"; // String | auth or auth-int
    String user = "user_example"; // String | 
    String passwd = "passwd_example"; // String | 
    String algorithm = "MD5"; // String | MD5, SHA-256, SHA-512
    String staleAfter = "never"; // String | 
    try {
      apiInstance.digestAuthQopUserPasswdAlgorithmStaleAfterGet(qop, user, passwd, algorithm, staleAfter);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#digestAuthQopUserPasswdAlgorithmStaleAfterGet");
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
| **qop** | **String**| auth or auth-int | |
| **user** | **String**|  | |
| **passwd** | **String**|  | |
| **algorithm** | **String**| MD5, SHA-256, SHA-512 | [default to MD5] |
| **staleAfter** | **String**|  | [default to never] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful authentication. |  -  |
| **401** | Unsuccessful authentication. |  -  |

<a id="digestAuthQopUserPasswdGet"></a>
# **digestAuthQopUserPasswdGet**
> digestAuthQopUserPasswdGet(qop, user, passwd)

Prompts the user for authorization using Digest Auth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String qop = "qop_example"; // String | auth or auth-int
    String user = "user_example"; // String | 
    String passwd = "passwd_example"; // String | 
    try {
      apiInstance.digestAuthQopUserPasswdGet(qop, user, passwd);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#digestAuthQopUserPasswdGet");
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
| **qop** | **String**| auth or auth-int | |
| **user** | **String**|  | |
| **passwd** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful authentication. |  -  |
| **401** | Unsuccessful authentication. |  -  |

<a id="hiddenBasicAuthUserPasswdGet"></a>
# **hiddenBasicAuthUserPasswdGet**
> hiddenBasicAuthUserPasswdGet(user, passwd)

Prompts the user for authorization using HTTP Basic Auth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://httpbin.org");

    AuthApi apiInstance = new AuthApi(defaultClient);
    String user = "user_example"; // String | 
    String passwd = "passwd_example"; // String | 
    try {
      apiInstance.hiddenBasicAuthUserPasswdGet(user, passwd);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#hiddenBasicAuthUserPasswdGet");
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
| **user** | **String**|  | |
| **passwd** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sucessful authentication. |  -  |
| **404** | Unsuccessful authentication. |  -  |

