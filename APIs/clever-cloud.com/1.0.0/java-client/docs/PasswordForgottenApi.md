# PasswordForgottenApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPasswordForgottenKey_0**](PasswordForgottenApi.md#getPasswordForgottenKey_0) | **GET** /password_forgotten/{key} |  |
| [**getPasswordForgotten_0**](PasswordForgottenApi.md#getPasswordForgotten_0) | **GET** /password_forgotten |  |
| [**postPasswordForgottenKey_0**](PasswordForgottenApi.md#postPasswordForgottenKey_0) | **POST** /password_forgotten/{key} |  |
| [**postPasswordForgotten_0**](PasswordForgottenApi.md#postPasswordForgotten_0) | **POST** /password_forgotten |  |


<a id="getPasswordForgottenKey_0"></a>
# **getPasswordForgottenKey_0**
> getPasswordForgottenKey_0(key)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordForgottenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PasswordForgottenApi apiInstance = new PasswordForgottenApi(defaultClient);
    String key = "key_example"; // String | 
    try {
      apiInstance.getPasswordForgottenKey_0(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordForgottenApi#getPasswordForgottenKey_0");
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
| **key** | **String**|  | |

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
| **200** | confirmPasswordResetRequest |  -  |

<a id="getPasswordForgotten_0"></a>
# **getPasswordForgotten_0**
> getPasswordForgotten_0()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordForgottenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PasswordForgottenApi apiInstance = new PasswordForgottenApi(defaultClient);
    try {
      apiInstance.getPasswordForgotten_0();
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordForgottenApi#getPasswordForgotten_0");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getPasswordForgottenForm |  -  |

<a id="postPasswordForgottenKey_0"></a>
# **postPasswordForgottenKey_0**
> postPasswordForgottenKey_0(key, pass, pass2)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordForgottenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PasswordForgottenApi apiInstance = new PasswordForgottenApi(defaultClient);
    String key = "key_example"; // String | 
    String pass = "pass_example"; // String | 
    String pass2 = "pass2_example"; // String | 
    try {
      apiInstance.postPasswordForgottenKey_0(key, pass, pass2);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordForgottenApi#postPasswordForgottenKey_0");
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
| **key** | **String**|  | |
| **pass** | **String**|  | [optional] |
| **pass2** | **String**|  | [optional] |

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
| **200** | resetPasswordForgotten |  -  |

<a id="postPasswordForgotten_0"></a>
# **postPasswordForgotten_0**
> postPasswordForgotten_0(login, dropTokens, testerPass)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordForgottenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    PasswordForgottenApi apiInstance = new PasswordForgottenApi(defaultClient);
    String login = "login_example"; // String | 
    String dropTokens = "dropTokens_example"; // String | 
    String testerPass = "testerPass_example"; // String | 
    try {
      apiInstance.postPasswordForgotten_0(login, dropTokens, testerPass);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordForgottenApi#postPasswordForgotten_0");
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
| **login** | **String**|  | [optional] |
| **dropTokens** | **String**|  | [optional] |
| **testerPass** | **String**|  | [optional] |

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
| **200** | askForPasswordResetViaForm |  -  |

