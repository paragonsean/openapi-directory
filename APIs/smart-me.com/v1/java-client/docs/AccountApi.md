# AccountApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountLogin**](AccountApi.md#accountLogin) | **GET** /api/Account/login |  |
| [**apiAccountLoginPost**](AccountApi.md#apiAccountLoginPost) | **POST** /api/Account/login |  |


<a id="accountLogin"></a>
# **accountLogin**
> Object accountLogin()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      Object result = apiInstance.accountLogin();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountLogin");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiAccountLoginPost"></a>
# **apiAccountLoginPost**
> Object apiAccountLoginPost()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      Object result = apiInstance.apiAccountLoginPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#apiAccountLoginPost");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

