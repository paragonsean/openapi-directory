# TokenVerificationApi

All URIs are relative to *https://api.tokenjay.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkToken**](TokenVerificationApi.md#checkToken) | **GET** /tokens/check/{tokenId}/{tokenName} | Check a token verification |
| [**listBlocked**](TokenVerificationApi.md#listBlocked) | **GET** /tokens/listBlocked | Lists all blocked tokens |
| [**listGenuine**](TokenVerificationApi.md#listGenuine) | **GET** /tokens/listGenuine | Lists all genuine tokens known |


<a id="checkToken"></a>
# **checkToken**
> CheckResponse checkToken(tokenId, tokenName)

Check a token verification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    TokenVerificationApi apiInstance = new TokenVerificationApi(defaultClient);
    String tokenId = "tokenId_example"; // String | 
    String tokenName = "tokenName_example"; // String | 
    try {
      CheckResponse result = apiInstance.checkToken(tokenId, tokenName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenVerificationApi#checkToken");
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
| **tokenId** | **String**|  | |
| **tokenName** | **String**|  | |

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="listBlocked"></a>
# **listBlocked**
> List&lt;String&gt; listBlocked()

Lists all blocked tokens

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    TokenVerificationApi apiInstance = new TokenVerificationApi(defaultClient);
    try {
      List<String> result = apiInstance.listBlocked();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenVerificationApi#listBlocked");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="listGenuine"></a>
# **listGenuine**
> List&lt;GenuineToken&gt; listGenuine()

Lists all genuine tokens known

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TokenVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tokenjay.app");

    TokenVerificationApi apiInstance = new TokenVerificationApi(defaultClient);
    try {
      List<GenuineToken> result = apiInstance.listGenuine();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TokenVerificationApi#listGenuine");
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

[**List&lt;GenuineToken&gt;**](GenuineToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

